# Introduction

In the following, the motivation for the development of this framework is listed.
The chapter provides a brief introduction into the problem domain, delineates the scope and boundaries of the present research, surveys the current state of the art in low-field (+mri) research and applications, articulates the research question driving this thesis and delineates the anticipated use cases and benefits that will be explored and analysed throughout the study.

## Background and Motivation

(+mri) stands as a cornerstone in clinical diagnostics, utilizing the principles of nuclear magnetic resonance (+nmr) to generate cross-sectional images of the body. This indispensable method plays a significant role in contemporary medicine and research, contributing significantly to saving lives. Despite its widespread use, traditional (+mri) systems often rely on large, heavy, and expensive magnets to achieve the necessary homogeneity of the magnetic field for accurate imaging. [@NK16]

Several types of magnets are applicated in different (+mri) systems. Regardless of the type, the primary objective is to create a homogeneous magnetic field within the (+mri). The higher the homogeneity, the more accurate the measurements. Homogeneity in composed (+mri) can be adapted using the shimming procedure which requires a lot of effort and is prone to errors. 
This uniform magnetic field aligns the molecules within the body or object, setting the stage for a second magnetic system to stimulate these molecules for spin-measurements.

\newpage

The challenge with conventional homogeneity systems lies in their substantial size, weight, and cost. Even when targeting smaller areas of the body, large devices are often necessary with a higher field-strength of at least 1.5 T. [@HH21]
In response to this, there is a growing interest in developing low-field (+mri) systems that utilize in many cases permanent magnets. Permanent magnets generate a steady yet relatively weak magnetic field.
These systems, while offering advantages in energy efficiency and reduced complexity, face a significant challenge related to the inherent variability in the strength of permanent magnets. Achieving homogeneity in the magnetic field is crucial for accurate imaging or comparative analyses.
Low-field systems facilitate the comparison of different field behaviours and the identification of all kinds of irritations. O'Reilly, Teeuwisse and de Gans [@OTW19] have already demonstrated low-cost and small-scale implementations with low-field (+mri) in 2021 calculating images of a head successfully. 

Permanent magnets, usually arranged in a circular *Halbach array* inside the (+mri), are commonly used in low-field systems. However, their drawback is the inherent variability in strength, complicating the achievement of a homogeneous field and requiring precise strength information for correct magnet ordering and (+mri) construction.

Completed (+mri) systems pose significant challenges for retrospective adjustments, particularly when individual magnets impact the overall homogeneity of the magnetic field. While deviations in homogeneity can be measured post-assembly, the intricate task of readjustment is considered.
It is less cost-intensive and less complicated to measure the magnets proactively, prior to the finalization of the (+mri) system. [@W14]

The focus of this thesis is to improve low-frequency (+mri) technology by examining the usability of magnetic field sensors for characterising permanent magnets used in these systems.
The variability in the strength of permanent magnets leads to significant difficulties in constructing an (+mri) magnet with the necessary precision for homogenous field generation.

To address this challenge, the thesis proposes the development of a comprehensive hardware and software framework.
The hardware system aims to selectively measure magnetic fields at various locations or fully around a permanent magnet using different sensors. Several existing open-source software solutions implement individual parts, but do not provide a complete data processing pipeline from acquisition to analysis, and their data storage formats are not compatible with each other. These projects and their incompatibilities are explained in detail in chapter \ref{user-interaction-points-example}.

The accompanying open source software for this work is not only designed to enable measurements with various sensors, but also to characterise permanent magnets, magnetic fields and the sensors themselves.

The sensor testing process involves three key test procedures for two digital sensors. Firstly, the background noise for both sensors is quantified by measuring with the sensors in a constant environment without any magnets. Secondly, the linearity of the magnetic fields is measured for all sensors to detect deviations from the estimated ideal magnetic curve.

This research initiative contributes to the improvement of low-frequency (+mri) systems by enhancing the accuracy of permanent magnet characterisation. The outcome of this thesis provides insights into the selection and evaluation of sensors for future low-field (+mri) research, ultimately contributing to advancements in medical imaging technologies.

### Low-Field MRI

For modern medical imaging high-field superconducting magnets dominate most (+mri) machines, providing in general a higher contrast. The substantial costs, space requirements and safety and installation considerations cause considerable challenges.

(+mri) relies on the presence of a robust magnetic field, and over time, there has been a continual push to enhance the strength of these magnetic fields. This strength is quantified in units of Tesla [T], commonly referred to as the *B0* field in medical contexts, while physicists use the term magnetic field induction. The (+snr) is proportional to the magnetic *B0* field; growing magnetic field leads automatically to higher (+snr). For high resolution images, the initial *B0* field aims to be a homogeneous as possible. 

Notably, the focus on high-field systems dominated discussions until around 1991 when the possibility of constructing (+mri) machines with lower magnetic field strengths came up. This marked a shift in exploring the potential advantages and applications of low-field (+mri) systems. [@NK16]

Low-field magnetic resonance imaging (low-field (+mri)) is a (+mri) technique that operates at a lower magnetic field strength compared to conventional high-field (+mri) scanners. Typically, the magnetic field in low-field (+mri)-systems measured between *0.1T* and *0.3T* compared to the usual *1.5T* to *3T* and above in high-field (+mri) scanners [@HH21].

This technology is used in medical imaging as well as in preclinical research. The main advantage of low-field (+mri)s is the improved contrasting of soft material. It also offers more cost-effective alternatives to high-field (+mri) systems [@HH21], cost reduction, a smaller device footprint, alleviated safety concerns and leading to diminished image resolution within clinically feasible scan durations. [@AFL23]

Low-field (+mri) systems are predominantly composed of permanent magnets. Through the connection of these permanent magnets, a consistent magnetic field of up to *0.35T* can be generated. However, this achievement comes at the cost of an average system weight of *14t*. Despite their cost-effectiveness in production and maintenance, permanent magnets show drawbacks such as high temperature dependencies. [@NK16]

In particular, the advantages of the small design, the fast and simple image acquisition and the low costs are advantages that will become increasingly important in the future. However, the use of permanent magnets and their structure is particularly important in such systems and needs to be analysed.

### Magnet System

%%Example_Halbach_ring_with_cutouts_for_eight_magnets.png%%

The positioning of permanent magnets holds a significant role in constructing an (+mri) and is influencing the homogeneity of the *B0* magnetic field. Halbach ring magnets [@H80] have become a common design for low field (+mri) and (+nmr) systems [@SB10].

This positioning has the ability to generate extremely homogeneous magnetic flux densities, produce virtually no stray fields and is particularly attractive for larger magnets as their design has the best flux-to-mass ratio [@WZC21].

A Halbach ring of this type is usually based on a ring with permanent magnets arranged in a circle.
Figure \ref{Example_Halbach_ring_with_cutouts_for_eight_magnets.png} shows an example (+cad) model of such a ring. 


In this generated model eight cubic *12x12x12mm* magnets are embedded to generate homogeneous magnetic flux densities of around *20mT*.
The homogeneity in this configuration depends, among other things, on the following main aspects:

* **Material**:
  The magnetic properties of a material influence the generated field strength.
  Various materials have different magnetic susceptibilities.

* **Magnetization**:
  The orientation of the magnetic moments in the material influences the field strength.
  A higher magnetization leads to a stronger field strength.
  
* **Temperature**:
  Temperature can influence the magnetic properties of a material.
  The magnetization of some materials decreases with increasing temperature.

* **Manufacturing process**:
  The manufacturing process can influence the magnetic properties of the material.
  This is dependent on the purity of the starting materials used and the processing methods.
  There may also be deviations in field strength if different magnets from different production batches are compared.

These aspects [@BC16] can also be applied to individual magnets. As a result, this also complicates the effect on the structure of a Halbach ring magnet.
If these are joined together to form a ring, positioning tolerances are also added.

Halbach magnetic arrays present a choice for mobile (+nmr) due to their ability to produce highly homogeneous and robust magnetic fields per unit of magnetic mass, coupled with minimal stray fields. The term *Halbach Array* (commonly known as *magic rings*) denotes a precise configuration of permanent magnets designed to amplify magnetic flux on one side while concurrently mitigating or eliminating it on the opposite side. [@BC16]

The Halbach magnetic array appears as an essential element for future Magnet characterisation. Based on this fact this thesis centres on assessing the sensors applicability, the Halbach magnetic array serves as a tool for later measurements, although its implementation and further discussion will not be the primary focus.

In order to compensate for inhomogeneities in a finished system, there are various so-called shimming procedures which further improve homogeneity after the system has been assembled. This procedure is explained in the following chapter.


### Shimming Procedure

The shimming process is an essential step in (+mri) to ensure homogeneous magnetic fields for precise imaging. Shimming corrects irregularities in the static magnetic field that can be caused by external influences or internal system errors. This process optimizes field homogeneity, which is essential for high-resolution and artifact-free images [@WAH21].

Optimal homogeneity is attained through intricate designs facilitating active shimming, a technique essential for achieving high-resolution spectroscopy. Beyond this, simpler combinations and adaptations of Halbach rings offer versatility, making them suitable for variable field magnets or magnets that can be effortlessly opened without applying force. [@BC16]

The sources for the shimming process can be passive and active based. 
In passive shimming, ferromagnetic metal materials are inserted into the inner magnetic bore. This is measured in particular with regard to homogeneity.  This process is complex and time-consuming and may have to be repeated several times. [@BPA22]
Active shimming, on the other hand, can use additional coils or existing gradient coils controlled by special circuitry. Also, software algorithms can be used to adjust the control parameters of the (+mri) system and improve homogeneity [@WAH21].

In this theis, reference is made exclusively to the passive shimming process, as this project is to be used in the future to construct a low-field magnet (+mri) from permanent magnets and to try to simplify the passive shimming process by means of various software optimizations.

## State of the Art 

**Low-Field MRI**

According to Wolfgang R. Nitz in 2016, just *13.4%* of actively used (+mri) systems are low-field (+mri) (*66.6% 1.5T systems, 20% 3.0T system, 14.4% low field with <0.5T*). [@NK16]

Within the research domain, various implementations have emerged. An exemplar instance is the work by O'Reilly, Teeuwisse, and Webb, who introduced a groundbreaking three-dimensional (+mri) in a homogeneous *27cm* diameter Bore Halbach Array magnet [@OTW19] in 2019.This innovative setup is subsequently employed in 2020 to acquire in vivo MR images, showcasing the practical applications of their pioneering research [@OTW21]. In 2023, de Vos, Remis and Webb published a summary of the design of a point-of-care Halbach array low-field (+mri) system [@DRW23].

The Halbach magnet incorporated in this system boasts a *27cm* diameter, a *B0* field strength of *50.4 mT*, and an impressive homogeneity of *2400 (+ppm)* over a *20cm* diameter using smaller magnets ($12 x 12 x 12 mm^3$). [@OTW19]

To further refine the magnets homogeneity, optimisation techniques are employed by adjusting the radius of the Halbach ring along the length of the magnet. The deliberate choice of smaller magnets, as opposed to other Halbach designs, serves to compensate for inherent manufacturing imperfections in each individual magnet. This strategic decision not only mitigates structural demands on the magnet housing in terms of strength and weight but also augments safety throughout the construction process.

**Magnet Characterisation**

The shimming process mentioned describes how, after the field magnet has been set up, if the homogeneous magnetic flux densities are not sufficient, these can be adjusted manually by means of adjustments to the setup or, if the hardware allows it, by software.
In addition, the causes that cause the inhomogeneity, the output permanent magnet, are also known.
As a result, there is the possibility of using the shimming process or checking the permanent magnets used in advance before they are used in a Halbach configuration.
In order to measure the magnets individually, there are already implementations that use different measurement methods to determine the field strength of individual magnets and individual measuring points are recorded. [@WZC21]

There are two ways of using the data from the magnets that are previously measured:

* By using binning or sorting algorithms to filter for the most similar magnets
* Adjustment of the rotation and position within the Halbach configuration

This form of data processing of previously characterised magnetic data is currently being implemented experimentally in projects using various algorithms [@WZC21].
Standard sorting algorithms are used as well as specialized algorithms for optimizing homogeneity by rotating the individual magnets in a Halbach ring relative to each other [@MWO24].

These are each separate projects that implement individual aspects of data processing, which realize the process of measuring individual magnets by manual combination.
However, there are still compatibility problems and limitations in the adaptation of hardware and software.

Special algorithms from various, public projects are used to optimize homogeneity, like a genetic algorithm which O'Reilly implemented [@O24]. Therefore, the challenge is to ensure the seamless integration and compatibility of these algorithms into the overall process.
This should make it possible to create a workflow from the individual magnet to the finished optimized (+cad) model of a Halbach ring. In addition, it is possible to find a selection of suitable magnets whose magnetic field is as identical as possible

## Aim of this Thesis

The present work aims to provide an efficient and comprehensive solution for the design of low-field (+mri) devices by developing and implementing a software and hardware framework.

Within the framework of the *DeLoRI* (Dedicated Low-field (+mri) for breast) project, *Fraunhofer MEVIS* in Bremen is actively engaged in crafting a compact and mobile low-field (+mri) unit customised specifically for screening purposes. As described before, since 1991 low-field (+mri)s have evolved into a growing realm of research, showcasing significant opportunities within the field of medical technology. The efforts by *Fraunhofer MEVIS* exemplifies the ongoing commitment to utilizing the potential of low-field (+mri) for enhanced breast screening applications.

The focus of the ongoing efforts is to improve the homogeneity of magnets within low-field (+mri) systems below *1000 (+ppm)*, primarily driven by the goal of establishing a compact low-field (+mri) for breast cancer detection. This value was defined as a rough target value for the homogeneity of the experimental test magnet to be set up for the project, as a result of which the performance can be compared with existing approaches for such magnets. [@HPB04]

Beyond the development and prototype construction of low-field (+mri) scanners, the project encompasses electromagnetic simulation of components within the low-field (+mri) system, coupled with machine learning-driven control and data acquisition. The resultant software will be instrumental in reconstruction, with a specific focus on leveraging (+ai)-based methodologies.

This comprehensive effort is designed to support the prototyping phase of the low-field (+mri). Diverging from the approach implemented by O'Reilly, Teeuwisse, and Webb, *DeLoRI* aims to design an open (+mri), departing from the circular (+mri) configuration discussed in the publication. This innovation is geared towards streamlining breast examinations, offering enhanced accessibility, and minimizing the spatial requirements during installation. 

In addition, *DeLoRI* efforts to achieve heightened accuracy, striving for precision levels below *1000 (+ppm)*. While O'Reilly, Teeuwisse, and Webb were able to modify the ring diameter to influence field homogeneity, the unique goal at this point is to characterize the magnets pre-installation, allowing for proactive assessments of homogeneity characteristics. This approach aims to provide insights into magnetic field uniformity before the magnets are integrated, thereby streamlining the optimisation process. Furthermore, it is important to note that the primary objective of this thesis is not merely to characterize the magnet itself; rather, the emphasis lies in the selection and comparison of potential sensors for the characterisation process.
To achieve this, a versatile hardware setup is in development, designed to accommodate various sensors for the measurement of magnets or other objects. Simultaneously, a software interface is being crafted to universally read data from different sensors and interact seamlessly with the diverse firmware associated with various Halbach sensors. A key feature of this system is the ease of sensor interchangeability, facilitating adaptability and versatility in the characterisation process.

The scope of the software library is to lay the foundation for the systematic characterisation of magnets based on permanent magnets.
The library will enable data acquisition, storage and analysis of magnetic properties, with customisation possible at each step of the process. Complete documentation, tutorials and tests will enable users to use the framework efficiently and adapt it to their specific requirements.
The characterisation of field sensors in consumer quality serves the practical application and validation of the developed solution.

A practical application of the framework is shown, which demonstrates the characterization of two magnetic field sensors. For this use case, two sensors were selected to be included in the study.
The aim is to use the framework to verify whether the selected sensors meet the strict criteria for an accuracy of *1000 (+ppm)*. It is also to check whether the measuring range of these sensors corresponds to the required field strength and whether they are suitable for the intended application.

