import subprocess
import os

items = os.listdir('prod_src/packages')
for item in items:
    if item == 'gui.prepost':
        continue

    fullitem = 'prod_src/packages/'+ item

    cmd = 'svn rm ' + fullitem
    subprocess.check_output(cmd)

items = os.listdir('prod')
for item in items:
    fullitem = 'prod/' + item
    if not os.path.isdir(fullitem):
        continue
    if item == 'gui.prepost':
        continue

    cmd = 'svn rm ' + fullitem
    # print(cmd)
    subprocess.check_output(cmd)
