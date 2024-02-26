import scipy.optimize as opt
from MRP import MRPReading, MRPReadingEntry
from MRP import MRPAnalysis
from MRP import MRPDataVisualization

def CUSTOM_apply_sensor_temperature_calibration(_readings_to_calibrate: [MRPReading.MRPReading], _temperature_calibration_readings: [MRPReading.MRPReading]) -> [MRPReading.MRPReading]:
    # REMOVE OFFSET
    zero_offset: float = 0.0
    for reading in _temperature_calibration_readings:
        zero_offset = min([zero_offset, abs(MRPAnalysis.MRPAnalysis.calculate_mean(reading))])
    # EXTRACT TEMPERATURES

    cr_temp: [float] = []
    cr_means: [float] = []
    for r in _temperature_calibration_readings:
        mean_temp: float = MRPAnalysis.MRPAnalysis.calculate_mean(r, _temperature_axis=True)
        cr_temp.append(mean_temp)

    rsorted: [MRPReading.MRPReading] = [v for _, v in sorted(zip(cr_temp, _temperature_calibration_readings))]

    cr_temp: [float] = []
    cr_means: [float] = []
    for r in rsorted:
        mean: float = MRPAnalysis.MRPAnalysis.calculate_mean(r)
        mean_temp: float = MRPAnalysis.MRPAnalysis.calculate_mean(r, _temperature_axis=True)
        cr_means.append(zero_offset - mean)
        cr_temp.append(mean_temp)
        print("reading imported for temp calibration {} m={:.2} c={:.2}".format(r.get_name(), mean_temp, mean))

    # PERFORM LINEAR FUNCTION FITTING
    a: float = 1.0
    b: float = 0.0
    try:
        opt_params, pcov = opt.curve_fit(MRPDataVisualization.MRPDataVisualization.linear_curve_func, cr_temp, cr_means)
        a = opt_params[0]
        b = opt_params[1]


    except Exception as e:
        print("cant fit temperature linear funtion")

    return_readings: [MRPReading.MRPReading] = []
    # FINALLY RUN THE CALIBRATION RUN
    for e in _readings_to_calibrate:
        nr: MRPReading.MRPReading = MRPReading.MRPReading()
        nr.load_from_dict(e.dump_to_dict())
        nr.data = []
        for dp in e.data:
            tfp: MRPReadingEntry = dp
            dp_value: float = tfp.value
            dp_temp: float = tfp.temperature
            offset = MRPDataVisualization.MRPDataVisualization.linear_curve_func(dp_temp, a, b)

            print("apply temp offset of {:.2} for m={:.2}".format(offset, dp_temp))
            tfp.value = tfp.value - offset
            nr.data.append(tfp)
        return_readings.append(nr)
    return return_readings
