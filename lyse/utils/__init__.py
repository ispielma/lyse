#####################################################################
#                                                                   #
# /utils.py                                                         #
#                                                                   #
# Copyright 2013, Monash University                                 #
#                                                                   #
# This file is part of the program lyse, in the labscript suite     #
# (see http://labscriptsuite.org), and is licensed under the        #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################
"""Lyse API common utilities
"""


from pathlib import Path

# labscript imports
from labscript_utils.labconfig import LabConfig

LYSE_DIR = Path(__file__).resolve().parent.parent

# Open up the lab config
LABCONFIG = LabConfig()

# get port that lyse is using for communication
try:
    LYSE_PORT = int(LABCONFIG.get('ports', 'lyse'))
except Exception:
    LYSE_PORT = 42519

def importer(splash):
    """
    Import modules for the first time for the exclusive reason to show the splash screen
    """

    splash.update_text('importing standard library modules')

    # stdlib imports
    import time
    import sys
    import queue
    import warnings
    import signal

    # 3rd party imports:
    splash.update_text('importing numpy')
    import numpy as np
    splash.update_text('importing pandas')
    import pandas

    # Labscript imports
    splash.update_text('importing zprocess (zlog and zlock must be running)')
    import labscript_utils.ls_zprocess

    splash.update_text('importing labscript suite modules')
    import labscript_utils.labconfig
    import labscript_utils.setup_logging
    import labscript_utils.qtwidgets.outputbox
    import labscript_utils 

    # qt imports
    splash.update_text('importing qt modules')
    import qtutils.qt
    import qtutils.qt.QtCore
    import qtutils
    import qtutils.icons 

    # needs to be present so that qtutils icons referenced in .ui files can be resolved.  Since this is 
    # magical is should not be implemented in this way.

    # Lyse imports
    splash.update_text('importing core Lyse modules')
    import lyse.utils
    import lyse.utils.gui
    import lyse.routines
    import lyse.communication