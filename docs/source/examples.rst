Examples
########

Installation/Usage:
*******************
As the package has not been published on PyPi yet, it CANNOT be install using pip.

Installation DEV
================

For now, the suggested method is to copy the ``MagneticReadoutProcessing`` folder into your Python project folder.
There are some other packages required which are listed in the ``requirements.txt``.
To install them use ``$ pip3 install -r requirements.txt`` command.

.. code-block:: console

    $ git clone https://github.com/LFB-MRI/MagneticReadoutProcessing ./MagneticReadoutProcessing
    $ cd ./MagneticReadoutProcessing
    $ pip3 install -r requirements.txt
    # COPY LIB TO YOUR PROJECT
    $ cp -R ./MagneticReadoutProcessing ~/yourPythonProject/



Installation PROD
=================

The other method is to use the ``setup.py`` to install ``MagneticReadoutProcessing`` as module:

.. code-block:: console

    $ git clone https://github.com/LFB-MRI/MagneticReadoutProcessing ./MagneticReadoutProcessing
    $ cd ./MagneticReadoutProcessing
    $ python ./setup.py install


.. note::
   There are further detailed examples in the ``test`` folder. There is a seperate test file for each submodule.



MRPReading Examples
*******************

Create a minimal measurement
============================

.. code-block:: python

    import MRPConfig
    import MRPReading
    import numpy as np
    from tqdm import tqdm
    import math
    # CREATE A CONFIG INSTANCE
    # HERE SOME PARAMETERS ABOUT THE READING AND MEASUREMENTS ARE STORED
    # ITS POSSIBLE TO LOAD THESE VALUES USING A INI FILE
    # PLEASE NOTICE THE MRPConfig MEMBERS
    Config = MRPConfig.MRPConfig()

    # SETUP SOME DETAILS ABOUT THE MEASUREMENT
    # WE WANT TO CREATE A HALF-SPHERE SCAN
    Config.MEASUREMENT_HORIZONTAL_RESOLUTION = 36
    Config.MEASUREMENT_VERTICAL_RESOLUTION = 18
    Config.MEASUREMENT_HORIZONTAL_AXIS_DEGREE = 360
    Config.MEASUREMENT_VERTICAL_AXIS_DEGREE = 180



    # CREATE A READING INSTANCE TO STORE THE READ DATA IN
    # HERE THE Config FROM ABOVE IS PASSED TO SET THE METADATA
    reading = MRPReading.MRPReading(Config)

    # CREATE A POLAR HALF SPHERE GRID TO ITERATE OVER
    n_phi = Config.MEASUREMENT_HORIZONTAL_RESOLUTION
    n_theta = Config.MEASUREMENT_VERTICAL_RESOLUTION
    phi_radians = math.radians(Config.MEASUREMENT_HORIZONTAL_AXIS_DEGREE)
    theta_radians = math.radians(Config.MEASUREMENT_VERTICAL_AXIS_DEGREE)
    # CREATE A POLAR COORDINATE GRID TO ITERATE OVER
    theta, phi = np.mgrid[0.0:0.5 * np.pi:n_theta * 1j, 0.0:2.0 * np.pi:n_phi * 1j]


    # FINALLY INSERT THE MEASUREMENT-DATA
    reading_index_theta = 0
    reading_index_phi = 0
    # TQDM IS USED TO SHOW A PROGRESSBAR IN RUNNING SHELL
    progressbar = tqdm(phi[0, :], desc ="Progress: ")
    for j in progressbar:
        reading_index_phi = reading_index_phi + 1
        reading_index_theta = 0
        for i in theta[:, 0]:
            reading_index_theta = reading_index_theta + 1
            # i = VERTICAL 0-90
            # j = HORIZONTAL 0-360
            horizontal_degree = math.degrees(j)
            vertical_degree = math.degrees(i)


            # READOUT THE SENSOR
            value = 0.2 # mT
            temp = 25.0 # DEGREE C

            # SAVE RESULT
            reading.insert_reading(value, j, i, reading_index_phi, reading_index_theta, temp)


            # UPDATE CONSOLE OUTPUT WITH THE CURRENT READOUT AND POSITION
            progressbar.set_description("X:{0} X:{1} = {2}".format(horizontal_degree, vertical_degree, value))
            progressbar.refresh()


Export a reading
================