## Research Question and Approach

Concerning the *DeLoRI* project, this study exclusively delves into the realm of permanent magnets employed for creating a homogeneous *B0* field through Halbach rings. Other systems for measurements are deliberately excluded from consideration but will be necessary in later stages of the *DeLoRI* project. 

Before naming the research focus, it is important to understand the difference and connection between deviation and resolution of the system. 
To measure a deviation of better than *1000 (+ppm)* in a *50mT* magnetic field, a resolution that is less than *1000 (+ppm)* of *50mT* is needed.

  \noteworthy{\frac{1000}{1000000} \times 50 \, mT = 0.05 \, mT \times 1000 = 50 \, \mu T}{: 1000ppm from 50mT needed resolution calucation I}

This means that to measure a deviation of better than *1000 (+ppm)* in a $50mT$ magnetic field, a resolution of less than *50* $\mu$T is needed.

The primary objectives of this work revolve around addressing two pivotal research questions:

* **Sensor characterisation**: Can the carefully selected sensors effectively measure a magnet? Specifically, this involves investigating the saturation of the sensors, the linearity of field strength concerning distance from the sensor, and, in a subsequent phase, exploring temperature dependence.

* **Homogeneity Measurement**: Can the chosen sensors be adeptly utilized to measure the homogeneity of a Halbach ring-based B0 field within the stringent limit of less than *1000 (+ppm)*? The desired outcome is a measurement of less than *50* $\mu$T at *1000 (+ppm)*, with a specific focus on determining the sensors viability for noise measurements.

It is essential to emphasize that the intention is not to characterize the magnets; the sensors which might be used for characterisation are be analysed and evaluated.

This work prioritises the development of both hardware and software customised for sensor utilization and final testing. Physical properties and considerations take a secondary role in comparison to the overarching goal of refining the sensor-based methodologies.

## Use cases

The following chapter defines desirable use cases that the future project need to cover. These use cases define the setup of the hard- and software. 
These illustrate practical situations to understand the functionality and added value of the implemented solution for the user.

The use cases are defined during project planning and provide an overview of how the user interacts with the project and what functionalities can be expected.

In the later accomplished evaluation process in chapter \ref{use-case-evaluation}, the defined use cases are also used as a reference to demonstrate the implemented capabilities of the solution.

This is important in order to understand the needs of the target group and design the result accordingly. For this purpose, these are defined into the following blocks:

1. **Ready to use hardware sensor designs**

  A universal, easy-to-integrate Hall sensor design allows users to evaluate the framework quickly and cost-effectively.
  The pre-built hardware sensors provide an optimal solution for research, reducing development time and achieving repeatable measurement results.
  Once successfully evaluated, the Hall sensor design should be easily adaptable to other sensors without the need for major firmware changes.

2. **Taking automatic measurements from sensors**

  The purpose of the framework is to enable the automated acquisition of measurement data from various connected hardware sensors.
  The user should be able to configure various measurement series, which should then be carried out by the framework without further user interaction.

3. **Open storage formats for data export**

  The use of open storage formats for the export of data enables an interoperable data exchange environment.
  The implementation of standardized formats improves the portability and long-term availability of data.
  This encourages the exchange and further processing of measurement data in other software tools.

4. **Ready to integrate data analysis functions**

  Once it is possible to record and store measured values, it should be possible for the user to analyse and visualize this data using various algorithms.
  The focus at this point should be on extending the framework with user-created algorithms.


5. **User-programmable data processing pipelines**

  User-programmable data processing pipelines enable the flexible design of data processing sequences as pipeline by users.
  The framework should enable users to create their own pipelines with the previously defined data analysis functions.


## Structure

This work is divided into six main chapters, which deal with the approach, implementation and evaluation. The techniques and concepts used are explained in detail. Specific examples provide an overview of the possible use of the developed solution by the user.

Chapter \ref{unified-sensor}. **Unified Sensor**
  refers to the integration of different sensors into a standardised solution.
  This enables simple data acquisition and serves as a basic hardware system on which the subsequent data processing library can be applied.

Chapter \ref{software-readout-framework}. **Software Readout Framework**
  describes the implementation of the data readout framework.
  This includes an explanation of the various modules and specific application examples.

Chapter \ref{usability-improvements}. **Usability Improvements**
  refers to additional activities to improve user-friendliness.
  This includes the optimisation of interfaces, interactions and processes to ensure intuitive and efficient use of the product.
  This also includes the documentation of code and the distribution of the source code as a package to users.

Chapter \ref{use-case-evaluation}. **Use Case Evaluation**
  describes the application of the framework to the previously defined use cases and thus forms the basis for later evaluation.

Chapter \ref{evaluation}. **Evaluation**
  outlines the evaluation process for permanent magnets using the developed framework. The research questions posed regarding the suitability of the sensors used for the characterisation of permanent magnets are examined.

Chapter \ref{conclusion-and-discussion}. **Conclusion and Discussion**
  bringing together essential research components, it synthesizes study outcomes, discusses implications, and provides insights for future work. This chapter ensures closure and aids readers in grasping the broader context and significance of the research.

A comprehensive hardware and software framework needs to be established, which can measure diverse objects using various sensors. In addition, comments must be made on the suitability of the sensors used for magnetic field measurements.

# Unified Sensor

A defined main objective of this project is the development of a cost-effective magnetic field sensors interface that is universally expandable as well.
The focus is on mapping different sensors and being compatible with different magnet types and shapes. This ensures a wide range of applications in different scenarios.

Another goal is reproducibility to ensure uniform results, which as a result reduces the susceptibility to errors. Easy communication with standard (+pc) hardware, which offers a variety of common interface options, maximizes the user-friendliness.

The flexibility to support different sensors and magnets makes the system versatile and opens the possibility for use in different applications.
A low-cost magnetic field sensors interface will therefore not only be economically attractive, but also facilitate the integration of magnetic field sensors in different contexts like for compasses or other devices.

In addition, the low-cost sensor interface will serve as a development platform for the data evaluation (+mrp) library and provide real measurement data from magnets.
Further, the interface firmware creates a basis for the development of a data protocol for exchanging measured values.

It simplifies of own measuring devices into the (+mrp) ecosystem later. This is only applicable with a minimal functional hardware and firmware setup; it is developed for this purpose in the first step.

\newpage

## Sensor Selection

The selection process for possible magnetic field sensors initially focuses on the most common and cost-effective hall effect ones, especially those that are already used in smartphones and are therefore widely available to consumers.

%%Typical_block_diagram_of_a_digital_hall_sensor_sensing_chain_using_three_hall_plates.png%%

A Hall effect sensor utilises the Hall effect that occurs when current flows in a conductor that is exposed to a magnetic field. The sensor consists of a semiconductor material such as gallium arsenide or indium antimonide. Inside the sensor are Hall effect plates, which essentially consist of a thin layer of this semiconductor material. [@BJJ16]

Figure \ref{Typical_block_diagram_of_a_digital_hall_sensor_sensing_chain_using_three_hall_plates.png} shows the internal structure of a digital Hall effect sensor as a block diagram. The Hall effect takes place in the Hall plates. These are orientated differently depending on the axis inside the (+ic)s. In this case, it is a three-axis hall effect sensor. The output voltage generated by the Hall plates is then digitised by a (+adc). The values can then be read out via a digital interface.

A key aspect of this selection is the preference for sensors with digital interfaces to facilitate implementation in the circuit layout since these kinds of sensors are easy to integrate compared to non-digital sensors, which require specific frameworks.
The integration of integrated temperature sensors represents a significant enhancement that will later enable precise temperature compensation.

Focussing on the digital (+i2c) interface not only facilitates implementation, but also contributes to overall cost efficiency.
At the same time, the integration of temperature sensors enables precise measurements under varying environmental conditions.
This strategic choice forms the basis for a flexible, universally applicable Hall sensor interface that can be seamlessly integrated into various existing systems.

%%List_of_in_unified_firmware_implemented_digital_magnetic_field_sensors_with_focus_on_different_sensor_capabilities.csv%%

The use of analogue sensors is purposefully avoided, though they are suitable for more precise measurements and extended measuring ranges.
They are excluded because they require more carefully designed circuits and more complicated energy management. In the context of the desired goal of developing a cost-efficient and universally expandable Hall sensor interface, the decision in favour of digital sensors seems appropriate.

Another point that contributed to the selection of this module is the availability of the sensor (+ic)s as a ready-made and readily available evaluation module. This ensured that the electrical design is verified by the manufacturer so that the sensor could be operated with the correct electrical parameters. On the other hand, it is possible to analyse several sensors in a shorter time, so that no separate (+pcb) has to be designed and manufactured.

Table \ref{List_of_in_unified_firmware_implemented_digital_magnetic_field_sensors_with_focus_on_different_sensor_capabilities.csv} shows a selection of sensors for which hardware and software support has been implemented.
The resolution of the selected sensors covers the expected range of values required by the various magnets to be tested.

In the *Evaluation* in chapter \ref{evaluation} basic characterisation methods are used to evaluate the sensors listed in Table \ref{List_of_in_unified_firmware_implemented_digital_magnetic_field_sensors_with_focus_on_different_sensor_capabilities.csv} regarding their sensitivity and other parameters. This is done at this point, as the components of the readout interface that enable interaction with the sensors are considered first.


## Mechanical Structure

The mechanical design of a sensor is kept as simple as possible so that it can be replicated as easily as possible.
The focus is on providing a stable foundation for the sensor (+ic) and an exchangeable holder for different magnets.

%%Rendered_mechanical_structure_of_the_1D_sensor_(+cad)_model_with_different_parts_colored_separately,_and_universal_magnet_mount_shown_in_green.png%%

Figure \ref{Rendered_mechanical_structure_of_the_1D_sensor_(+cad)_model_with_different_parts_colored_separately,_and_universal_magnet_mount_shown_in_green.png}, shows rendered view of the 1D-Single sensor (+cad) drawing, which is described in chapter \ref{d-single-sensor}. All parts are produced using 3D printing additive manufacturing process. The sensor circuit board is glued underneath the magnet holder. This is interchangeable, so different distances between sensor and magnet can be realised. The exchangeable magnetic holder (shown in green in Figure \ref{Rendered_mechanical_structure_of_the_1D_sensor_(+cad)_model_with_different_parts_colored_separately,_and_universal_magnet_mount_shown_in_green.png}) can be adapted to different magnets. It can be produced quickly due to the small number of parts used.
The two recesses lock the magnet holder with the inserted magnet over the sensor.
The mechanical design created is able to accommodate cylinders, cubes, up to a maximum length of *30mm*.
Other magnet shapes require a modification of the base plate and the sensor holder.
The specified tolerances of *0.45mm* allow the magnet to be inserted into the 3D printed holder with repeat accuracy and without backlash. This was accomplished with the help of tolerance tests for the 3D printing material (+pla) and the used *Voron 2.4 350mm* 3D printer through several series of tests.
This is important if several magnets must be measured, where the positioning over the sensor must always be the same.


## Electrical Interface

%%1D_sensor_schematic_using_an_Raspberry_Pi_Pico_with_a_TLV493D_footprint_in_the_center.png%%

The electronics consist of the magnetic field sensor and the electrical interface to connect it to a (+pc) in the form of a microcontroller. The focus is on utilising existing microcontroller development and evaluation boards, which already integrate all the components required for basic operation. This not only enabled a time-saving implementation, but also ensured a cost-efficient realisation. A *Raspberry Pi Pico* and a *STM32F4* are used as a computer-sensor interface for this thesis, which are popular, cost-effective and simple to implement.

All the necessary components and their circuitry are recorded on a (+pcb) shown in Figure \ref{1D_sensor_schematic_using_an_Raspberry_Pi_Pico_with_a_TLV493D_footprint_in_the_center.png} and subsequently manufactured.
In addition, footprints are provided for various sensor (+ic) packages.
By placing mounting holes on the (+pcb), it is possible to attach various mechanical mounts on top of the sensor (+ic)s. These holes are necessary for later adaptions and sensor changes, such as different magnet holders or measurement equipment (e.g. for additional temperature sensors).

Special attention is paid to the provision of an accessible SYNC-(+gpio) connector.
This enables subsequent multi-sensor synchronization and offers options for later sensor-extensions. 
This functionality opens the possibility of synchronising data from different sensors to achieve precise and coherent measurement results.
Overall, this integrated approach represents an effective solution for the flexible evaluation of sensors and helps to optimise the development process.

## Firmware

%%Unified_sensor_firmware_program_structure_with_listed_setup_and_main_loop_routines_using_simplified_function_blocks.png%%

The microcontroller firmware is software that is executed on a microcontroller in an embedded system. 
It controls the hardware and enables the execution of predefined functions. The firmware is used to process input data, control output devices and performs specific tasks according to the program code. It manages communication with sensors, actuators and other peripheral devices, processing data and making decisions.
Firmware is critical to the functioning of devices. The firmware is responsible for detecting the possible connected sensors shown in Table \ref{List_of_in_unified_firmware_implemented_digital_magnetic_field_sensors_with_focus_on_different_sensor_capabilities.csv} and query measurements.
This measured data can be forwarded to a host (+pc) via a user interface and can then be further processed there.

A key component is that as many common sensors as possible can be easily connected without having to adapt the firmware. This modularity is implemented using abstract class design.
These are initiated according to the sensors found at startup. If new hardware needs to be integrated, only the required functions in Listing \ref{lst:CustomSensorClass} need to be implemented.

```cpp {#lst:CustomSensorClass caption="CustomSensor-Class for adding new sensor hardware support into the unified sensor firmware package."}
#ifndef __CustomSensor_h__
#define __CustomSensor_h__
// register custom sensor in implemented_sensors.h also
class CustomSensor: public baseSensor
{
public:
  CustomSensor();
  ~CustomSensor();
  // implement depending on sensor communication interface
  bool begin(TwoWire& _wire_instance); // I2C
  bool begin(HardwareSerial& _serial_instance); // UART
  bool begin(Pin& _pin_instance); // ANALOG or DIGITAL PIN like one wire
  // FUNCTIONS USED BY READOUT LOGIC
  bool is_valid() override;
  String capabilities() override;
  String get_sensor_name() override;
  bool query_sensor() override;
  sensor_result get_result() override;
};
#endif
```

Figure \ref{Unified_sensor_firmware_program_structure_with_listed_setup_and_main_loop_routines_using_simplified_function_blocks.png} shows a flow chart of the start process after powering on the sensor and the subsequent main loop for processing the user commands and sensor results.
When the microcontroller is started, the software checks whether known sensors are connected to (+i2c) or (+uart) interfaces.

If any are found (using a dedicated (+lut) with sensor address translation information), the appropriate class instances are created and these can later be used to read out measurement results.

The next initialisation system is dedicated for multi-sensor synchronisation described in chapter \ref{sensor-synchronisation-interface}. The last step in the setup is to configure communication with the host or connected (+pc).
All implemented microcontroller platforms used (*Raspberry Pi Pico*, *STM32F4*) have a (+usb) slave port.

The used usb descriptor is a (+usb)-(+cdc). This is used to emulate a virtual *RS232* communication port using a (+usb) port on a (+pc) and usually no additional driver is needed on modern host systems.

After execution of the setup routine is completed, the system switches to an infinite loop, which processes several actions. One task is, to react to user commands which can be sent to the system by the user via the integrated (+cli).
All sensors are read out via a timer interval set in the setup procedure and their values are stored in a ring buffer.
Ring buffer offers efficient data management in limited memory.
Its cyclic structure enables continuous overwriting of older data, saves memory space and facilitates seamless processing of real-time data.

Ring buffers are well suited for applications with variable data rates and minimise the need for complex memory management.
The buffer can be read out by command and the result of the measurement is sent to the host.
Each sensor measurement result is transmitted from the buffer to the host together with a time stamp and a sequential number.

This ensures that in a multi-sensor setup with several sensors are synchronized in time like described in chapter \ref{sensor-synchronisation-interface} and are not out of sequence or drift.

### Communication Interface

