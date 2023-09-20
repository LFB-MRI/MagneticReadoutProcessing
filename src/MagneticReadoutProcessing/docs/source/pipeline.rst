UDPP - User Defined Processing Pipeline
#######################################

After usage of the CLI and taking some measurements of the magnets, its time ro process them.
One solution is to use a Jupyter Notebook to call the ``MRP`` functions directly or using ``UDPP`` interface.
Here its possible to define a data analysis pipeline (as such in CI pipelines) and run them like CLI commands.


Installation
************

.. code-block:: bash

    $ git clone https://github.com/LFB-MRI/MagneticReadoutProcessing ./MagneticReadoutProcessing
    $ cd ./MagneticReadoutProcessing
    $ pip3 install -r requirements.txt


    # RUNNING THE CLI USING VENV (if library is not installed on system)
    $ ./venv/bin/python3.9 ./udpp/udpp.py --help


.. note::
    In order to allow direct running of the examples below, the ``venv`` is used.
    So all cli commands are changed to: ``./venv/bin/python3.9 ./udpp/udpp.py`` instead of ``python3 ./udpp/udpp.py``.


Pipeline Definition
*******************

