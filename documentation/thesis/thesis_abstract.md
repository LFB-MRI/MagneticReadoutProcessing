A large number of magnets are used in the construction of low-field MRI equipment on the basis of permanent magnets.
The magnetic properties of these magnets must be similar to a certain degree in order to achieve a homogeneous B0 field, which is necessary for many setups.

Due to the complex manufacturing process of neodymium magnets, the different properties, i.e. the direction of magnetisation, can deviate from each other.
This affects the homogeneity of the field.


A passive shimming process is typically used to adjust the field afterwards.
This is complex and time-consuming and requires manual corrections to the magnets used.
To avoid this process, magnets can be systematically measured in advance.
Data acquisition, storage and subsequent analysis play an important role in this methodology.


Several existing open source solutions implement individual parts, but do not provide a complete data processing pipeline from acquisition to analysis, and their data storage formats are not compatible with each other.


For this use case, the MagneticReadoutProcessing library has been created in this work.
It implements all important aspects of acquisition, storage and analysis, and each intermediate step can be customised by the user without having to create everything from scratch, thus encouraging exchange between different user groups.

Complete documentation, tutorials and tests enable users to use and adapt the framework as quickly as possible. 
The framework was used to characterise different magnets, which requires integrating magnetic field sensors.