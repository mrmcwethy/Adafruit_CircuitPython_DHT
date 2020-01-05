
Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-dht/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/dht/en/latest/
    :alt: Documentation Status


.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://discord.gg/nBQh6qu
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_DHT/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_DHT/actions
    :alt: Build Status

CircuitPython support for the DHT11 and DHT22 temperature and humidity devices.

Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-dht/>`_. To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-dht

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-dht

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install adafruit-circuitpython-dht

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

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
