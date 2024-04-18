Introduction
============

Motivation for ``MagneticReadoutProcessing``
********************************************

This library was created for the Low-Field MRI project and allows processing of data measured by magnetic field sensors.
The focus is on visualization, followed by the provision of simple interfaces to work with this data.

General structure
-----------------

.. image:: _static/MRP_COMPLETE_FLOW.png
   :width: 600

The picture above, illustrates the general idea of this library.
Each component provides for itself minimal functionality needed for a dataflow from sensor data qcquisition to analysis to export.

The user can implement additional functionalities in each stage to get the desired output.




Limitations
***********

The current state of the Python module is in alpha status.
It offers rudimentary functions:

- Only spherical scans are possible

- recording of raw data including metadata

- visualization of recorded raw data

- export/import

- conversion of data into ``numpy`` compatible formats