.. code-block:: python

    # EXTENDS THE `Create a minimal measurement` EXAMPLE
    # EXPORT TO A DIFFERENT FOLDER
    RESULT_FILEPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out/test.mag.pkl")
    if not os.path.exists(RESULT_FILEPATH):
        os.makedirs(RESULT_FILEPATH)
    # ADD SOME ADDITION META DATA
    reading_storage.set_additional_data('filepath', RESULT_FILEPATH)
    reading_storage.set_additional_data('description', 'a new nice reading')
    # FINALLY EXPORT
    reading.dump_to_file(RESULT_FILEPATH)


Import a reading
================
.. code-block:: python

    # EXTENDS THE `Export a reading` EXAMPLE
    RESULT_FILEPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out/test.mag.pkl")
    reading_imported = MRPReading.MRPReading(None)
    reading_imported.load_from_file(RESULT_FILEPATH)




MRPVisualization Examples
*************************

Visualization of a measurement
==============================

.. image:: _static/example_visualization.png
   :width: 600


.. code-block:: python

    # EXTENDS THE `Create a minimal measurement` EXAMPLE
    import MRPVisualization
    # HERE matplotlib is also used

    visu = MRPVisualization.MRPVisualization(reading)

    # 2D PLOT INTO A WINDOW
    visu.plot2d_top(None)
    visu.plot2d_side(None)

    # 3D PLOT TO FILE
    visu.plot3d(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plot3d_3d.png'))



MRPAnalysis Examples
*************************


Apply a calibration reading
===========================

The idea behind the calibration routine is to perform a measurement without a magnetic source being placed in the sample holder.
The ``reading_calibration`` is performed with the same settings for all subsequent measurements.
Afterwards the Function ``apply_calibration_data_inplace`` is called for each new reading.

.. note::
   Make sure that the sample size (``HORIZONTAL_RESOLUTION`` and ``VERTICAL_RESOLUTION``) for calibration and all further measurements match.

.. note::
   Attention: Make sure that the environment does not change and the device is not moved.


.. code-block:: python

    # reading_calibration => measurement without magnetic source => environment only
    # reading_A => reading with source placed
    MRPAnalysis.MRPAnalysis.apply_calibration_data_inplace(reading_calibration, reading_A)
    # THE CALIBRATION_READING IS APPLIED DIRECTLY TO READING_A
    reading_A.set_additional_data('calibrated', 1)
    reading.dump_to_file(RESULT_FILEPATH)



Merge two half sphere readings
==============================

.. image:: _static/merged_readings_example.png
   :width: 600

The current mechanical scanner can only scan one magnet side in one pass, so two scann passes are required to scan a full sphere.
The ``merge_two_half_sphere_measurements_to_full_sphere`` function combine two readings (top, bottom) into one.

.. note::
   Make sure that the sample size (``HORIZONTAL_RESOLUTION`` and ``VERTICAL_RESOLUTION``) for calibration and all further measurements match.

.. code-block:: python

    # IMPORT TWO EXISTING READINGS FROM FILE
    reading_top_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/114N2.mag.pkl")
    reading_bottom_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets/114S2.mag.pkl")
    # IMPORT TOP READING
    reading_top = MRPReading.MRPReading(None)
    reading_top.load_from_file(reading_top_filepath)
    # IMPORT BOTTOM READING
    reading_bottom = MRPReading.MRPReading(None)
    reading_bottom.load_from_file(reading_bottom_filepath)
    # FINALLY MERGE
    merged_reading = MRPAnalysis.MRPAnalysis.merge_two_half_sphere_measurements_to_full_sphere(reading_top, reading_bottom)


MISC Examples
*************

Export reading to numpy
=======================

For further and more advanced analysis the ``MRPReading`` class offers two functions in order to export the ``data`` member into a ``numpy.ndarray``.
The current implementation returns

.. code-block:: python

    # EXTENDS THE `Create a minimal measurement` EXAMPLE

    # POLAR COORDINATES
    # [[phi, theta, magnetic_value], ....]
    numpy_1d_array = reading.to_numpy_polar(_normalize=False)

    # CARTESIAN COORDINATES
    # [[x, y, z], ....]
    # THE  CONVERSION TO CARTESIAN IS A BIT SPECIAL
    # IT USES THE MAGNETIC_VALUE for the radius
    # SO THE VECTOR IS LONGER IF THE MAGNETIC VALUE IS STRONGER
    # THIS CONVERSION CAN BE USED WITH VECTOR CALCULATIONS LIKE FIND NEAREST POINT ....
    numpy_1d_array = reading.to_numpy_polar(_normalize=False)