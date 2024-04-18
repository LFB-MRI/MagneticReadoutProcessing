from pathlib import Path
import numpy as np
# IMPORT SOME HELPER FUNCTIONS FOR IMPORT EXPORT AND PLOTTING
from MRPudpp.UDPPFunctionCollection import UDPPFunctionCollection as mrphelper
from MRP import MRPAnalysis, MRPPolarVisualization, MRPReading, MRPReadingEntry, MRPPolarVisualization, MRPMagnetTypes, MRPMeasurementConfig
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


    # GET META-DATA ABOUT THE READING
    # SEE MRP.MRPMagnetTypes FOR POSSIBLE VALUES
    meta_data_reading = magnet_readings[0]
    magnet_type: MRPMagnetTypes.MagnetType = meta_data_reading.get_magnet_type() # SCANNED MAGNET TYPE SUCH AS N45_CUBIC_12x12x12 or NOT_SPECIFIED

    measurement_config: MRPMeasurementConfig.MRPMeasurementConfig = meta_data_reading.measurement_config
    measurement_config.sensor_id() # USED SENSOR ID
        

    

    # RAW MEASUREMENT DATA ACCESS
    # entry is type of MRPReadingEntry.MRPReadingEntry
    for entry in magnet_readings[0].data:
        # MEASURED B VALUE OF THE DATAPOINT
        entry.value()
        # MEASURED SENSOR TEMPERATURE VALUE OF THE DATAPOINT
        entry.temperature()


        # FOR FULLSPHERE READINGS THE COORDINATES IN POLAR SPACE ARE EMBEDDED INTO THE READING STRUCTURE
        entry.theta()
        entry.phi()
        
        # SOME OTHER INFORMATION
        entry.is_valid() # SENSOR REPSONDS WITH VALID VALUES
        entry.id() # ID OF THE READING STARTING FROM 0 TO LEN(data) = MAX READINGS
        #...
        
    


    # RAW DATA ACCESS
    plain_array = magnet_readings[0].to_value_array()

    
    # PLOT READINGS USING MATHPLOTLIB TO FILE
    # Please see MRP.MRPDataVisualization file for further examples
    mrphelper.plot_readings(magnet_readings, "example plot", RESULT_STORAGE_FOLDER)

    # IF A FULLSPHERE READING IS IMPORTED ITS POSSIBLE TO PLOT THE FULL SPHERE
    # Please refer to MRP.MRPPolarVisualization file for further usage documentation
    mrphelper.plot_fullsphere(magnet_readings, "example fullsphere plot", RESULT_STORAGE_FOLDER)
    
if __name__ == '__main__':
    main()