Each sensor that is loaded with the firmware, registers on to the host (+pc) as a serial interface. There are several ways for the user to interact with the sensor:

* (+mrp)-library, is introduced in chapter \ref{software-readout-framework}
* Stand-alone mode via sending commands using built-in (+cli)

The (+cli) mode is a simple text-based interface with which it is possible to read out current measured values, obtain debug information and set operating parameters.
This allows to quickly inspect whether the hardware is working properly after firmware installation.
The command *help*, displays a detailed command reference with all available commands as shown in Figure \ref{Unified_sensor_firmware_provided_serial_terminal_based_(+cli)_allows_the_user_to_configure_the_sensor_manually.png} to the user.

%%Unified_sensor_firmware_provided_serial_terminal_based_(+cli)_allows_the_user_to_configure_the_sensor_manually.png%%

Figure \ref{Result_of_an_executed_b_value_measurement_readout_command_using_the_sensors_(+cli)_with_immediate_user_readable_response.png} shows the current measured value queried by using the *readout* command by the user. 

The other option is to use the (+mrp)-library explained in chapter \ref{software-readout-framework}. The serial interface is also used at this point. However, after a connection attempt by the (+hal) module (explained in chapter \ref{mrphal}) of the (+mrp)-library (explained in chapter \ref{software-readout-framework}), the system switches to binary mode, which is initiated using the *sbm* command. The command is only sent by the library, not by the user.
The same commands are available to (+mrp)-library as for user (+cli)-based communication, but in a binary format.

%%Result_of_an_executed_b_value_measurement_readout_command_using_the_sensors_(+cli)_with_immediate_user_readable_response.png%%

### Sensor Synchronisation Interface

%%Multi_sensor_synchronisation_wiring_example_using_three_sensors_together_with_one_host_(+pc)_performing_the_triggering_and_readout_processing.png%%

One problem with the use of several sensors on one readout host (+pc) is that the measurements may drift over time. On the one hand, (+usb) latencies can occur.
This can occur due to numerous factors, including device drivers, data transfer speed and system resources.
High-quality (+usb) devices and modern drivers often minimise latencies. [@WSB19]
Nevertheless, complex data processing tasks and overloaded (+usb) ports can lead to delays.

%%(+usb)_connected_sensor_latency_test_results_using_several_sensor_readout_requests_togehter_with_variable_host_system_cpu_loads_testing_for_jitter_variations.csv%%

\newpage

Table \ref{(+usb)_connected_sensor_latency_test_results_using_several_sensor_readout_requests_togehter_with_variable_host_system_cpu_loads_testing_for_jitter_variations.csv} contains various jitter measurements. These are performed on a *Raspberry Pi 4 4GB*-(+sbc) together with an *1D: Single Sensor* explained in chapter \ref{d-single-sensor} and the following software settings:

* *Raspberry Pi OS Lite* - (+os)
* (+mrp)-library described in chapter \ref{software-readout-framework} - Version *1.4.1*
* Unified Sensor-firmware described in chapter \ref{unified-sensor} - Version *1.0.1*

A jitter time of up to an additional *1ms* is added between the triggering of the measurements by the host system and the receipt of the command by the sensor hardware.
If the host system is still under load, this value increases many times over. This means that synchronising several sensors via the (+usb) connection alone is not sufficient. 
The other issue is sending the trigger signal from the readout software, which is described in chapter \ref{software-readout-framework}. At this point unpredictable latencies can occur, too, depending on which other tasks are also executed on this port.
To enable the most stable possible synchronisation between several sensors, an option has already been created to establish an electrical connection between sensors.
This is used together with the firmware to synchronise the readout intervals.
Figure \ref{Multi_sensor_synchronisation_wiring_example_using_three_sensors_together_with_one_host_(+pc)_performing_the_triggering_and_readout_processing.png} illustrates the schematic how several sensors must be wired together to implement this form of synchronisation.

%%Unified_sensor_firmware_multi_sensor_synchronisation_procedure_using_sync_(+gpio)_input_for_operation_(primary_or_secondary)_mode_decision.png%%

Once the hardware has been prepared, the task of the firmware of each of the chained sensors is to find a common synchronisation clock.
Figure \ref{Unified_sensor_firmware_multi_sensor_synchronisation_procedure_using_sync_(+gpio)_input_for_operation_(primary_or_secondary)_mode_decision.png} illustrates how the firmware handles the decision task if the sensor is *primary* or *secondary* at startup.
The internal firmware-function *register irq on sync pin* is overwritten. To set one *primary* and several *secondary* sensors, each sensor waits for an initial pulse on the SYNC-(+gpio), which is a pin at the microcontroller with the functionality to detect if the sensor is a primary or a secondary sensor.
A random timer is started beforehand by each sensor, which sends a pulse on the sync line. All others receive this and switch to *secondary mode* and synchronise the measurements based on each sync pulse received.

Since the presumed *primary* sensor cannot register its own sync pulse (because the pin is switched to output), there is a timeout branch condition *got pulse within 1000ms* and this becomes the *primary* sensor.
This means that in a chain of sensors there is exactly one *primary* and many *secondary* sensors.

In single-sensor operation, this automatically jumps to *primary* sensor operation through the *got impulse within 1000ms* branch result.
Figure \ref{Result_of_the_opmode_command_execution_on_a_sensor_which_is_connected_to_another_as_primary_configured_sensor.png} shows the synchronisation status of the sensor which can be queried via the user interface described in chapter \ref{communication-interface} by using the *opmode* command.
An important aspect of the implementation is that there is no numbering or sequence of the individual sensors.
This means that for the subsequent readout of the measurements, it is only important that they are taken at the same interval across all sensors.
The sensor differentiation takes place later in the (+mrp)-library \ref{software-readout-framework} by using the sensor (+uuid).

%%Result_of_the_opmode_command_execution_on_a_sensor_which_is_connected_to_another_as_primary_configured_sensor.png%%

## Example Sensors

Two functional sensor platforms are built in order to create a solid test platform for later tests and for the development of the (+mrp)-library \ref{software-readout-framework} with the previously developed sensor concepts.

%%Build_hardware_sensors_equipped_with_different_sensor_(+ic)s_to_cover_various_magnet_charaterisation_setups.csv%%

Table \ref{Build_hardware_sensors_equipped_with_different_sensor_(+ic)s_to_cover_various_magnet_charaterisation_setups.csv} shows the various prototype sensor platforms equipped with different magnetic field sensors.
These cover all the required functions described in the use cases \ref{use-cases}. The most significant difference, apart from the sensor used, is the *scan mode*.
In this context, this describes whether the sensor can measure a *static* fixed point on the magnet or if the sensor can move *dynamically* around the magnet using a controllable manipulator.

In the following, the hardware structure of a *static* and *dynamic* sensor is described. For the *static* sensor, only the *1D* variant is shown, as this does not differ significantly from the structure of the *1D: dual sensor*, except it uses two *TLV493D* sensors, mounted above and on top of the magnet.

### 1D: Single Sensor

%%Manufactured_1D_sensor_construction_from_different_angles_and_universal_magnet_mount_(green_3D_printed_part)_equipped_with_N45_12x12x12mm_magnet.png%%


The 1D sensor shown in Figure \ref{Manufactured_1D_sensor_construction_from_different_angles_and_universal_magnet_mount_(green_3D_printed_part)_equipped_with_N45_12x12x12mm_magnet.png} is the simplest possible sensor that is compatible with the Unified Sensor firmware.

The electrical level is based on a *Raspberry Pi Pico* together with the *MMC5603NJ* magnetic sensor.
The mechanical setup consists of four 3D printed components, which are fixed together with nylon screws to minimise influences on the measurement.

Since the *MMC5603NJ* only has limited measurement range of total *6mT*, even small coin sized neodymium magnets already saturates the sensor.
It is possible to mount 3D printed spacers (see green part in Figure \ref{Manufactured_1D_sensor_construction_from_different_angles_and_universal_magnet_mount_(green_3D_printed_part)_equipped_with_N45_12x12x12mm_magnet.png})over the sensor to increase the distance between the magnet and the sensor and thus also measure these magnets.

The designed magnet holder can be adapted for different magnet shapes and can be placed on the spacer without backlash to be able to perform a repeatable measurement without introducing measurement irregularities by mechanically changing the magnet.


### 3D: Full Sphere

%%Full_sphere_sensor_implementation_using_two_Nema17_stepper_motors_in_a_polar_coordinate_system.png%%

The 3D full sphere sensor shown in Figure \ref{Full_sphere_sensor_implementation_using_two_Nema17_stepper_motors_in_a_polar_coordinate_system.png} offers the possibility to create a 3D map of the inserted magnet.

Figure \ref{3D_plot_of_an_N45_12x12x12mm_magnet_using_the_build_3D_full_sphere_sensor_with_visible_magnetic_field_strength_deviations_using_different_shaded_vertices_on_a_sphere.png} shows the visualisation of such a scan in the form of a spherical 3D map. On the sphere is the magnetic field strength, which is detected by the sensor at the position. The transition from a fully positive field strength (red) to a negative field strength (blue) is clearly recognisable and corresponds to the orientation of the magnet in the holder. The magnet sensor is mounted on a movable arm, which can move *180* degrees around the magnet on one axis. To be able to map the full sphere, the magnet is mounted on a turntable. This permits the manipulator to move a polar coordinate system.

%%3D_plot_of_an_N45_12x12x12mm_magnet_using_the_build_3D_full_sphere_sensor_with_visible_magnetic_field_strength_deviations_using_different_shaded_vertices_on_a_sphere.png%%

As the magnets in the motors, as with the screws used in the 1D sensor, can influence the measurements of the magnetic field sensor, the distance between these and the sensor and magnet is increased by using nylon and 3D printed spacer. The turntable and its drive motor are connected to each other via a belt.

On the electrical side, consists of a *SKR-Pico* stepper motor controller on the one hand side and a *TLV493D* magnetic field sensor on the other hand side.
This is chosen because of its larger measuring range and can therefore be used more universally without having to change the sensor of the arm.

### Integration of an Industry-Teslameter

