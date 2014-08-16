__version__ = "$Rev: 10 $"
import pkg_resources
try:
    version = pkg_resources.require("pypiview")[0].version
except Exception:
    version = __version__


from pypiview import *
