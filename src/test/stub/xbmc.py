import time

LOGDEBUG = 0
LOGERROR = 4
LOGFATAL = 6
LOGINFO = 1
LOGNONE = 7
LOGNOTICE = 2
LOGSEVERE = 5
LOGWARNING = 3

def executeJSONRPC(command):
    return '{}'

def sleep(time):
    time.sleep(time / 1000)

def log(msg, level = LOGDEBUG):
    print(msg)

def translatePath(path):
    print('xbmc.translatePath ' + path)
    return 'kodi/' + path

def getCondVisibility(key):
    return 0