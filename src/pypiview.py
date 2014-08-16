# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of the easydev software
#
#  Copyright (c) 2011-2014
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.com>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  Website: https://www.assembla.com/spaces/pyeasydev/wiki
#  Documentation: http://packages.python.org/easydev
#
##############################################################################
# $:Id $
"""Utilities to lookup into pypi stats.


.. warning:: requires pandas and vanity packages
"""
import datetime
import sys
import vanity
import pandas as pd
import pylab


__all__ = ["PYPIView"]


class PYPIView(object):
    """Plot number of downloads versus time of a PYPI package.

    .. plot::
        :include-source:
        :width: 80%

        from pypiview import PYPIView
        p = PYPIView(["requests"], verbose=False)
        p.plot(logy=True)
        


    The attribute :attr:`df` contains the dataframe with all results.
    The attribute :attr:`tss` contains the individual TimeSeries for each package
    as returned by :meth:`get_data_one_package`.

    """
    def __init__(self, packages, verbose=True):
        """.. rubric:: Constructor

        :param packages: list of packages or single package
        :param bool verbose: print some information.

        """
        if isinstance(packages, (str)):
            packages = [packages]
        self.verbose = verbose
        self.tss = []

        for package in packages:
            print("Downloading data for {0} package".format(package))
            ts = self.get_data_one_package(package)
            self.tss.append(ts.to_frame())

        self.df = pd.concat(self.tss)
        self.df = self.df.sort_index()
        if self.verbose:
            print(self.df)
         
    def get_data_one_package(self, package):
        """Return the data for one package
        
        :param str pacakge: a single package name
        :return: a Pandas time series.

        """


        releases = list(vanity.package_releases([package]))[0][1]
        downloads = []
        times = []
        data = list(vanity.release_data([package]))
        for i in range(0, len(releases)):
            if len(data[i][0]):
                dtime = data[i][0][0]['upload_time']
                download = data[i][0][0]['downloads']
                tt = dtime.timetuple()
                times.append([tt[0], tt[1], tt[2]])
                downloads.append(download)
        df = pd.Series(downloads, [datetime.datetime(*x) for x in times], 
            name=package)
        df = df.sort_index()
        return df

    def plot(self, lw=2, fontsize=16, marker='o', logy=False):
        """plot the number of downloads

        The data used is the data stored in the :attr:`df` attribute.

        :param int lw: width of the curves
        :param int fontsize: fontsize used in titles
        :param marker: 
        :param bool logy: set y-axis to logarithmic scale


        #. first plot shows the cumulative downloads
        #. second plot shows the individual downloads

        .. plot::

            from pypiview import PYPIView
            p = PYPIView("requests", verbose=False)
            p.plot()

        """

        self.df.cumsum().plot(marker=marker, lw=lw, fontsize=fontsize, logy=logy)
        pylab.legend()
        pylab.title("Cumulative downloads", fontsize=fontsize)

        self.df.plot(marker=marker, lw=lw, fontsize=fontsize, logy=logy)
        pylab.legend()
        pylab.title("Downloads of each release")



def Help():
    print("T.C, Aug 2014\n")
    print("Usage: \n")
    print("\tpypiview [pkgnames]\n")
    print("[pkgnames] is a list of one or several packages to be found on pypi\n")

    print("Other options are\n")
    print("You can also add --verbose option")
    print("plots can be tuned with --fontsize <number>")
    print("plots can be tuned with --lw <number> , to set the line width of the curves")
    print("plots can be tuned with --logy optoin to set y-scale to a log scale")

    print("\nExamples:\n")
    print("    pypiview requests --verbose --logy --lw 2 --fontsize 16\n")
    print("    pypiview setuptools distribute --verbose --logy --lw 2 --fontsize 16\n")

def main(show=True):
    """The main executable"""
    args = sys.argv

    if "--help" in args:
        Help()
        return

    # could use argparse but there are just a few parameters.
    if len(args)<2:
        Help()
        return

    if "--verbose" in args:
        verbose = True
        index = args.index('--verbose')
        args.pop(index)
    else:
        verbose = False

    if "--logy" in args:
        logy = True
        index = args.index('--logy')
        args.pop(index)
    else:
        logy = False

    if "--fontsize" in args:
        index = args.index("--fontsize")
        fontsize = args[index+1]
        args.pop(index)
        args.pop(index)
    else:
        fontsize = 16

    if "--lw" in args:
        index = args.index("--lw")
        lw = args[index+1]
        args.pop(index)
        args.pop(index)
    else:
        lw = 2

    print(args[1:])
    p = PYPIView(args[1:], verbose=verbose)
    p.plot(lw=lw, fontsize=fontsize, logy=logy)
    if show: pylab.show()



if __name__ == "__main__":
    main()
