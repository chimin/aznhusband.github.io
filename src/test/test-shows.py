import sys
import os

sys.argv.append(0)
sys.dont_write_bytecode = True

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

sys.path.append('../plugin.video.icdrama')
sys.path.append('../plugin.video.icdrama/lib')
sys.path.append('stub')
sys.path.append('lib/script.module.resolveurl/lib')

from urlparse import urljoin
from lib.scrapers import shows
from config import base_url

list = shows(urljoin(base_url, '/hk-drama'))
for item in list:
    print str(item)