As the sensors shown so far relate exclusively to self-built, low-cost hardware, the following chapter shows how existing hardware can be integrated into the system.
A temperature-compensated *Voltcraft GM-70* telsameter shown in Figure \ref{Voltcraft_GM70_teslameter_with_custom_(+pc)_interface_board_using_a_(+usb)_to_serial_converter_and_needed_additional_pull-up_resistors.png} is used, which has a measuring range of *0T* to *3T* with a resolution of *0.1mT*.
It offers an *RS232* interface with a documented protocol for connection to a (+pc). This connectivity makes it possible to make the device compatible with the previously build unified sensor firmware using a separate \href{https://github.com/RBEGamer/VoltcraftGM70Rest}{VoltcraftGM70Rest interface software} executable on the host (+pc).

Another option is a custom interface board between the meter and the PC. This is a good option as many modern (+pc)s or (+sbc)s no longer offer a physical *RS232* interface.
As with the other sensors, this interface consists of a *Raspberry Pi Pico* with an additional level shifter.
The teslameter is connected to the microcontroller using two free (+gpio)s in (+uart) mode.
The firmware is adapted using a separate build configuration.

In order to be able to read and correctly interpret the data from the microcontroller, the serial protocol of the sensor is implemented in a customised version of the *CustomSensor* class as shown in Listing \ref{lst:CustomSensorClass}. 
This software or hardware integration can be conducted on any other measuring device with a suitable communication interface and a known protocol thanks to the modular design.

%%Voltcraft_GM70_teslameter_with_custom_(+pc)_interface_board_using_a_(+usb)_to_serial_converter_and_needed_additional_pull-up_resistors.png%%


# Software Readout Framework

The software readout framework is the central software component that is developed as part of this work.
This software framework is intended to provide a user-oriented data acquisition and analysis environment.
For this purpose, typical individual steps that occur in relation to these tasks are implemented:

* Data acquisition - from hardware sensors or other data sources - see chapter \ref{unified-sensor} 
* Storage - export of data in various open formats - see chapter \ref{storage-and-datamanagement}
* Analysis - algorithms to analyse different data sets - see chapter \ref{analysis}

All these steps are divided into different blocks with an additional functionality for users to add own modules.
This concept is explained in the following chapter.

## User Interaction Points

User interaction points represent one core concept of the developed library and are intended to provide user-friendliness on the one hand and the rapid development of own analysis and optimisation algorithms on the other. For this thesis it also eases the option to change sensors for measurements. 

For this purpose, the library is divided into individual modules, which are shown in Figure \ref{A_high_level_overview_of_all_MRP_library_implemented_Python_modules_which_can_be_changed_by_the_user.png}.
In combination, these represent a typical measurement-analysis-evaluation workflow of data.
For this purpose, a module system with standardised functional patterns and data types is developed and packed together in an extendable Python library.

\newpage

According to this concept, the user should be able to replace individual components from this chain with own modules without having to worry about implementing other of these to make the project work.

%%A_high_level_overview_of_all_MRP_library_implemented_Python_modules_which_can_be_changed_by_the_user.png%%

### User Interaction Points Example

The following example shows the advantages of using *user interaction points*. In the following, two different projects are shown, which are based on each other in terms of their functions for analysing and optimising magnetic fields, but they are not compatible with each other due to the different data formats and programming paradigms used.

The first project is a project called *HalbachOptimisation* [@O24] implements a data analysis step and optimizes a magnetic field that is as homogeneous as possible within a circular section using given mechanical dimensions as input parameters of the magnets which are used. For this purpose, a mutation of the magnet positions and rotations is performed. The result is a list of positions for each magnet.

The *HalbachMRIDesigner* [@MWO24] is an open-source project and generates basic (+cad) drawings for (+mri) magnets in a Halbach configuration. To do this, the number of magnets and additional parameters for the properties of the (+cad) model to be created are passed to the function provided as input parameters using a (+json) file. The result is an *OpenSCAD* [@MMN19] based 3D model of the magnet holder.

As a result, there are two projects which are both in combination suitable for the task of optimizing and generating Halbach magnets for (+mri) applications. The data structures are not compatible with each other and are usually executed manually one after the other by the user in order to obtain a result, whereby additional manual data conversion is required.

The (+mrp)-library solve this compatibility problem by providing standardized and flexible data structures for of magnetic field data and specified data flow guidelines.

The functionalities mapped by the two projects mentioned can be broken down into the following steps so that an optimised Halbach array can be generated from magnetic field data.
The implementation of the same functionalities from the mentioned projects above looks as follows when using the (+mrp)-library:

1. **Create magnetic field data**

  The input parameters of the *HalbachOptimisation* [@O24] project are the mechanical dimensions and the number of magnets to be used.
  Ideal magnets are assumed at this point. However, it should also be possible to import measured magnetic field data from measured magnets.
  Using the (+mri)-library data aquisition sub-step, it is possible to generate any number of ideal magnets or import measured magnets using sensor data from hardware sensors (see chapter \ref{example-sensors}).
 
2. **Add custom analysis processing step**

  Next, the user creates his own analysis step to be able to call up its functions.
  In the case of the *HalbachOptimisation* [@O24] project, the function signature of the start function must be changed.
  This receives the result of the previous step, in this case the generated magnet data.
  By optionally setting meta data in data type, constants can be replaced in the analysis function and made dynamically configurable.
  The return result also corresponds to the same data type so that subsequent steps are compatible and contains the magnet data with modified position and rotation data.

\newpage

3. **Generate fabrication data** 

  The last step is to call the *MWO24* [@MWO24] project, which creates the (+cad) model of the magnet holder and the model can be exported as file.
  To make the project compatible, the function signatures are adapted.
  In this case, more changes are required, as the configuration file is loaded from the file system.
  This logic needs to be removed to use the added meta data as input parameter instead.

After these customisation steps, executing both projects one after the other is possible and all required configuration parameters are contained in the data structure looped through the individual steps as meta data.
This also maps the functionality of a project file, which can be executed or passed on repeatedly.

This also fulfils the goal of making individual user-created algorithms interchangeable.
If the user wishes to use a different (+cad) algorithm instead of the example *HalbachMRIDesigner* [@MWO24] project, the other steps can simply be preserved and only the new step needs to be implemented.

## Modules


In order to realise the concept of *user interaction points* from chapter \ref{user-interaction-points}, the library is divided into different modules. These modules can be divided into two main categories:

* Core - All modules related to measurement data management
* Extensions - Contains modules for visualisations, hardware sensor access

In each of these categories there are then several sub-categories divided into User Interaction Points.
An overview of these is given in the subchapters as the following.
There are also introductory examples which provide an overview of the provided functions in the *Examples* \ref{examples} chapter, as well as further examples in the \href{https://magneticreadoutprocessing.readthedocs.io/en/latest/}{online documentation}.

### Core Modules

The included core modules are essential for using the library.
Basic data types are implemented, as well as functions for import and export.
In addition, there are other support scripts that are required internally.

The following modules are implemented in detail:

* *MRPReading* - storage of measured values
* *MRPMeasurementConfig* - storage of the measurement parameters
* *MRPMagnetTypes* - various physical constants for basic magnet types


The *MRPReading* module performs an essential role in streamlining the centralized management of measurement data. It serves as a storage provider for various measurements, offering functionalities that facilitate the creation and addition of data records.
To customise and add meta-data, users have the flexibility to configure parameters through the dedicated *MRPMeasurementConfig* module into a *MRPReading* instance.

Within the realm of measurement data, a diverse range of data points can be seamlessly incorporated.
The process is initiated by employing specialized functions designed for the creation and addition of data records.

To configure parameters, ensuring a tailored approach to the entire measurement process, these parameters act as an essential bridge between user preferences and the robust capabilities of the *MRPReading* module.

The system is also designed to be compatible with *Extension Modules* \ref{extension-modules}, allowing the generation of measurement data through various modules.
This extensibility enhances the versatility of the system, accommodating diverse measurement scenarios and expanding its utility across different domains.

To enhance the accessibility and interpretability of the recorded data, a dedicated module, *MRPMagnetTypes*, comes into play.
This module is specifically designed for the storage of physical parameters pertaining to the magnets targeted for measurement.

By centralizing this information, users can streamline the subsequent phases of evaluation and analysis, simplifying the overall process and ensuring a more efficient and insightful exploration of the collected data.

At the end of processing, the collected and modified data are typically exported; various functions are provided for this purpose.
This process is described in the following subchapter.

### Storage and Datamanagement

An important aspect is data import and export. On the one hand, this allows the library to reuse and archive the measurements.
On the other hand, the focus during development is that it is also possible to use the data in other programs.

For this purpose, an open, documented export format must be selected.
Ideally, this should be human-readable and viewable with a plain text editor.
This eliminates all binary-based formats such as the \href{https://docs.python.org/3/library/pickle.html}{Python-Pickle} package. Taking these points into account, the (+json) format is chosen.
This is human and machine readable and there is a compatible parser for every programming language.

The following Listing \ref{lst:json_export_format_example} shows an example (+json) structure which is generated when a measurement that using the library is dumped to the filesystem.
By using the (+json) format, all measurement points and metadata are available in readable plain text. This means that they can also be read out in other programs.
Using serialization, the *MRPReading* class inherited from Python-*Object* class is serialized via a dictionary conversion step. This (+json) string can then be processed directly or written to the file system as a file.

```json {#lst:json_export_format_example caption="JSON structure of an exported MRPReading based measurement with information about the measurement environment, additional meta-data and raw data value objects."}
{
  "time_start": "Wed Sep 20 08:50:13 2023",
  "time_end": "Wed Sep 20 08:54:13 2023",
  "additional_data": {
      "sensor_device_path": "/dev/ttyUnifiedSensorSingle",
      "sensor_name": "Unified Sensor Single Sensor",
      "sensor_id": "386731533439",
      "sensor_capabilities": ["static", "axis_b", "axis_x", "axis_y", "axis_z", "axis_temp", "time"],
      "configname": "calibrationtemp30.yaml",
      "runner": "cli"},
  "data": [{
      "value": {"b":0.135},
      "id": 0,
      "temperature": 34.32}],
  "measurement_config": {
      "sensor_distance_radius": 40.0,
      "magnet_type": 1// CUBIC 12x12x12mm N45
  },}
```

The exported example Listing \ref{lst:json_export_format_example} contains different object keys, which contain the following information:

* *additional_data* - Additional user-defined metadata
* *data* - Datapoint storage consists of measured value, (+uuid) and temperature, among other parameters
* *measurement_config* - Information about the sensor used for measurement

In addition, further custom objects can be inserted into the (+json) using the functions provided.
Since there are popular data processing frameworks such as *Numpy* [@HMW20], or the program for mathematical calculations, *MATLAB* are often used, the library also supports export formats for these systems.
The different formats can be triggered by the user by calling up the corresponding *MRPReading* class functions:

* *.dump() - (+json)
* *.to_numpy_matrix()* - *Numpy*-Array of *data* object with different options
* *.dump_savemat()* - *MATLAB* mat-file with measurement values and temperatures

Currently, data re-import of an exported measurement is only supported via the (+json) format, as an export using the *Numpy* or *MATLAB* based formats loses meta-data during the export procedure.
These only exports the raw measured values as an array represenation, so the additional attributes such as *additional_data* meta-data field (refer to Listing: \ref{lst:json_export_format_example}) are lost.

### Extension Modules

The extension modules build on the core modules and offer the user additional basic functionalities.
These include functions for data acquisition, visualisation and analysis.
 
#### Sensor Interface

Another collection of optional modules provided by the library is the connection of external hardware sensors.
All compatible sensors that are compatible with the firmware developed in the *Unified Sensor* \ref{unified-sensor} chapter are supported.
The library provides the following sensor (+hal) modules for this purpose:

\newpage

* *MRPHal* - Firmware protocol implementation
* *MRPHalLocal* - (+usb) sensor interface
* *MRPHalRemote* - Remote sensor interface

These provide functions to communicate with a connected hardware sensor and send commands to it. To generate these and convert the received measurement data into the appropriate format for the core modules, there is a suitable module for each sensor type:

* *MRPReadingSourceStatic* - for 1D and 2D sensors such as *1D: Single Sensor* \ref{d-single-sensor}
* *MRPReadingSourceFullSphere* - for 3D sensors such as *3D: Full Sphere* \ref{d-full-sphere}

The decision which of these modules to use is made automatically depending on the connected hardware.
For this purpose, a static function *createReadingSourceInstance* is implemented in the base class *MRPReadingSource*, which automatically creates the appropriate instance based on the sensor capabilities.


#### Visualisation

To give the user the possibility to display the recorded data visually, two modules are created, which can graphically prepare *MRPReading* instances:

* *MRPVisualization* - different table and graph-based plots
* *MRPPolarVisualization* - full sphere map plots

On the one hand, it is possible with the *MRPVisualization* module to display measurement data as a table or plot (e.g. stream, line, point).
This makes it possible, for example, to visually identify outliers or trends in the measurement data. These can also be saved as an image file.
The module is compatible with all measurement data.

In contrast to the *MRPPolarVisualization* module, this provides functions to create 2D map plots a polar coordinate system.
This requires measurement data with additionally set spatial coordinates.
These can be generated automatically with the *3D: Full Sphere* \ref{d-full-sphere} sensor, or the user must provide the spatial information from another source.


#### Analysis

Data analysis offers the user the greatest flexibility to implement their own modules.
For this reason, *MRPAnalysis* contains functions for calculating the following data analyses, which are compatible with class instances of *MRPReading*:

* *std_deviation* - (+sd)
* *mean* - Mean value
* *variance* - Variance
* *binning* - Distribution of a sample by means of a histogram using bins
* *k-nearest* - K-nearest neighbours

In addition, the export function *.to_numpy_matrix* enables further processing of the data in the *Numpy* [@HMW20] framework, in which many other standard analysis functions are implemented.

## Multi Sensor Setup

In the previous described scenarios, only the sensors that are directly connected to the host (+pc) can be detected and used.
That functionality has the disadvantage that there must always be a physical connection.
Difficulties arise when installing multiple sensors in measurement setups where space or cable routing options are limited.

Multiple sensors can be connected to any (+pc) which is available on the network.
This can be a (+sbc) (e.g. a *Raspberry Pi*).
The small footprint and low power consumption make it a viable choice. It can also be used in a temperature chamber.


The *MRPProxy* module in Figure \ref{MRP_library_proxy_module_usage_example_with_host_(+pc)_for_readout_processing_and_remote_(+pc)_for_sensor_communication_using_the_http_protocol.png} has been developed to allow forwarding and interaction with several sensors over a network connection using a (+rest) interface.
The approach of implementing this via a (+rest) interface also offers the advantage that several measurements or experiments can be recorded at the same time with one remote sensor setup.

%%MRP_library_proxy_module_usage_example_with_host_(+pc)_for_readout_processing_and_remote_(+pc)_for_sensor_communication_using_the_http_protocol.png%%

Another application example is when sensors are physically separated or there are long distances between them.
By connecting several sensors via the proxy module, it is possible to link several instances and all sensors available in the network are accessible to the *control* (+pc) by routing the requests through each *control* (+pc) in the chain to the target.

%%Example_MRP_proxy_module_usage_using_two_remote_(+pc)s.png%%

Figure \ref{Example_MRP_proxy_module_usage_using_two_remote_(+pc)s.png} shows the modified *multi-proxy - multi-sensor* topology.
Both proxy instances do not communicate directly with the *control* (+pc), but the proxy instance *remote* (+pc) *#2* can access the proxy running on *remote* (+pc) *#1*.
The *control* (+pc) only communicates with the *remote* (+pc) *#1*, but can access all sensors in this chain thought

### Network-Proxy

Figure \ref{Example_MRP_proxy_module_usage_using_two_remote_(+pc)s.png} shows the separation of the various (+hal) instances, which communicate with the physically connected sensors on the *remote* (+pc) and the *control* (+pc) side, which communicates with the remote side via the network. 
For the user, nothing changes in the procedure for setting up a measurement.
The *MRPProxy* (+cli) application must always be started like shown in Listing \ref{lst:mrpcli_proxy_start} on the (+pc) with connected hardware sensors attached.


```bash {#lst:mrpcli_proxy_start caption="MRPProxy usage to enable local sensor forwarding over the network. The CLI output shows the available sensor to the connected host PC."}
# START PROXY INSTNACE WITH TWO LOCALLY CONNECTED SENSORS
$ python3 mrpproxy.py proxy launch /dev/ttySENSOR_A /dev/ttySENSOR_B # add another proxy instance http://proxyinstance_2.local for multi-sensor, multi-proxy chain
Proxy started. http://remotepc.local:5556/
PRECHECK: SENSOR_HAL: 1337 # SENSOR A FOUND
PRECHECK: SENSOR_HAL: 4242 # SENSOR B FOUND
Terminate Proxy instance [y/N] [n]: 
```

After the proxy instance has been successfully started, it is optionally possible to check the status via the (+rest) interface, which is shown in Listing \ref{lst:mrpcli_config_rest}.

```bash {#lst:mrpcli_config_rest caption="MRPProxy provided REST endpoint query example using wget command line tool to send requests."}
# GET PROXY STATUS
$ wget http://proxyinstance.local:5556/proxy/status
{
"capabilities":[
  "static",
  "axis_b",
  "axis_x",
  "axis_y",
  "axis_z",
  "axis_temp",
  "axis_stimestamp"
],
"commands":[
  "status",
  "initialize",
  "disconnect",
  "combinedsensorcnt",
  "sensorcnt",
  "readsensor",
  "temp"
]}
# RUN A SENSOR COMMAND AND GET THE TOTAL SENSOR COUNT
$ wget http://proxyinstance.local:5556/proxy/command?cmd=combinedsensorcnt
{
"output":[
  "2"
]}
```

The query result shows that the sensors are connected correctly and that the capabilities have also been recognised correctly.
To be able to configure a measurement on the *control* (+pc), only the (+ip) address or hostname of the (+pc) running an *MRPProxy* instance is required as shown in Listing \ref{lst:mrpcli_config_using_rpc}. 

```bash {#lst:mrpcli_config_using_rpc caption="MRPcli usage example to connect with a MRPProxy based network sensor."}
# CONFIGURE MEASUREMENT JOB USING A PROXY INSTANCE
$ MRPCli config setupsensor testcfg --path http://proxyinstance.local:5556
> remote sensor connected: True using proxy connection:
> http://proxyinstance.local:5556 with 1 local sensor connected
```

### Sensor Synchronisation

Another important aspect for using several sensors via the proxy system is the synchronisation of the measurement intervals between the sensors. 
Individual sensor setups do not require any additional synchronisation information, as this is communicated via the (+usb) interface.
If several sensors are connected locally, they can be connected to each other via their sync input using short cables.
One sensor acts as the central clock as described in chapter \ref{sensor-synchronisation-interface}.
This no longer works for long distances and the synchronisation must be established via a shared network connection. 
If time-critical synchronisation over the network is required, (+ptp) and (+pps) output functionality [@O24] can be used on many (+sbc), such as the *Raspberry Pi Compute Module*.

### Command-Router

As it is possible to connect many identical sensors to one host, therefore it needs to be possible to address them separately.
This separation is done by the *MRPProxy* module, which is a separate part from the core (+mrp)-library, to keep installation package dependencies small.
Each connected sensor is accessed via the text-based (+cli), which is initially the same for each sensor. The only identification feature is the sensor (+uuid) by using the *id* command of the sensor (+cli). The *MRPProxy* instance claims to be a sensor to the host (+pc) running (+mrp) (+cli), so multiple sensors must be combined into one virtual one. This is done in several steps, the procedure is described in the following sub-chapters.

#### Merging the Sensor Capabilities

%%Sensor_capabilities_merging_algorithm.csv%%

Immediately after starting the *MRPProxy*, the (+uuid)s of all locally connected sensors are read out.
These are stored together with the class instance of the *MRPHal* module in a (+lut).
This makes it possible to address and interact with a  sensor directly using its (+uuid).
When using sensors with the same capabilities, these must be combined.
These are used to select the appropriate measurement mode for a measurement.
For this purpose, the *info* command of each sensor is queried.
This information is added to the previously created (+lut). Duplicate entries are summarised (see Table \ref{Sensor_capabilities_merging_algorithm.csv}) and returned to the host when the *info* \ref{lst:mtsc} command is received over network.
\newpage

```bash {#lst:mtsc caption="MRPProxy REST capabilities query result after executing the merging algorithm."}
# QUERY Network-Proxy capabilities
$ wget http://proxyinstance.local:5556/proxy/status
{"capabilities":[
"static",
"dynamic",
"axis_temp",
"axis_x"
]}
```

The same procedure is performed for all available (+cli)-command of each sensor, to merge available commands of connected sensors into the (+lut).


#### Dynamic extension of the available Network-Proxy Commands

For the host to be able to send a command to the network multi-sensor setup, the command received needs to be forwarded to the correct sensor.
In addition, there are commands such as the previously used *info* or *status* command, which must be intercepted by the *MRPProxy* module so that it can be handled differently (see example Listing \ref{lst:mtsc}). To realize this, a (+lut) is created in the previous steps, which contains information regarding *requested capability* -> *sensor*-(+uuid) -> *physical sensor* and allows the commands to be routed.

For commands, which have several entries for *CAPABLE SENSORS ID LUT* from Table \ref{Sensor_capabilities_merging_algorithm.csv}, there are two approaches to how the command is processed:

* Redirect to each capable sensor
* Extend commands using an id parameter

These two methods have been implemented and are applied automatically. The decision is based on which hardware sensors are connected. In a setup where only the same sensor variants are connected, *redirect to each capable sensor* is applied. This offers a time advantage as fewer commands need to be sent from the host. Thus, with a *readsensor* command, all sensors are read out via one command and the summarised result is transmitted to the host.

The *extend commands using an id parameter* strategy is used to differentiate sensors. Each command is extended on the *Network-Proxy*, which is explained in chapter \ref{network-proxy} by another (+uuid) parameter, according to the following scheme:

* *readsensor AXIS SENSOR_INDEX* -> *readsensor ID AXIS SENSOR_INDEX*
* *opmode* -> *opmode ID*

This allows the host to address individual sensors directly via their specific (+uuid) and extended id parameter.

## Examples

The following chapter shows some examples of how the (+mrp)-library can be used.
These examples are limited to a functional minimum for selected modules of the (+mrp)-library. The documentation in chapter \ref{documentation} contains further and more detailed examples.
Many basic examples are also supplied in the form of the test scripts used for testing in chapter \ref{testing}.

### MRPReading

The *MRPReading* is the key module of the (+mrp) core.
It is used to manage the measurement data and can be imported and exported.
The following example Listing \ref{lst:mrpexample_reading} shows how a measurement is created and measurement points are added in the form of *MRPReadingEntry* instances.

A crucial point is the management of the meta data, which further describes the measurement. This is realised in the example using the *set_additional_data* function.
The measurement is exported for archiving and further processing; various export formats are available. Using the *dump_to_file* function, the measurement can be converted into a open (+json) format.

\newpage

```python {#lst:mrpexample_reading caption="MRPReading example for setting up a basic measurement using Python code."}
from MRP import MRPReading, MRPMeasurementConfig
# [OPTIONAL] CONFIGURE READING USING MEASUREMENT CONFIG INSTANCE
config: MRPMeasurementConfig = MRPMeasurementConfig
config.sensor_distance_radius(40) # 40mm DISTANCE BETWEEN MAGNET AND SENSOR
config.magnet_type(N45_CUBIC_12x12x12) # CHECK MRPMagnetTypes.py FOR IMPLEMENTED TYPES
# CREATE READING
reading: MRPReading = MRPReading(config)
# ADD METADATA
reading.set_name("example reading")
reading.set_additional_data("description", "abc")
reading.set_additional_data("test-number", 1)
# EXAMPLE: INSERT A RANDOM DATAPOINT HERE
measurement = MRPReadingEntry.MRPReadingEntry()
measurement.value = random.random()
reading.insert_reading_instance(measurement, False)
# EXPORT MEASURED VALUES INto OTHER DATAFORMATS
npmatrix: np.ndarray = reading.to_numpy_matrix() ## NUMPY
csv: []= reading.to_value_array() ## CSV
js: dict= reading.dump() ## JSON
# EXPORT READING TO FILE
reading.dump_to_file("exported_reading.mag.json")
# IMPORT READING
imported_reading: MRPReading = MRPReading()
imported_reading.load_from_file("exported_reading.mag.json")
```


### MRPHal

The main function of the *MRPReading* module is to manage the measurement and meta-data. The next step is to record and store data points using hardware sensors.
For this purpose, the *MRPHal* module is developed, which can interact with all *Unified Sensor* compatible sensors (refer to chapter \ref{unified-sensor}).
In the following example Listing \ref{lst:mrpexample_hal}, an *1D: Single Sensor*, which is explained in chapter \ref{d-single-sensor}, is connected locally to the host (+pc).
\newpage


```python {#lst:mrpexample_hal caption="MRPHal example to use a connected hardware sensor to store raw sensor readings inside a measurement."}
from MRP import MRPHalSerialPortInformation, MRPHal, MRPBaseSensor, MRPReadingSource
# SEARCH FOR CONNECTED SENSORS
## LISTS LOCAL CONNECTED OR NETWORK SENSORS
system_ports = MRPHalSerialPortInformation.list_sensors()
sensor = MRPHal(system_ports[0])
# OR USE SPECIFIED SENSOR DEVICE
device_path = MRPHalSerialPortInformation("UnifiedSensor_4242")
sensor = MRPHal(device_path)
# RAW SENSOR INTERACTION MODE
sensor.connect()
basesensor = MRPBaseSensor.MRPBaseSensor(sensor)
basesensor.query_readout()
print(basesensor.get_b()) # GET RAW MEASUREMENT
print(basesensor.get_b(1)) # GET RAW DATA FROM SENSOR WITH ID 1
# TO GENERATE A READING THE perform_measurement FUNCTION CAN BE USED
reading_source = MRPReadingSourceHelper.createReadingSourceInstance(sensor)
result_readings: [MRPReading] = reading_source.perform_measurement(_readings=1, _hwavg=1)
```

In general, a sensor can be connected using its specific system path or the sensor (+uuid) via the *MRPHalSerialPortInformation* function.
Locally connected or network sensors can also be automatically recognised using the *list_sensors* function.
Once connected, these are then converted into a usable data source using the *MRPReadingSource* module. This automatically recognises the type of sensor and generated an *MRPReading* instance with the measured values of the sensor.

### MRPSimulation

If no hardware sensor is available for the generation of test data, the *MRPSimulation* module is available. This contains a series of functions that simulate various magnets and their fields. The result is a complete *MRPReading* measurement with a wide range of set meta data. The example Listing \ref{lst:mrpexample_simulation} illustrates the basic usage.
Different variations of the *generate_reading* function offer the user additional parameterisation options, such as random polarisation direction or a defined centre-of-gravity vector.
The data is generated in the background using the *magpylib* [@OB20] library according to the specified parameters.

```python {#lst:mrpexample_simulation caption="MRPSimulation example illustrates the usage of several functions how to generate simulated magnets."}
from MRP import MRPSimulation, MRPPolarVisualization, MRPReading
# GENERATE SILUMATED READING USING A SIMULATED HALLSENSOR FROM magpy LIBRARY
reading = MRPSimulation.generate_reading(MagnetType.N45_CUBIC_12x12x12,_add_random_polarisation=True)
# GENERATE A FULL SPHERE MAP READING
reading_fullsphere = MRPSimulation.generate_random_full_sphere_reading()
# RENDER READING TO FILE IN 3D
visu = MRPPolarVisualization(reading)
visu.plot3d("simulated_reading.png")
# EXPORT READING
reading.dump_to_file("simulated_reading.mag.json")
```

### MRPAnalysis

Once data can be acquired using hardware or software sensors, the next step is to analyse this data. (+mrp) provides some simple analysis functions for this purpose. The code example shows the basic use of the module.
The chapter *Evaluation* \ref{evaluation} shows how the user can implement their own algorithms and add them to the library.

```python {#lst:mrpexample_analysis caption="MRPAnalysis example code performs several data analysis steps."}
from MRP import MRPAnalysis, MRPReading
# CREATE A SAMPLE MEASUREMENT WITH SIMULATED DATA
reading = MRPSimulation.generate_reading(MagnetType.N45_CUBIC_10x10x10)
# CALCULATE MEAN
print(MRPAnalysis.calculate_mean(reading))
# CALCULATE STD DEVIATION ON TEMPERATURE AXIS
print(MRPAnalysis.calculate_std_deviation(reading, _temp_axis=True))
# CALCULATE CENTER OF GRAVITY
(x, y, z) = MRPAnalysis.calculate_center_of_gravity(reading)
# APPLY CALIBRATION READING TO REMOVE BACKGROUND NOISE
calibration_reading = MRPSimulation.generate_reading(MagnetType.N45_CUBIC_10x10x10, _ideal = True)
MRPAnalysis.apply_calibration_data_inplace(calibration_reading,reading)
```

### MRPVisualisation

This final example shows the use of the *MRPVisualisation* module, which provides general functions for visualising measurements.
The visualisation options make it possible to visually assess the results of a measurement. This is particularly helpful for full sphere measurements recorded with the *3D: Full sphere* sensor introduced in chapter \ref{d-full-sphere}.
The sub-module *MRPPolarVisualisation* is specially designed for these. Figure \ref{Example_full_sphere_plot_of_an_measurement_using_the_MRPVisualisation_module_using_different_shaded_vertices_on_a_sphere.png} shows a plot of a full sphere measurement.
It is also possible to export the data from the *MRPAnalysis* module graphically as diagrams.
The *MRPVisualisation* modules are used for this.
The following example Listing \ref{lst:mrpexample_visualisation} shows the usage of both modules.

```python {#lst:mrpexample_visualisation caption="MRPVisualisation example which plots a full sphere to an image file."}
from MRP import MRPPolarVisualization
# CREATE MRPPolarVisualization INSTANCE
## IT CAN BE REUSED CALLING plot2d AGAIN, AFTER LINKED READING DATA ARE MODIFIED
visu = MRPPolarVisualization.MRPPolarVisualization(reading)
# 2D PLOT INTO A WINDOW
visu.plot2d_top(None)
visu.plot2d_side(None)
# 3D PLOT TO FILE
visu.plot3d(os.path.join('./plot3d_3d.png'))
# PLOT ANALYSIS RESULTS
from MRP import MRPDataVisualization
MRPDataVisualization.MRPDataVisualization.plot_error([reading_a, reading_b, reading_c])
```

%%Example_full_sphere_plot_of_an_measurement_using_the_MRPVisualisation_module_using_different_shaded_vertices_on_a_sphere.png%%

### MRPHalbachArrayGenerator

The following example Listing \ref{lst:mrpexample_halbach} shows how a simple Halbach magnetic ring can be generated. This can be used to construct a Halbach ring magnet (see chapter \ref{magnet-system}) for a low-field (+mri).
Eight random measurements are generated at this point.
It is important that the magnet type (for example *N45_CUBIC_15x15x15* refers to a type *N45* cubic 15x15x15mm neodymium magnet) is specified.
This is necessary so that the correct magnet cutouts can be generated when creating the 3D model. 

After the measurements have been generated, they are provided with a position and rotation offset according to the Halbach design and calculation scheme [@O24] using the *MRPHalbachArrayGenerator* module.

```python {#lst:mrpexample_halbach caption="MRPHalbachArrayGenerator example for generating an OpenSCAD based Halbach ring."}
readings = []
for idx in range(8):
  # GENERATE EXAMPLE READINGS USING N45 CUBIC 15x15x15 MAGNETS
  readings.append(MRPSimulation.MRPSimulation.generate_reading(MRPMagnetTypes.MagnetType.N45_CUBIC_15x15x15))
## GENERATE HALBACH
halbach_array: MRPHalbachArrayGenerator.MRPHalbachArrayResult = MRPHalbachArrayGenerator.MRPHalbachArrayGenerator.generate_1k_halbach_using_polarisation_direction(readings)
# EXPORT TO OPENSCAD
## 2D MODE DXF e.g. for laser cutting
MRPHalbachArrayGenerator.MRPHalbachArrayGenerator.generate_openscad_model([halbach_array], "./2d_test.scad",_2d_object_code=True)
## 3D MODE e.g. for 3D printing
MRPHalbachArrayGenerator.MRPHalbachArrayGenerator.generate_openscad_model([halbach_array], "./3d_test.scad",_2d_object_code=False)
```

In the last step, a 3D model with the dimensions of the magnet type set is generated from the generated magnet positions.
The result is an *OpenSCAD* [@MMN19] file, which contains the module generated. After computing the model using the *OpenSCAD* (+cli) utility, the following model rendering shown in Figure \ref{Generated_Halbach_array_with_generated_cutouts_for_eight_magnets.png} can be generated.

%%Generated_Halbach_array_with_generated_cutouts_for_eight_magnets.png%%

# Usability Improvements

Usability improvements in software libraries are essential for efficient and user-friendly development.
Intuitive API documentation, clearly structured code examples and improved error messages promote a smooth developer experience.
A (+gui) or (+cli) application for complex libraries can make them more user-friendly, especially for developers with less experience.
Continuous feedback through automated tests and comprehensive error logs enable faster bug fixing.

The integration of user feedback and regular updates promotes the adaptability of the (+mrp)-library.
Effective usability improvements help to speed up development processes and increase the satisfaction of the developer community.
In the following, some of these have been added in and around the (+mrp)-library, but they are only optional components for the intended use.

## Command Line Interface

%%MRP_(+cli)_output_to_configure_a_new_measurement.png%%

In the first version of the (+mrp)-library, the user had to write his own Python scripts even for short measurement and visualisation tasks.
This is already a time-consuming process for reading out a sensor and configuring the measurement parameters and metadata and quickly required more than 100 lines of new Python code.

Although such examples are provided in the documentation, it must be possible for programming beginners in particular to use them.
To simplify these tasks, a (+cli) is implemented and implements the following functionalities:

* Detection of connected sensors
* Configuration of measurement series
* Recording of measured values from stored measurement series
* Simple commands for checking recorded measurement series and their data

As a result of this implemented functionality of the (+cli), it is now possible to connect a sensor to the (+pc), configure a measurement series with it and run it at the end, which is shown in Figure \ref{MRP_(+cli)_output_to_configure_a_new_measurement.png}. The result is an exported file with the measured values.
These can then be read in again using the *MRPReading* module and processed further. The following bash Listing \ref{lst:MRPCli_config_run} shows the setup procedure in detail:

```bash {#lst:MRPCli_config_run caption="MRPCli example usage for configuration of a measurement run."}
# CLI EXAMPLE FOR CONFIGURING A MEASUREMENT RUN
## CONFIGURE THE SENSOR TO USE
$ MRPCli config setupsensor testcfg
> 0 - Unified Sensor 386731533439 - /dev/cu.usbmodem3867315334391
> Please select one of the found sensors [0]:
> sensor connected: True 1243455
## CONFIGURE THE MEASUREMENT
$ MRPCli config setup testcfg
> CONFIGURE testcfg
> READING-NAME: [testreading]: testreading
> OUTPUT-FOLDER [/cli/reading]: /tmp/reading_folder_path
> NUMBER DATAPOINTS: [1]: 10
> NUMBER AVERAGE READINGS PER DATAPOINT: [1]: 100
# RUN THE CONFIGURED MEASUREMENT
$ MRPCli measure run
> STARTING MEASUREMENT RUN WITH FOLLOWING CONFIGS: ['testcfg']
> config-test: OK
> sensor-connection-test: OK
> START MEASUREMENT CYCLE
> sampling 10 datapoints with 100 average readings
> SID:0 DP:0 B:47.359mT TEMP:23.56
> ....
> dump_to_file testreading_ID:525771256544952_SID:0_MAG:N45_CUBIC_12x12x12mm.mag.json
```

## Programmable Data Processing Pipeline

%%Example_measurement_analysis_pipeline.png%%

The next logical step is to analyse the recorded data.
This can involve one or several hundred data records. Again, the procedure for the user is to write their own evaluation Python scripts using the (+mrp)-library.
This is particularly useful for complex analyses or custom algorithms, but not necessarily for simple standard tasks such as bias compensation or graphical plot outputs.
For this purpose, (+cli) application is created further, to enable the user to create and execute complex evaluation pipelines for measurement data without programming.
Figure \ref{Example_measurement_analysis_pipeline.png} shows a typical measurement data analysis pipeline, which consists of the following steps:

1. Import the measurements
2. Determine sensor bias value from imported measurements using a reference measurement
3. Apply linear temperature compensation
4. Export the modified measurements
5. Create a graphical plot of all measurements with standard deviation

In order to implement such a pipeline, the(+yaml) file format is chosen for the definition of the pipeline, as this is for non-programmers to understand and can also be easily edited with a plain text editor.
Detailed examples can be found in the \href{https://magneticreadoutprocessing.readthedocs.io/en/latest/}{documentation}. The pipeline definition consists of sections which execute the appropriate Python commands in the background.
The function signatures in the (+yaml) file are called using reflection and a real-time search of the loaded *global()* functions \href{https://docs.python.org/3/library/functions.html#globals}{symbol table}.
This system is capable to make all Python functions available to the user.
To simplify usage, a pre-defined list of verified and tested functions for use in pipelines is listed in the \href{https://magneticreadoutprocessing.readthedocs.io/en/latest/}{documentation}.
The following pipeline definition in Listing \ref{lst:mrpuddp_example_yaml} shows the previously defined steps shown in Figure \ref{Example_measurement_analysis_pipeline.png} as (+yaml) syntax.

\newpage

```yaml {#lst:mrpuddp_example_yaml caption="Example YAML code of a user defined processing pipeline with six stages linked together."}
stage import_readings:
  function: import_readings
  parameters:
    IP_input_folder: ./readings/fullsphere/
    IP_file_regex: 360_(.)*.mag.json

stage import_bias_reading:
  function: import_readings
  parameters:
    IP_input_folder: ./readings/fullsphere/
    IP_file_regex: bias_reading.mag.json

stage apply_bias_offset:
  function: apply_sensor_bias_offset
  parameters:
    bias_readings: stage import_bias_reading # USE RESULT FROM FUNCTION import_bias_reading
    readings_to_calibrate: stage import_readings

stage apply_temp_compensation:
  function: apply_temperature_compensation
  parameters:
    readings_to_calibrate: stage import_readings # USE RESULT FROM FUNCTION import_readings

stage plot_normal_bias_offset:
  function: plot_readings
  parameters:
    readings_to_plot: stage apply_temp_compensation
    IP_export_folder: ./readings/fullsphere/plots/
    IP_plot_headline_prefix: Sample N45 12x12x12mm magnets calibrated

stage export_readings:
  function: export_readings
  parameters:
    readings_to_plot: stage apply_temp_compensation
    IP_export_folder: ./readings/fullsphere/plots/
```

\newpage

Each pipeline step is divided into *stages*, which contain a name, the function to be executed and its parameters.

The various steps are linked by using the *stage NAME* macro as input parameter of the next function to be executed (see comments in Listing \ref{lst:mrpuddp_example_yaml}).
Therefore, it is feasible to use the results of one function in several others without them directly following each other.
The disadvantages of this system are the following:

* No circular parameter dependencies
* Complex determination of the execution sequence of the steps

To determine the order of the pipeline steps, the parser script created converts them into one problem of the graph theories. Each step represents a node in the graph and the steps referred to by the input parameter form the edges.
After several simplification steps, determination of start steps and repeated traversal, the final execution sequence can be determined in the form of a call tree in Figure \ref{Example_result_of_an_step_execution_tree_from_user_defined_processing_pipeline.png}.
The individual steps are then executed along the graph.
The intermediate results and the results in Figure \ref{Generated_pipeline_output_files_and example_results_combined_into_one_plot_after_running_example_pipeline_on_a_set_of_readings.png} are saved for optional later use.

%%Example_result_of_an_step_execution_tree_from_user_defined_processing_pipeline.png%%

%%Generated_pipeline_output_files_and example_results_combined_into_one_plot_after_running_example_pipeline_on_a_set_of_readings.png%%

## Testing

%%MRP_library_test_results_for_different_submodules_executed_in_PyCharm_(+ide).png%%

Software tests in libraries offer numerous advantages for improving quality and efficiency. Software tests ease to identify errors and vulnerabilities before the software is released as an updated version.

This significantly improves the reliability of (+mrp)-library applications.
Tests also ensure consistent and reliable performance, which is particularly important when libraries are used by different users and for different use cases.

During the development of the (+mrp)-library, test cases are also created for all important functionalities and use cases.
The test framework *PyTest* [@P17] is used for this purpose, as it offers direct integration in most (+ide)s (see Figure \ref{MRP_library_test_results_for_different_submodules_executed_in_PyCharm_(+ide).png}) and also because it provides detailed and easy-to-understand test reports as output in order to quickly identify and correct errors.
It also allows to tag tests, which is useful for grouping tests or excluding certain tests in certain build environment scenarios.
Since all intended use cases are mapped using the test cases created, the code of the test cases could later be used in slightly simplified variants of Listing \ref{lst:pytest_example_code} as examples for the documentation. 


```python {#lst:pytest_example_code caption="Example of a PyTest class for testing the internal functions of the MRPReading and MRPSimulation modules."}
class TestMPRReading(unittest.TestCase):
  # PREPARE AN INITIAL CONFIGURATION FILE FOR ALL FOLLOWING TEST CASES IN THIS FILE
  def setUp(self) -> None:
    self.test_folder: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tmp")
    self.test_file:str = os.path.join(self.import_export_test_folderpath, "tmp")

  def test_matrix(self):
    reading: MRPReading = MRPSimulation.generate_reading()
    matrix: np.ndarray = reading.to_numpy_matrix()
    n_phi: float = reading.measurement_config.n_phi
    n_theta: float = reading.measurement_config.n_theta
    # CHECK MATRIX SHAPE
    self.assertTrue(matrix.shape != (n_theta,))
    self.assertTrue(len(matrix.shape) <= n_phi)

  def test_export_reading(self) -> None:
    reading: MRPReading = MRPSimulation.generate_reading()
    self.assertIsNotNone(reading)
    # EXPORT READING TO A FILE
    reading.dump_to_file(self.test_file)

  def test_import_reading(self):
    # CREATE EMPTY READING AND LOAD FROM FILE
    reading_imported:MRPReading = MRPReading.MRPReading(None)
    reading_imported.load_from_file(self.test_file)
    # COMPARE
    self.assertIsNotNone(reading_imported.compare(MRPSimulation.generate_reading()))
```

Difficulties arise with the parts of the (+mrp)-library that require direct access to external hardware.
These are, for example, the *MRPHal* and *MRPHalRest* modules, which are required to read out sensors connected via the network.
Two different approaches are used:

* **Local Test Execution**:
  In the case of local development, the test runs are carried out on a (+pc) that can reach the network hardware and thus the test run could be carried out with real data.

* **Remote Test Execution**: 
  In the other scenario, the tests are to be executed out before a new published release in the repository based on \href{https://github.com/features/actions}{GithubActions}.
  It has the possibility to host local build (runner) software, which then has access to the hardware, but in this case a (+pc) must be permanently available for this task.
  Instead, the hardware sensors are simulated by software and executed via virtualisation on the services systems. The simulation of the hardware is implemented using (+usb) emulation, which uses a (+lut) to provide the expected or incorrect feedback.

\newpage

## Package Distribution

%%MagneticReadoutProcessing_library_hosted_on_PyPi.png%%

One crucial point that improves usability for users is the simple installation of all (+mrp) modules.
As it is created in the Python programming language, there are several public package registries where users can provide their software modules. For this purpose \href{https://pypi.org}{PyPI} Figure \ref{MagneticReadoutProcessing_library_hosted_on_PyPi.png} is the most used package registry and offers direct support for the package installation program (+pip) shown in Listing \ref{lst:setup_lib_with_pip}.

(+pip) not only manages package dependencies, but also manages the installation of different versions of a package.
In addition, the version compatibility is also checked during the installation of a new package, which can be resolved manually by the user in the event of conflicts.

```bash {#lst:setup_lib_with_pip caption="Bash commands to install the MagneticReadoutProcessing library using PIP."}
# https://pypi.org/project/MagneticReadoutProcessing/
# install the latest version
$ pip3 install MagneticReadoutProcessing
# install the specific version 1.4.0
$ pip3 install MagneticReadoutProcessing==1.4.0
```

To make the (+mrp) file structure compatible with the package registry, Python provides separate installation routines that build a package in an isolated environment and then provide an installation \href{https://peps.python.org/pep-0427/}{wheel} archive.
This can be uploaded to the package registry.

Since the (+mrp)-library requires additional Python dependencies, which cannot be assumed to be already installed on the target system, these must be installed prior to the actual installation. These can be specified in the library installation configuration *setup.py* in Listing \ref{lst:setup_py_req} for this purpose.

\newpage

```python {#lst:setup_py_req caption="setup.py with dynamic requirement parsing using a given requirements.txt."}
# dynamic requirement loading using requirements.txt
req_path = './requirements.txt'
with pathlib.Path(req_path).open() as requirements_txt:
  install_requires = [str(requirement) for requirement in pkg_resources.parse_requirements(requirements_txt)]

setup(name='MagneticReadoutProcessing',
  version='1.4.3',
  url='https://github.com/LFB-MRI/MagnetCharacterization/',
  packages= ['MRP', 'MRPCli', 'MRPudpp', 'MRPproxy'],
  install_requires=install_requires,
  entry_points={
    'console_scripts': [
      'MRPCli = MRPCli.cli:run',
      'MRPUdpp = MRPUdpp.uddp:run',
      'MRPProxy = MRPProxy.mrpproxy:run'
    ]
  }
)
```

The (+cli) scripts are written in Python and simplify the execution for the user since there is no *python3* prefix needed. This has been configured in the installation configuration using the *entry_points* option, and the following commands are available to the user:

* *$ MRPCli --help* instead of *$ python3 cli.py --help*
* *$ MRPUdpp --help* instead of *$ python3 udpp.py --help*
* *$ MRPProxy --help* instead of *$ python3 proxy.py --help*

In addition, these commands are available globally in the system without the terminal shell located in the (+mrp)-library folder.

### Documentation

To provide comprehensive documentation for the end-user, the source code is documented using Python-\href{https://peps.python.org/pep-0257/}{Docstrings} and the Python type annotations.
The use of type annotations also simplifies further development, as modern (+ide)s can more reliably display methods to the user as an assistance. It is implemented in Listing \ref{lst:pydocstring}.

\newpage

```python {#lst:pydocstring caption="Documentation using Python docstring example."}
# MRPDataVisualisation.py - example docstring
def plot_temperature(_readings: [MRPReading.MRPReading], _title: str = '', _filename: str = None, _unit: str = "degree C") -> str:
  """
  Plots a temperature bar graph of the reading data entries as figure
  :param _readings: readings to plot
  :type _readings: list(MRPReading.MRPReading)
  :param _title: Title text of the figure, embedded into the head
  :type _title: str
  :param _filename: export graphic to a given absolute file path with .png
  :type _filename: str
  :returns: returns the abs file path of the generated file
  :rtype: str
  """
  if _readings is None or len(_readings) <= 0:
      raise MRPDataVisualizationException("no readings in _reading given")
  num_readings = len(_readings)
  # ...
```

Since *docstrings* only document the source code, but do not provide simple how-to-use instructions, the documentation framework *Sphinx* [@G17] is used for this purpose.
This framework offers the functionality to generate (+html) or (+pdf) documentation from various source code documentation formats, such as the used *docstrings*.

These are converted into a Markdown format in an intermediate step and this also allows to add further user documentation such as examples or installation instructions. Once the finished documentation has been generated from static (+html) files, it is stored in the project repository.
Another publication option is to host the documentation via online services such as \href{https://readthedocs.com}{ReadTheDocs}, where users can make documentation for typical software projects available to others.

The documentation has also been uploaded to the \href{https://magneticreadoutprocessing.readthedocs.io/}{ReadTheDocs} service. Figure \ref{MagneticReadoutProcessing_documentation_hosted_on_ReadTheDocs.png} shows a screenshot of the start page, which also lists separate menu items for tutorials on the individual functionalities.
The process of creating and publishing the documentation has been automated using \href{https://github.com/features/actions}{GithubActions}, so that it is always automatically kept up to date with new features.



%%MagneticReadoutProcessing_documentation_hosted_on_ReadTheDocs.png%%

# Use Case Evaluation

The practical application of the hardware and software framework is shown below.
It is implemented by using the previously defined use cases in chapter *Use cases* \ref{use-cases}.
In the application example, various permanent magnets are measured and then sorted according to their field strength.
The result should then list the magnets that deviate the least from each other in terms of their field strength.
This is determined using a sorting algorithm developed by the user.

The process is broken down into the following steps and the practical application of *User Interaction Points* in chapter \ref{user-interaction-points} is shown:

1. **Hardware preparation**:
   Users can prepare measurements using the implemented framework. This includes the placement of the sensors and the selection of the relevant parameters for the characterisation of the permanent magnets.

2. **Configuration of the measurement**:
   The software provides a user-friendly interface for configuring the measurement parameters. Users can make the desired settings here and customise the framework to their specific requirements.

3. **Custom algorithm implementation**:
   An important contribution of the (+mrp) ecosystem is the possibility for users to implement their own algorithm for data analysis. This allows customisation to specific research questions or experimental requirements.

4. **Execution of analysis pipeline**:
   The analysis pipeline can then be executed with the implemented algorithm. The collected measurement data is automatically processed and analysed to extract characteristic parameters of the permanent magnets.

\newpage

This process covers all the essential functionalities required for a comprehensive characterisation of permanent magnets.
These are previously described in the chapter *Use cases* \ref{use-cases}.
The developed framework not only offers a cost-effective and flexible hardware solution, but also enables customisation of the analysis algorithms to meet the requirements of different research projects.


## Hardware Preparation

%%Ten_numbered_N45_12x12x12mm_test_magnets_in_separate_3D_printed_holders.png%%

For the hardware setup, the 3D-Full Sphere sensor, explained in chapter \ref{d-full-sphere}, is used for the evaluation of the framework. As this is equipped with an exchangeable magnetic holder mount, suitable holders are required for the magnets to be measured. Ten random *N45 12x12x12mm* neodymium magnets are used, which are shown in Figure \ref{Ten_numbered_N45_12x12x12mm_test_magnets_in_separate_3D_printed_holders.png}.

These are placed in modified 3D printed holders shown in Figure \ref{Ten_numbered_N45_12x12x12mm_test_magnets_in_separate_3D_printed_holders.png} and afterwards numbered. This allows to match the magnets to the measurement results later.

## Configuration of the Measurement

The configured hardware is connected to the host system using the *MRPCli config setupsensor*-(+cli) command.
The measurement is configured for a measurement run, using the following configuration commands from Listing \ref{lst:evaluation_measurement_config}.

The *MRPCli measure ruxn* command is then called up for each individual magnet to execute a measurement. 
After each run, the *READING-NAME* parameter is filled with the id of the next magnet so that all measurements could be assigned to the physical magnets.

```bash {#lst:evaluation_measurement_config caption="Measurement configuration for evaluation measurement."}
## CONFIGURE THE MEASUREMENT
$ MRPCli config setup eval_measurement_config
> READING-NAME: 360_eval_magnet_<id>
> OUTPUT-FOLDER: ./readings/evaluation/ 
> NUMBER DATAPOINTS: 18 # FOR A FULL SPHERE READING USE MULTIBLE OF 18
> NUMBER AVERAGE READINGS PER DATAPOINT: 10
```

## Custom Algorithm Implementation

The next step for the user is the implementation of the filter algorithm in Listing \ref{lst:custom_find_similar_values_algorithm}. This can have any function signature and is implemented in the file *UDPPFunctionCollection.py*.
This Python file is loaded when the pipeline is started and all functions that are imported as a module or implemented directly can be called via the pipeline.
As this is a short algorithm, it is inserted directly into the file.

The parameter _readings should later receive the imported measurements from the *stage rawimport* in Listing \ref{lst:pipeline_mrp_evaluation_yaml} and the optional *IP_return_count* parameter specifies the number of best measurements that are returned.
The return parameter is a list of measurements containing the most similar measurements, measured by the smallest distance between all measurements.

The sorting indicator for each measurement is determined using the *(+cog)* function and is implemented using the following equation:

\noteworthy{\text{CoG} = \frac{\sum{D_{istance} \times W_{eight}}}{\sum{W_{eight}}}}{: Center of Gravity} 

Where *$D_{distance}$* corresponds to the set distance from the centre of the magnet to the surface of the sensor (+ic). This is the same for each measuring point in the measurement and corresponds to the mechanical structure of the *3D: Full Sphere* \ref{d-full-sphere} sensor *40mm*. The weighting *$W_{eight}$* corresponds here to the *B*-field value in $\mu$T measured by the *TLV493D* sensor.

```python {#lst:custom_find_similar_values_algorithm caption="User implemented custom find most similar readings algorithm."}
@staticmethod
def FindSimilarValuesAlgorithm(_readings: [MRPReading.MRPReading], IP_return_count: int = -1) -> [MRPReading.MRPReading]:
  import heapq
  import math
  heap = []
  # SET RESULT VALUE COUNT
  IP_return_count = max([int(IP_return_count),len(_readings)])
  if IP_return_count < 0:
      IP_return_count = len(_readings) / 5
  # CALCULATE TARGET VALUE: CENTER OF GRAVITY MAGNITUDE FOR ALL READINGS
  target_value = 0.0
  for idx, r in enumerate(_readings):
      cog = MRPAnalysis.MRPAnalysis.calculate_center_of_gravity(r)
      # COMPUTE LENGTH OF VECTOR = B value
      cog_value: float = math.sqrt(cog[0]**2 + cog[1]**2 cog[2]**2)
      target_value = target_value + cog
  target_value = target_value / len(_readings)
  # PUSH READINGS TO HEAP
  for value in _readings:
      # USE DIFF AS PRIORITY VALUE IN MIN-HEAP
      cog = MRPAnalysis.MRPAnalysis.calculate_center_of_gravity(value)
      cog_value: float = math.sqrt(cog[0]**2 + cog[1]**2 cog[2]**2)
      diff = abs(cog_value - target_value)
      heapq.heappush(heap, (diff, cog_value))
  # RETURN X BEST ITEMS FROM HEAP
  similar_values = [item[1] for item in heapq.nsmallest(IP_return_count, heap)]
  # CLEAN UP USED LIBRARIES AND RETURN RESULT
  del heapq
  del math
  return similar_values
```

The calculated distances from the *(+cog)* value of the measurements to are inserted into a *heapq* priority queue. 
Subsequently, as many elements of the queue are returned as defined by the *IP_return_count* parameter. The actual sorting is carried out by the queue in the background.

### Alternative Filter Algorithm Implementation

Another possibility for filtering is to use a reference measurement instead of a simulated ideal magnet as a reference, as described before.
This can initially come from a magnet selected as a reference magnet.
As a result, the filter algorithm returns the measurements that are most similar to the selected reference magnet. The code snipped in Listing \ref{lst:custom_find_similar_values_algorithm_refmagnet} shows the modified filter algorithm code, with added _ref input parameter for the reference measurement.


```python {#lst:custom_find_similar_values_algorithm_refmagnet caption="Modified user implemented custom find algorithm using a reference magnet reading."}
@staticmethod
def FindSimilarValuesAlgorithmREF(_readings: [MRPReading.MRPReading], _ref: [MRPReading.MRPReading], IP_return_count: int = 4) -> [MRPReading.MRPReading]:
  # CALCULATE CoG VALUE OF REFERENCE MAGNET
  cog_ref = MRPAnalysis.MRPAnalysis.calculate_center_of_gravity(_ref[0])
  ref_value: float = math.sqrt(cog_ref[0]**2 + cog_ref[1]**2 cog_ref[2]**2)
  # PUSH READINGS TO HEAP
  for value in _readings:
      # USE DIFF AS PRIORITY VALUE IN MIN-HEAP
      cog = MRPAnalysis.MRPAnalysis.calculate_center_of_gravity(value)
      cog_value: float = math.sqrt(cog[0]**2 + cog[1]**2 cog[2]**2)
      heapq.heappush(heap, (abs(cog_value - ref_value), cog_value))
  # RETURN X BEST ITEMS FROM HEAP
  return [item[1] for item in heapq.nsmallest(IP_return_count, heap)]
```

## Execution of Analysis Pipeline

Once the filter function has been implemented, it still needs to be integrated into the analysis pipeline in Listing \ref{lst:pipeline_mrp_evaluation_yaml}.
At this point, the example pipeline in Figure \ref{Example_measurement_analysis_pipeline.png} is simplified and an additional stage *find_similar_values* has been added, which has set *FindSimilarValuesAlgorithm* as the function to be called.
As a decisive step, the result is used in the *plot_filtered* stage for visualisation.

\newpage

```yaml {#lst:pipeline_mrp_evaluation_yaml caption="User defined processing pipeline using custom implemented filter algorithm in third stage."}
name: pipeline_mrp_evaluation
stage rawimport:
  function: import_readings
  parameters:
    IP_input_folder: ./readings/evaluation/
    IP_file_regex: 360_(.)*.mag.json

stage find_similar_values:
  function: custom_find_similar_values_algorithm
  parameters:
    _readings: stage rawimport # USE RESULTS FROM rawimport STAGE
    IP_return_count: 4 # RETURN BEST 4 of 10 READINGS

stage plot_filtered:
  function: plot_readings
  parameters:
    readings_to_plot: stage find_similar_values # USE RESULTS FROM find_similar_values STAGE
    IP_export_folder: ./readings/evaluation/plots/plot_filtered/
    IP_plot_headline_prefix: MRP evaluation - filtered
```

The final pipeline has been saved in the pipeline directory as *pipeline_mrp_evaluation.yaml* file and is ready for execution.
This is carried out using the *MRPudpp* (+cli), which is described in Listing \ref{lst:bash_pipeline_mrp_evaluation_yaml}.
After the run has been successfully completed, the results are saved in the result folder specified in the pipeline using the *IP_export_folder* parameter.

```bash {#lst:bash_pipeline_mrp_evaluation_yaml caption="Bash result log of the analysis pipeline run."}
# LIST ACTIVE PIPELINES IN PIPELINE DIRECTORY 
$ MRPudpp pipeline listenabledpipelines
> Found enabled pipelines:
> 1. pipeline_mrp_evaluation.yaml
# EXECUTE THE EVALUATION PIPELINE
$ MRPudpp pipeline run
> loading pipeline pipeline_mrp_evaluation.yaml
> stage nodes: ['import', 'find_similar_values', 'plot_raw', 'plot_filtered']
> =====> stage: import 
> =====> stage: find_similar_values 
> =====> stage plot_filtered 
> Process finished with exit code 0
```

## Result Analysis



%%MRP_evaluation_result_after_find_similar_values_algorithm_execution_in_the_user_defined_pipeline.png%%

Figure \ref{MRP_evaluation_result_after_find_similar_values_algorithm_execution_in_the_user_defined_pipeline.png} shows the measured values filtered by the implemented filter algorithm of Listing \ref{lst:custom_find_similar_values_algorithm}. It can be seen that out of the initial *10* measurements (upper plot) only four measurements that are most similar to the *(+cog)* mean value are filtered (lower plot). The number of desired result measurements are defined here by the parameter *IP_return_count*. 
It can be seen from the plotted *(+cog)* $\mu$T mean values are close to an ideal Magnet with a *(+cog)* value of 0$\mu$T. This ideal value is calculated with the function *MRP.MRPSimulation.generate_simulated_reading*, using the same measurement parameters (*magnet type*, *dimensions*, *sensor distance*) as they correspond to the mechanical structure of the used hardware sensor in chapter \ref{d-full-sphere}.

It can be seen that there are measured magnets with larger deviations (see magnet index plots for *7:0*,*10-2:0*,*10-1:0* in Figure \ref{MRP_evaluation_result_after_find_similar_values_algorithm_execution_in_the_user_defined_pipeline.png}).

If the alternative filter algorithm from chapter *Alternative Filter Algorithm Implementation* \ref{alternative-filter-algorithm-implementation} is executed at this point, the same result is returned if the magnet measurement with (+id) *5:0* is used as the reference magnet.

The filter algorithm implemented by the user is thus successfully executed via the user-programmable pipeline.
The calculation result is successfully verified using raw measurement data and the result of the algorithm and verified using reference measurements.
The streamlined pipeline approach enables the user to re-execute the implemented measurement pipeline example with further measurement data. Changes to filter parameters, for example, are also possible without having to adapt the code.
Using this example, all the required functional capabilities from the chapter *Use cases* \ref{use-cases} of this implemented solution are demonstrated in their functional capability.

# Evaluation

In the previous chapter *Use Case Evaluation* \ref{use-case-evaluation} it is demonstrated that the implementation of the hardware and software framework for various magnetic field sensors is successfully implemented. In addition, the basic application of the framework for the user and the resulting advantages are demonstrated using the specific example.

Based on this it is possible to systematically characterise magnets from the software and readout hardware side by means of data acquisition, storage and analysis.

After the hardware and software components developed have been discussed in detail, the following chapter answers the question of which sensors fulfill the requirements described in chapter \ref{research-question-and-approach}:

* Measure a wide range of different permanent magnets with regard to their systematic field strength
* Automated measurement of the homogeneity with an accuracy of less than *1000 (+ppm)* what is demanded to measure Halbach rings

These questions are answered in the following as a basic readout and analysis functionality platform had to be created first and thus an automated sensor characterisation can be performed.

## Sensors for Evaluation

For this evaluation, the sensors listed in Table \ref{Digital_magnetic_field_sensors_characterised_for_evaluation.csv} are used for sensor characterisation. The selection of sensors is described in chapter \ref{sensor-selection}.
The additional column for the *Background Noise* is taken from the respective data sheets of the sensors and will be verified in the later *Background Noise* measurement in chapter \ref{sensor-characterisation-background-noise}.

%%Digital_magnetic_field_sensors_characterised_for_evaluation.csv%%

The values in Table \ref{Digital_magnetic_field_sensors_characterised_for_evaluation.csv} are taken from the data sheets of the relevant manufacturers as a reference for comparison with the later measurement results.

The developed framework is directly compatible with a variety of magnetic field sensors without modifications, including those listed in the table.
For this evaluation, the sensors listed in the table are used for sensor characterisation. This selection is made for the following reasons:

* Availability of ready to use development boards
* Specifications correspond to the application areas
* Availability for testing

It is possible to carry out the sensor characterisation demonstrated for other compatible sensors using the same procedure. Pre-configured measurements in chapter \ref{command-line-interface} and analysis pipelines in chapter \ref{programmable-data-processing-pipeline}, which are available for this purpose, are packaged within the library.
The following parameters are determined and analysed for the sensor evaulation:

* Background Noise
* Linearity
* Temperature Sensitivity

The characterisation methodology is modified and adapted from Crescentini, Gibiino and Piero [@CSG22], as their approaches are focused towards the analysis of analogue Hall sensors.
Direct transmission is not possible, as their methods are specially tailored to these sensors.
This includes measuring the analogue bias currents and raw sensor output voltages, which are not accessible with these digital-only sensors.
Adaptations are therefore necessary to extend the characterisation to the choosen digital sensors listed in Table \ref{Digital_magnetic_field_sensors_characterised_for_evaluation.csv}.

## Evaluation Sensor Setup

%%Sensor_evaluation_plattform_with_TLV493D_and MMC5603_sensors_placed_with_thermal_conductive_glue_on_an_aluminium_baseplate.png%%

The sensor platform used is an adapted version of the *1D: Single Sensor* from chapter \ref{d-single-sensor} sensor platform.
The sensors to be measured are fixed together on an aluminium plate with thermally conductive adhesive.
This compensates for thermal differences.
This is essential for the subsequent temperature deviation tests in order to obtain comparable measurement results. [@J21]


The set-up is set up and pre-wired in the temperature chamber *24* hours before the measurement series is performed.
The insulated housing of a *Voron 2.4* 3D printer, which has a separately controlled internal equipped heating system, is used as the temperature chamber.
To verify the temperature, an additional thermometer *7055BT* is placed on the base plate.
A *10mm* thick *PTFE* insulation plate is placed between the floor and the sensor base plate to prevent direct and uneven heating of the base plate by the heated floor.

Figure \ref{Sensor_evaluation_plattform_with_TLV493D_and MMC5603_sensors_placed_with_thermal_conductive_glue_on_an_aluminium_baseplate.png} shows this basic setup, the *Raspberry Pi Pico* is used as the readout hardware, on which the *Unified Sensor Firmware* is running.
With additional connected switch, it is possible to isolate or select a sensor or both sensors to be queried from the firmware.

A separate battery power supply is used as low-noise power supply for the sensor boards.
An *Raspberry Pi 4* is implemented as the host computer, which is connected to the sensors via a *Hailege ADUM3160* (+usb) isolator and is placed outside the temperature chamber.

For the software setup, *MRPCli* \ref{command-line-interface} is used to control and record the measurement series, with the functions of the *MRPDataVisualisation* \ref{mrpvisualisation} and *MRPAnalysis* \ref{mrpanalysis} packages from the library \ref{software-readout-framework} being used for subsequent evaluation.
The recorded measurement series are automatically analysed using the *Programmable-Data Processing Pipeline* \ref{programmable-data-processing-pipeline} and the results are visualised.

## Sensor Characterisation: Background Noise

%%Sensor_evaluation_setup_for_noise_measurements.png%%

Measuring the noise in a magnetic field sensor requires a precise procedure and a special measurement setup. First, the magnetic field sensor is placed in a quiet and static environment to minimize external field interference. The temperature chamber for all noise tests is set to *$\mu_{trev}$=21.0$^{\circ}$C* and the sensors are placed *24* hours before the measurement run in the final measurement configuration inside of the chamber.

%%Sensor_noise_evaluation_results.csv%%

The procedure starts with the acquisition of the baseline by operating the sensor without external magnetic fields.
For this purpose, a sample size of *$N_{baseline}$=10000* measured values is recorded for the baseline measurement.
The output signal of the sensor is continuously measured and recorded. It is important to carry out the measurement over a sufficiently lengthy period of time in order to record both short-term and long-term fluctuations. For this purpose, *$N_{measurement}$=2000* additional measured values are taken with a trigger and readout rate of one measurement per second.
In order to quantify the noise, the (+sd) of the signal is calculated. These parameters provide information about the variation of the signal over time and therefore about the sensor background noise. 


%%Sensor_noise_evaluation_results_for_TLV493D_and_MMC5603NJ_with_N=2000_samples_and_no_averaging.png%%

The following Figure \ref{Sensor_noise_evaluation_results_for_TLV493D_and_MMC5603NJ_with_N=2000_samples_and_no_averaging.png} contains the measured values of these sensors. In the next phases these are analysed for each sensor examined.
The following data is shown in the plots:

* Plot of the raw data of the sensor
* Plot of the sensor's internal temperature sensor
* Noise level with reference to the initial baseline
* Histogram of the background noise level

Table \ref{Sensor_noise_evaluation_results.csv} lists the measured values that are extracted from the measurement data of the sensors in Figure \ref{Sensor_noise_evaluation_results_for_TLV493D_and_MMC5603NJ_with_N=2000_samples_and_no_averaging.png}.
These measured values are categorised below.




### Sensor Temperature Analysis

The temperature stability of the *TLV493D* with a mean value of *20.68$^{\circ}$C* and a (+sd) of $\sigma_{t,TLV493D}$=0.53$^{\circ}$C shows a strongly noisy characteristic with an accuracy of two decimal places. The confidence interval varies between *20.15$^{\circ}$C* and *21.21$^{\circ}$C*, which is 
In contrast to the *MMC5603* with stable *19.40$^{\circ}$C*, this result is not suitable for use, e.g. for temperature compensation.
A second measurement run with another *TLV493D* confirms this result.

Both sensors provide an offset to the measured chamber temperature $\mu_{trev, 7055BT}$.

With an additional measurement run with a different temperature setting of *30.0$^{\circ}$C*, the measured temperature deviations and offsets remains constant.

As a result, an external temperature sensor should be used for temperature-critical measurements with the *TLV493D*. This is considered for the *Temperature Sensitivity* run in chapter \ref{sensor-characterisation-temperature-sensitivity}.

### Raw Sensor Data Analysis

The noise of a sensor describes unwanted, random fluctuations or signals in the measured data. These are clearly recognisable in Figure \ref{Sensor_noise_evaluation_results_for_TLV493D_and_MMC5603NJ_with_N=2000_samples_and_no_averaging.png} in the raw data plot. 
The baseline measurement which is previously determined for each sensor is shown by the red $\mu_{rv}$ [$\mu$T] line. It can be seen that each sensor has a different baseline offset in the same environment.
This variable is the result of multiple effects, including the electrical offset introduced by the front end and the effect of the earth's magnetic field [@CSG22] and the test environment.

For verification, a reference measurement of the environment is carried out with the calibrated *Voltcraft GM70* Telsameter next to the sensor (+ic).
This provides a reference baseline value of *$\mu_{rev, GM70}$=-21.0$\mu$T*.

The noise of the sensor is drawn around this using the blue line. 
For the *TLV493D* the (+sd) *$\sigma_{rv,TLV493D}$=172.0${\mu}$T*, which is twice the value given by the datasheet as the noise value (refer to Table \ref{Digital_magnetic_field_sensors_characterised_for_evaluation.csv}). The histogram of the measured values shows that the  *TLV493D* exhibits a asymmetry to measured values that are higher than the long-term mean values and as a result does not provide normally distributed data and provides isolated outliers. As a result, it is necessary to work with floating averages to obtain representative measured values.

Under the same conditions, the *MMC5603NJ* undercuts the value specified by the manufacturer. The (+sd) approaches *$\sigma_{rv, MMC5603NJ}$=0.20${\mu}$T* and is negligible, especially when additional averaging is used. The mean and median of the data are approximately the same, as the normal distribution is symmetrical, as shown by the hinstrogram.
As a result, most of the measured values are close to the long-term mean even without additional averaging.


Further measurement series are also recorded with inserted *N45 12x12x12mm* magnets, so that the sensors are saturated halfway through their (+dr).
This allows the noise measurement values to be compared with a blank measurement. These values correspond, so it can be concluded that the noise is within the same range across the measuring range.

## Sensor Characterisation: Linearity

%%Sensor_evaluation_setup_for_linearity_measurements.png%%

The sensor linearity of a magnetic field sensor or describes the ability of the sensor to provide a proportional linear response to changes in the magnetic field without non-linear distortions [@CSG22].
This means that the output signals of the sensor vary directly proportional to the input magnetic fields without deviations or distortions and is therefore an important indicator for measurements of fields at different distances or objects.
This is achieved by means of an additional linear axis installed above the sensor setup.
A holder for an *N45 12x12x12mm* magnet is attached to the end effector of this axis, which can thus be moved at different distances above the respective sensor (+ic). 
The ambient temperature is set to *$\mu_{trev, 7055BT}$=21.0$^{\circ}$C* in the measurement runs and thus corresponds to the same conditions as in the chapter *Background Noise* \ref{sensor-characterisation-background-noise} setup.

Figure \ref{Sensor_evaluation_setup_for_linearity_measurements.png} contains this updated measurement setup with the added components.
To control the linear axis an additional motion controller of the type *SKR-Pico* placed outside the temperature chamber is required, which can be controlled via a network interface.


### Measurement Setup

After the sensor baseline has been determined with *$N_{baseline}$=10000* samples, the magnet is inserted into the holder.
The linear axis is moved by the user until it is maximally saturated. With the *TLV493D*, this corresponds to *250.000$\mu$T* and below in low resolution mode. *MCC5603NJ* around *3000$\mu$T*.
This ensures that the linearity is determined over the entire measuring range.

### Measurement Run

The measurement run is then started using a script.
The user defines the path to be travelled by the linear axis.
A complete range of *120mm* in *1mm* steps is selected. The following automated process then runs as follows:
 
1. Move the linear axis upwards by the selected distance
2. De-energise the axis stepper motor
3. Create measurement using *MRPCli* with *$N_{measurement}$=2000* data points per reading and step
4. Export reading to filesystem with current linear axis position in meta-data and filename

### Linearity Analysis

After the measurements are exported, these are analysed for linearity using *MRPAnalysis* functions in chapter \ref{mrpanalysis}.

%%Sensor_linearity_evaluation_results_for_TLV493D_and_MMC5603NJ.png%%

Figure \ref{Sensor_linearity_evaluation_results_for_TLV493D_and_MMC5603NJ.png} combines the visual representation of linearity as a plot. Only the measuring range specified in the sensors data sheet is considered here, as linearity is guaranteed for this range. In terms of the *TLV493D* this is *0.5%* and in the case of the *MMC5603NJ* *0.1%*.

The distance from the magnet to the sensor is plotted in *mm* on the x-axis.
The measured value of the sensor is plotted on the y-axis.
This is not directly comparable for both plots, as the sensors have different measuring ranges.
To ensure comparability, the ideal curve is determined [@CSG22].
In order to be able to make quantifiable statements about the measurement results, the mean and (+sd) deviation of these two curves is determined.

For both sensors, the deviation is less than *1%* over the entire resolution. With the *MMC5603NJ* this is on average only *0.04%*. With the *TLV493D* the (+sd) is *3.64%*, for which the deviations at the end in particular (with field strengths towards zero) are decisive.
In general, the measured values correspond to the data sheet specifications of both sensors, which specify a value of *5%*.
It is also feasible to calculate these small deviations using curve fitting methods. Suitable functions are implemented in the library.


### Dynamic Range Analysis

%%Sensor_dynamic_range_evaluation_results_for_TLV493D_and_MMC5603NJ.png%%

With the same setup as for the linearity measurement, the (+dr) can be determined outside the range specified by the manufacturer. As a result, it is possible to analyze how the sensor behaves when the defined (+dr) is exceeded. This allows the extent to which the limits of the sensors can be exhausted to be taken into account in subsequent measurement setups.
A high (+dr) enables a more precise detection of magnetic fields, while a low (+dr) can lead to the sensor detecting magnetic fields outside its detection range.

Figure \ref{Sensor_dynamic_range_evaluation_results_for_TLV493D_and_MMC5603NJ.png} shows the plot of the linearity measurement outside the specified (+dr) for the respective sensor. 
For the *TLV493D* a (+dr) of almost double the specified (+dr) could be measured, with a peak value of *240mT* with constant linearity deviation.
The *MMC5603NJ* measures the same linear values as in the linearity measurement. From a measured value of *3.4mT* it reaches a plateau and does not increase any further.
As a result, the full specified (+dr) can be fully utilized with both sensors.

This extended characterized (+dr) is not used in the further analyses. Reference is made exclusively to the values specified by the manufacturer, as the values determined do not apply to every sensor (+ic) of the same type.


## Sensor Characterisation: Temperature Sensitivity

The temperature sensitivity of magnetic field sensors describes how sensitively the sensors output is sensitive to temperature changes.
It is important to ensure that temperature fluctuations do not affect measurement accuracy. A low temperature sensitivity reduces errors due to temperature changes [@J21].
An accurate temperature sensitivity characteristic is therefore crucial for subsequent precise magnetic field measurements. As the temperature sensor *TLV493D* in particular produced vastly different results in the previous measurements, an additional temperature sensor is attached to the sensor circuit board for this measurement. 

%%Sensor_evaluation_setup_for_temperature_sensitivity_measurements.png%%

Figure \ref{Sensor_evaluation_setup_for_temperature_sensitivity_measurements.png} represents these modifications in detail. These changes makes it possible to accurately determine the sensors (+ic) temperature.
The temperature measuring device *7055BT* can be analysed using a (+pc) interface.
The controller of the temperature chamber can also be programmed via a (+pc) interface and a target temperature can be specified.
With this setup, it is possible to automatically acquire measured values from the sensors under controlled temperature conditions.

The field of permanent magnets is highly temperature-dependent and can lose its magnetisation at higher temperatures (typically *>=80$^{\circ}$* for non-high-quality *Type-N* magnets [@GKT16]).
The temperature range is selected so that it lies within a sufficient range for typical subsequent measurement tasks.
The same procedure is used as for the *Linearity* measurement in chapter \ref{sensor-characterisation-linearity}, except that instead of moving the linear axis, the temperature of the temperature chamber is systematically increased from *20$^{\circ}$* to *50$^{\circ}$*.
Between each of these temperature changes, the system is given a additional waiting time of *30* minutes after reaching the target temperature.



### Temperature Sensitivity Analysis

%%Sensor_temperature_sensitivity_evaluation_results_for_TLV493D_and_MMC5603NJ.png%%

Figure \ref{Sensor_temperature_sensitivity_evaluation_results_for_TLV493D_and_MMC5603NJ.png} represents the measured data as a plot with the temperature measured by the measuring devices on the X-axis and the sensor measured value on the Y-axis. The ideal baseline is also shown as a red line.
It can be seen that the *MMC5603NJ* shows a straight-line drop in the measured field strength with increasing temperatures. However, this is very constant with a value of *-2 $\mu$T / $^{\circ}$C* and is therefore predictable.

The graph of the *TLV493d* is significantly steeper with a gradient of -5.13 $\mu$T / $^{\circ}$C, and it is also not as linear as the *MMC5603NJ*; there are clear jumps in the gradient. However, the total change between the temperature regions of 175$\mu$T is less than that of the *MMC5603NJ* with *70$\mu$T*, if the total measurement range of the sensors is also considered.
In the evaluation (see Figure \ref{Sensor_temperature_sensitivity_evaluation_results_for_TLV493D_and_MMC5603NJ.png}) a linear function is also calculated using curve fitting to determine the temperature coefficients of the sensors. This makes it possible to compensate these deviations based on the ambient temperature during the software calibration.

\newpage

## Result Analysis

%%Overview_of_all_characterised_sensor_properties.csv%%

Table \ref{Overview_of_all_characterised_sensor_properties.csv} represents a summary of all recorded and analysed measured values of the two characterised sensors *TLV493D* and *MMC5603NJ*.
It can be clearly seen that these differ significantly by a factor of *x10*.

The *TLV493D* performs in noise measurements worse than specified in the data sheet (*100$\mu$T* instead of *175$\mu$T*), but the large (+dr), which fulfils the required specifications from chapter *Research Question* in chapter \ref{research-question-and-approach}, must be considered here, which is not met by the *MMC5603NJ*.

The *MMC5603NJ* can be used directly without additional software calibration for measuring permanent magnets. Even without additional measurement averaging, very precise measurement results can be achieved, which achieve a measurement accuracy of less than *1000 (+ppm)*.
Due to the limited (+dr) of around *±3mT*, direct measurement of stronger magnets is not possible using the *MMC5603NJ*. The *N45 12x12x12mm* magnets used in the application typically have a field strength of around *100mT* at a distance of *10mm* which is more than the *MMC5603NJ* can measure.
The *TLV493D*, on the other hand, is able to measure these ranges with a specified (+dr) of *±130mT*, but does not achieve the required accuracy due to strong noise and steep temperature coefficients.
In the following chapter, recommendations for action are defined, which are derived from the analysis results.

### Recommendation for Action

After analysing the measurement results, it can be seen that the selected sensors are only partially suitable for the previously defined requirements.

In general, further digital and analogue sensors should be characterised with the developed framework.
In particular, the use of analogue magnetic field sensors with separate bias voltage should be evaluated, as a simplified characterisation procedure can be applied due to the lack of a base offset.

In the following, alternative methods for sensor adaptions will be described that the sensors can still be used for these measurements.

#### Permanent Magnet Characterisation

Both sensors are suitable for precisely measuring and quantifying magnetic fields.
To ensure the linearity of the sensors, compensation can be performed using a defined measurement setup. This concept has already been successfully implemented in chapter *Example Sensors* \ref{example-sensors}, in particular *1D: Single Sensor* \ref{d-single-sensor}, and proven to be functional in earlier chapters.

The *MMC5603NJ* sensor has a limited measuring range, which means that it may not the best choice considering these application parameters.
However, this limitation also makes it possible to compare relative magnetic field strengths with each other.
Furthermore, by using software, it is possible to achieve absolute comparability of the magnetic fields by scaling the measured values accordingly.
This is shown in the chapter *Use Case Evaluation* \ref{use-case-evaluation} by comparing and sorting different permanent magnets using these sensors.

Overall, both the *TLV493D* and the *MMC5603NJ* offer possibilities for characterising permanent magnets. By using suitable hardware setup, software calibration methods and precise characterisations can be carried out.

#### Homogeneity Measurement of a Halbach Ring-based B0 Field

The *MMC5603NJ* cannot be used for this due to the limited value range. The method of increasing the distance, as with permanent magnet characterisation, cannot be used as the magnet is located within a limited space in the Halbach ring.

In contrast, the *TLV493D* has too much noise, so that the measured values cannot be used directly without post-processing. With software calibration, it is possible to reduce the noise to below *50$\mu$T* with the *TLV493D*. 
As a test, several further measurement runs are carried out, which achieved results for the sensor noise of *71$\mu$T* to *41$\mu$T* when averaging *100* to *1000* measured values.
However, further measurement runs must be carried out to verify these results.

In general, post-processing of the measurements should, include temperature compensation with a separate temperature sensor, especially in the case of changing measurement conditions (e.g. movement of the sensor in the *B0* field).

# Conclusion and Discussion

## Conclusion

This thesis describes the development of a (+mrp) Python library that can be used to efficiently process data from magnetic field sensors from acquisition to analysis.
To ensure a practical application and allow users to acquire their own magnetic field data directly, a low-cost and easily reproducible hardware is also developed.
The hardware is based on widely used consumer magnetic field sensors and low-cost microcontrollers, enabling an easily expandable and applicable solution for measuring magnets with repeatable accuracy.
Special attention is paid to the expandability by the user. Interchangeable modules allow the user to develop their own analysis algorithms without having to design everything from scratch. The software framework is evaluated on the basis of the previously defined use cases.
A user-defined sorting algorithm is implemented and integrated into the framework. The result is a list of the magnets that deviate least from the magnetic strength.

The result is successfully verified by means of manual checks for various other series of measurements. In this way, extensibility and customisability are also successfully demonstrated during the software evaluation.
This underlines the power of the developed framework and shows that it is not only effective in processing magnetic field sensor data, but also provides a flexible platform for the implementation of user-specific analyses.
Subsequently, the developed framework is used to automatically characterise various magnetic field sensors.
For this purpose, the developed pipeline feature of the software is used to determine various sensor characteristics, including background noise, temperature coefficients and linearity.

The evaluation of the measurement data showed that the selected sensors only partially fulfil the defined requirements. 
The *TLV493D* and *MMC5603NJ* sensors are both suitable for characterising permanent magnets and enable linearity compensation with a defined measurement setup. Although the *MMC5603NJ* has a limited measuring range, it can still be used for relative comparisons of permanent magnets without additional devices and without software calibration.
It also has a minimal long-term background noise.
Absolute comparability can be achieved by prior software calibration and using reference measurements, making it an ideal sensor for the task of characterising permanent magnets in field tests.

The *MMC5603NJ* is not recommended for measuring the homogeneity of a *50$\mu$T* *B0* field on a Halbach ring basis with an accuracy of better than *1000 (+ppm)* due to its limited measuring range. The *TLV493D* sensor, on the other hand, has too much noise.
It has been shown that this can be compensated for by software calibration and long-term averaging of measured values. Despite constant ambient conditions, temperature compensation is necessary for this sensor.
Due to the large measuring range and the constant linearity, no software compensation is necessary.
These results show that the analysed sensors are generally suitable for the application scenarios using the developed (+mrp) library with some limitations.

Based on these results, it is proposed to characterise further digital and analogue sensors, in particular analogue magnetic field sensors with separate bias voltage.
Alternative methods for sensor adaptation are described in order to be able to use these widely used consumer magnetic field sensors for the characterisation of neodymium magnet-based permanent magnets. 


## Outlook

With this version of the framework, a solid basis has been created that contains all the necessary functions to solve various problems in the acquisition and processing of magnetic fields. Easy-to-assemble measurement hardware has created an easy-to-use platform for the characterisation of permanent magnets, for example. An exemplary characterisation of the magnetic field sensors used allows the possible areas of application for these to be narrowed down. The framework has already been published in a first stable version, but extensions and improvements are still necessary.
The stable version is also distributed via a package registration and can therefore be quickly evaluated by new users. 
In addition, further user experience and actual measurements under real laboratory conditions on (+mri) B0 field magnets are still missing. This is limited by the currently restricted selection of characterised sensors. The aim for the next revision of the hardware and software framework is therefore to support additional magnetic field sensors. The current restriction to purely digital sensor interfaces is also to be extended to analogue interfaces. This will open up the use of a wide range of magnetic field sensors. It is also possible to integrate high-resolution magnetic field probes based on NMR samples, which can cover measurement errors of less than *10nT* in fields of more than *1T* [@DBN08].
Another possibility already supported by the software, but for which hardware development is still necessary, is 2D arrays of magnetic field sensors to display fields on a surface[@CP16]. This means that deviations can also be visualised graphically without physically moving the sensors such as in the implemented *3D: Full Sphere* \ref{d-full-sphere} sensor. In addition, larger areas or volumes, for example in a large *B0* field, can be measured more quickly.