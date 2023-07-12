Examples
========

Installation/Usage:
*******************
As the package has not been published on PyPi yet, it CANNOT be install using pip.

For now, the suggested method is to copy the ``MagneticReadoutProcessing`` folder into your Python project folder.
There are some other packages required which are listed in the ``requirements.txt``.
To install them use ``$ pip3 install -r requirements.txt`` command.



The other method is to use the ``setup.py`` to install ``MagneticReadoutProcessing`` as module:

.. code-block:: console

    $ git clone https://github.com/LFB-MRI/MagneticReadoutProcessing ./MagneticReadoutProcessing
    $ cd ./MagneticReadoutProcessing
    $ python ./setup.py install



Create a minimal measurement
****************************

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





Visualization of a measurement
******************************
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

Export a reading
****************
.. code-block:: python

    # EXTENDS THE `Create a minimal measurement` EXAMPLE
    # EXPORT TO A DIFFERENT FOLDER
    RESULT_FILEPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    if not os.path.exists(RESULT_FILEPATH):
        os.makedirs(RESULT_FILEPATH)
    # ADD SOME ADDITION META DATA
    reading_storage.set_additional_data('filepath', RESULT_FILEPATH)
    reading_storage.set_additional_data('description', 'a new nice reading')
    # FINALLY EXPORT
    reading.dump_to_file(RESULT_FILEPATH)

