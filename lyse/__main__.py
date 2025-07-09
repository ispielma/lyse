#####################################################################
#                                                                   #
# /__main__.py                                                      #
#                                                                   #
# Copyright 2013, Monash University                                 #
#                                                                   #
# This file is part of the program lyse, in the labscript suite     #
# (see http://labscriptsuite.org), and is licensed under the        #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################
"""Top level Lyse GUI
"""
import os
import labscript_utils.excepthook

# Associate app windows with OS menu shortcuts, must be before any GUI calls, apparently
import desktop_app
desktop_app.set_process_appid('lyse')

# Splash screen
from labscript_utils.splash import Splash
splash = Splash(os.path.join(os.path.dirname(__file__), 'lyse.svg'))
splash.show()

splash.update_text('importing standard library modules')
# stdlib imports
import sys

from qtutils.qt import QtCore, QtWidgets

import lyse.main_window

if __name__ == "__main__":

    qapplication = QtWidgets.QApplication.instance()
    if qapplication is None:
        qapplication = QtWidgets.QApplication(sys.argv)
    qapplication.setAttribute(QtCore.Qt.AA_DontShowIconsInMenus, False)

    app = lyse.main_window.Lyse(qapplication, splash)
    
    splash.hide()
    qapplication.exec_()

    # Shutdown the webserver.  Should be managed by the main window
    app.server.shutdown()
