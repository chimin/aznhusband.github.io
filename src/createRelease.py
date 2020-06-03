import sys
import re
import os
import hashlib
from zipfile import ZipFile, ZIP_DEFLATED

try:
    new_version = sys.argv[1]
except IndexError:
    print 'Enter a new release version'
    new_version = input()

print 'New Release Version %s' % new_version

index_html = open('../index.html', 'r')
lines = index_html.readlines()
index_html.close()

for index, line in enumerate(lines):
    match = re.search('<h1>Current Version: (.*)</h1>', line)
    if match is not None:
        current_version = match.group(1)
        lines[index] = line[:match.start(1)] + new_version + line[match.end(1):]
        break

print 'Current Release: %s ' % current_version
if current_version is None:
    raise 'Unable to retrieve current version'

index_html = open('../index.html', 'w')
index_html.writelines(lines)
index_html.close()

zip_file = ZipFile('../plugin.video.icdrama/plugin.video.icdrama-%s.zip' % new_version, 'w', ZIP_DEFLATED)
for root, dirs, files in os.walk('plugin.video.icdrama'):
    for file in files:
        path = os.path.join(root, file)
        zip_file.write(path, path)
zip_file.close()

os.chdir('..\\plugin.video.icdrama')
os.system('python ..\\src\\kodidirlist.py > index.html')

os.chdir('..')
addons_xml = open('addons.xml', 'r')
addons_xml_md5 = open('addons.xml.md5', 'w')
addons_xml_md5.write(hashlib.md5(addons_xml.read()).hexdigest())
addons_xml_md5.close()
addons_xml.close()