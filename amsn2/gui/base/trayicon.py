
class aMSNTrayIcon(object):
    """ This interface represents the tray icon. """

    def __init__(self, amsn_core):
        """
        @type amsn_core: aMSNCore
        """

        pass

    def show(self):
        raise NotImplementedError

    def hide(self):
        raise NotImplementedError

    #setMenu, blink, ... ?
