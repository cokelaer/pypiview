PYPIView
#########

.. image:: https://badge.fury.io/py/pypiview.svg
    :target: https://badge.fury.io/py/pypiview.svg


**PYPIView** package provides a simple class to visualise the number of downloads of a Pypi package (or several packages). The information of downloads is retrieved via the `vanity <https://pypi.python.org/pypi/vanity/2.0.3>`_ package. The plotting is performed with the  `Pandas <http://pandas.pydata.org/>`_ package.

Installation
==============

::

    pip install pypiview


Usage
========

::

    from pypiview import PYPIView
    p = PYPIView("requests")
    p.plot(logy=True)



.. image:: http://pythonhosted.org//pypiview/_images/index-1_00.png
    :target: http://pythonhosted.org//pypiview/_images/index-1_00.png



See the `online <http://pythonhosted.org//pypiview/>`_ documentation for details.
