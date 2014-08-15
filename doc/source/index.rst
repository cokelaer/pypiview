

#############################
PYPIView documentation
#############################


**PYPIView** package provides a simple class to plot the number of downloads of a Pypi package (or several). The download counting is perfomed by the `vanity <https://pypi.python.org/pypi/vanity/2.0.3>`_ package. The plotting is performed with the  `Pandas <http://pandas.pydata.org/>`_ package.

Installation
###################

::

    pip install pypiview


Quick Start
##################


Nothing complicated since there is just one class provided. You can look at a single package or several packages. First, we create an instance telling what package we are instereted in::


    from pypiview import PYPIView
    p = PYPIView("requests")

Then, we call the plotting method. Here, we use the a logarithm scale because requests package is a popular one::

    p.plot(logy=True)



.. plot::
    :width: 80%

    from pypiview import PYPIView
    p = PYPIView("requests")
    p.plot(logy=True)

Alternatively, you can look at several packages at the same time, which is handy for comparison:


.. plot::
    :width: 80%

    from pypiview import PYPIView
    p = PYPIView("requests")
    p.plot(logy=True, lw=1, fontsize=20)


**PYPIview** provides also a command line argument called pypiview. Usage is as follows::

    pypiview <list of packages separated by spaces> --verbose --logy --lw 2 --fontsize 16 

Example::

    pypiview requests --verbose --logy --lw 2 --fontsize 16

    pypiview setuptools distribute --verbose --logy --lw 2 --fontsize 16


 






Reference Guide
##################


.. toctree::
    :maxdepth: 2
    :numbered:

    references

