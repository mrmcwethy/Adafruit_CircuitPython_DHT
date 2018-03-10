
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-dht/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/dht/en/latest/
    :alt: Documentation Status


.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://travis-ci.org/adafruit/Adafruit_CircuitPython_DHT.svg?branch=master
    :target: https://travis-ci.org/adafruit/Adafruit_CircuitPython_DHT
    :alt: Build Status

CircuitPython support for the DHT11 and DHT22 temperature and humidity devices.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
==============

Hardware Set-up
----------------

The DHT11 and DHT22 devices both need a pull-resistor on the data signal wire.  
This resistor is in the range of 1k to 5k.  Please check your device datasheet for the 
appropriate value.

Basics
-------

Of course, you must import the library to use it:

.. code:: python

    import adafruit_dht

The DHT type devices use single data wire, so import the board pin

.. code:: python

    from board import <pin>

Now, to initialize the DHT11 device:

.. code:: python

    dht_device = adafruit_dht.DHT11(<pin>)

OR initialize the DHT22 device:

.. code:: python

    dht_device = adafruit_dht.DHT22(<pin>)

Read temperature and humidity
------------------------------

Now get the temperature and humidity values

.. code:: python

    temperature = dht_device.temperature
    humidity = dht_device.humidity

These properties may raise an exception if a problem occurs.  You should use try/raise 
logic and catch RuntimeError and then retry getting the values after 1/2 second.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_DHT/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Building locally
================

To build this library locally you'll need to install the
`circuitpython-build-tools <https://github.com/adafruit/circuitpython-build-tools>`_ package.

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install circuitpython-build-tools

Once installed, make sure you are in the virtual environment:

.. code-block:: shell

    source .env/bin/activate

Then run the build:

.. code-block:: shell

    circuitpython-build-bundles --filename_prefix adafruit-circuitpython-veml6070 --library_location .

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.

