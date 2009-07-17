from amsn2.gui import base
from PyQt4 import QtGui

class aMSNTrayIcon(base.aMSNTrayIcon):
    
    def __init__(self, amsn_core):

        self._amsn_core = amsn_core
        self._tray_support = QtGui.QSystemTrayIcon.isSystemTrayAvailable()

        if self._tray_support:
            icon = QtGui.QIcon("amsn2/themes/default/images/amsn2icon.png")     
            self._tray = QtGui.QSystemTrayIcon(icon)
            self._createTrayMenu()
            self.show()
        else:
            print "Support for TrayIcon: False"
            self._tray = None


    def show(self):
        if self._tray_support:
            self._tray.setVisible(True)
        
    def hide(self):
        if self._tray_support:
            self._tray.setVisible(False)

    def _createTrayMenu(self):
        #FIXME: Menus won't popup, I don't know why

        #quitAction = QtGui.QAction("Quit", self._amsn_core._loop.app)
        quitAction = QtGui.QAction("Quit", None)

        trayIconMenu = QtGui.QMenu()
        trayIconMenu.addAction(quitAction)

        self._tray.setContextMenu(trayIconMenu)

