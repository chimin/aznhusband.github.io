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

from lib.scrapers import mirrors
from config import base_url

list = mirrors('http://www1.adrama.to/watch-online-the-exorcist-s-2nd-meter-episode-25-end-238373.html')
print list