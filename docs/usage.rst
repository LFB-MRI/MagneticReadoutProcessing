Usage
=====

.. _installation:

Installation
------------

 To use MagneticReadoutProcessing library, first install it using the setup script:

.. .. code-block:: console
..    # RELEASE
..    $ git clone https://github.com/LFB-MRI/MagneticReadoutProcessing ./MagneticReadoutProcessing
..    $ cd ./MagneticReadoutProcessing
..    $ python ./setup.py install




..  Creating recipes
.. ----------------

.. To retrieve a list of random ingredients,
.. you can use the ``lumache.get_random_ingredients()`` function:

.. .. autofunction:: lumache.get_random_ingredients

.. The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
.. or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
.. will raise an exception.

.. .. autoexception:: lumache.InvalidKindError

.. For example:

.. >>> echo "." #import lumache
.. >>> echo "b" 
.. ['shells', 'gorgonzola', 'parsley']

