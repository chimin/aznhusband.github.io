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

from lib.scrapers import versions
from config import base_url

list = versions('http://www1.adrama.to/hk-drama/6095-the-exorcist-s-2nd-meter/')
print list