import os
import re

from MRP import MRPReading, MRPReadingEntry

result_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "extracted")
import_folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "")

if not os.path.exists(result_folder_path):
    os.makedirs(result_folder_path)


initial_temp: int = 20

files = [f for f in os.listdir(import_folder_path) if re.match(r'(.)*TEMPERATURE=COMBINED(.)*.mag.json', f)]

for e in files:
    reading: MRPReading.MRPReading = MRPReading.MRPReading()

    name: str = e.replace("COMBINED", "%").replace(".mag","").replace(".json", "")
    reading.load_from_file(os.path.join(import_folder_path, e))



    values: [float] = reading.to_value_array()
    #values = [v for _, v in sorted(zip(values, values))]

    for tidx, tv in enumerate(values):
        new_reading: MRPReading.MRPReading = MRPReading.MRPReading()
        new_reading.set_name(name.replace("%", "{}".format(tidx+initial_temp)))

        bef: int = new_reading.len()
        for i in range(100):
            e: MRPReadingEntry.MRPReadingEntry = MRPReadingEntry.MRPReadingEntry()
            e.value = tv
            e.id = bef + i
            e.is_valid = True
            e.temperature = tidx+initial_temp
            new_reading.insert_reading_instance(e, _autoupdate_measurement_config=False)

        export_path: str = os.path.join(result_folder_path, new_reading.get_name().replace(" ", "_")+ "_NTS" + ".mag.json")
        new_reading.dump_to_file(export_path)