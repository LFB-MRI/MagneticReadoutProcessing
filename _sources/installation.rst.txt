Installation
############

.. note::
   There are further detailed examples in the ``test`` folder.
   In general there is a separate test file for each submodule.


.. note::
   This is a Python3 library!


Release
=======

.. code-block:: console

    $ pip3 install MagneticReadoutProcessing



Development
===========

For now, the suggested development method is to copy the ``MagneticReadoutProcessing`` folder into your Python project folder.
There are some other packages required which are listed in the ``requirements.txt``.
To install them use ``$ pip3 install -r requirements.txt`` command.

.. code-block:: console

    $ git clone https://github.com/LFB-MRI/MagneticReadoutProcessing ./MagneticReadoutProcessing
    $ cd ./MagneticReadoutProcessing/src/MagneticReadoutProcessing
    $ pip install -e .


.. note::
   For further development, ``build``, ``run``, ``docs``, ``test`` configurations for PyCharm are included too.
   Just open the ``MagneticReadoutProcessing`` as project in the IDE (personal, edu or professional).



Distribute package
==================

To build the library as a packe, the python module build command can be used.
The result can be found in the ``dist`` folder.
In the default configuration (see ``setup.py``), this library, the CLI and test scripts are included too.

.. code-block:: console
    
    $ git clone https://github.com/LFB-MRI/MagneticReadoutProcessing ./MagneticReadoutProcessing
    $ cd ./MagneticReadoutProcessing/src/MagneticReadoutProcessing/
    $ python3 -m build


Tests
=====

Tests are implemented for all library related functions.
These are grouped by and are locates in the ``tests`` folder.
``unittest`` and ``pytest`` is used to tun these tests.

.. note::
    There are also tests included which need be run against a connected sensor hardware.
    These have the file-prefix ``hwtest_``.
    To disable hardware dependent testing, edit the ``test_config.ini`` and set ``enable_hardware_required_tests`` to ``0``.

.. code-block:: console
    
    $ git clone https://github.com/LFB-MRI/MagneticReadoutProcessing ./MagneticReadoutProcessing
    $ cd ./MagneticReadoutProcessing/src/MagneticReadoutProcessing/
    $ cd ./tests
    # RUN ALL TESTS
    $ python3 -m unittest discover
    # RUN MODULE SPECIFIC TEST






Documentation
=============

This documentation is build using the ``sphinx`` framework and all source files are located in the ``docs`` folder.

.. code-block:: console

    $ git clone https://github.com/LFB-MRI/MagneticReadoutProcessing ./MagneticReadoutProcessing
    $ cd ./MagneticReadoutProcessing/src/MagneticReadoutProcessing/
    $ cd ./docs
    $ sphinx-build -b html source build


