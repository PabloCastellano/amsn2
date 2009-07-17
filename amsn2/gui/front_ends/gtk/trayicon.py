from amsn2.gui import base
import gtk

class aMSNTrayIcon(base.aMSNTrayIcon):
    
    def __init__(self, amsn_core):

        self._amsn_core = amsn_core
        self._tray = gtk.StatusIcon()
        #What if current WM doesn't support systrays??
        
        self._tray.set_from_file("amsn2/themes/default/images/amsn2icon.png")     
        self._createTrayMenu()

    def show(self):
        self._tray.set_visible(True)
        
    def hide(self):
        self._tray.set_visible(False)
        
    def _make_menu(self, event_button, event_time, icon):
        menu = gtk.Menu()
        quitItem = gtk.MenuItem("Quit")
        quitItem.show()
        menu.append(quitItem)
        menu.popup(None, None, gtk.status_icon_position_menu, event_button,event_time, icon)
        
    def _on_right_click(self, icon, event_button, event_time):
        self._make_menu(event_button, event_time, icon)
        
    def _createTrayMenu(self):
        self._tray.connect('popup-menu', self._on_right_click)
        
