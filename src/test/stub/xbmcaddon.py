class Addon:

    def __init__(self, name = ''):
        self.name = name

    def getAddonInfo(self, key):
        if key == 'name':
            return self.name
        elif key == 'version':
            return '10.0'
        elif key == 'profile':
            return 'default'
        elif key == 'path':
            return '.'
        else:
            raise

    def getSetting(self, key):
        if key.endswith('_enabled'):
            return 'true'
        else:
            return ''

    def setSetting(self, key, value):
        print "xmbcaddon.setSetting " + key + " " + value
        pass

    def openSettings(self):
        raise

    def getLocalizedString(self, id):
        return str(id)
