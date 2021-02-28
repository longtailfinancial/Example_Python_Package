"""
Root level package init
"""

import pkg_resources
__version__ = pkg_resources.require("example_pkg")[0].version
