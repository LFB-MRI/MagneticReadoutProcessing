from pathlib import Path
import numpy as np
# IMPORT SOME HELPER FUNCTIONS FOR IMPORT EXPORT AND PLOTTING
from MRPudpp.UDPPFunctionCollection import UDPPFunctionCollection as mrphelper
from MRP import MRPAnalysis, MRPPolarVisualization, MRPReading, MRPReadingEntry
# IMPORT OTHER FUNTIONS


# GET FOLDER PATH WITH EXAMPLE READINGS
READINGS_STORAGE_FOLDER: str = str(Path.joinpath(Path(__file__).parent, Path("readings/example")))
RESULT_STORAGE_FOLDER: str = str(Path.joinpath(Path(__file__).parent, Path("out")))

def main():
    # IMPORT READINGS
    print("READINGS FOLDER PATH: {}".format(READINGS_STORAGE_FOLDER))
    magnet_readings: List(MRPReading.MRPReading) = mrphelper.import_readings(READINGS_STORAGE_FOLDER, "fullsphere_magnet_(.)*.mag.json")
    bias_reading: [MRPReading.MRPReading]  = mrphelper.import_readings(READINGS_STORAGE_FOLDER, "fullsphere_bias.mag.json")
    print("found {} magnet readings and {} bias readings".format(len(magnet_readings), len(bias_reading)))

    # REMOVE READING BIAS USING THE BIAS READING / EMPTY READING
    magnet_readings: [MRPReading.MRPReading] = mrphelper.apply_sensor_bias_offset(bias_reading, magnet_readings)

    # CALCULATE CENTER OF GRAVITY
    cog: (float, float, float) = MRPAnalysis.MRPAnalysis.calculate_center_of_gravity(magnet_readings[0])
    print("CoG for magnet 0 is {}".format(cog))

    # CALCULATE MEAN 
    mean: float = MRPAnalysis.MRPAnalysis.calculate_mean(magnet_readings[1])
    print("mean for magnet 1 is {:.2}".format(mean))


    # ADVANCED DATA ACCESS
    # entry is type of MRPReadingEntry.MRPReadingEntry
    for entry in magnet_readings[0]:
        pass
        #entry.temperature()
        #entry.value()
        #entry.is_valid()
        #entry.id()
    


    # RAW DATA ACCESS
    plain_array = magnet_readings[0].to_value_array()

    
    # PLOT READINGS USING MATHPLOTLIB TO FILE
    # Please see MRP.MRPDataVisualization file for further examples
    mrphelper.plot_readings(magnet_readings, "example plot", RESULT_STORAGE_FOLDER)
    
if __name__ == '__main__':
    main()
