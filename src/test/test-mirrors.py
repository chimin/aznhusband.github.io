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

list = mirrors('http://www1.hkdrama.to/watch-online-armed-reaction-2021-episode-01-274007.html')
print list