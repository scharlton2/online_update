import subprocess
import os

cmd = 'svn rm prod_src/packages'
# print(cmd)
subprocess.check_output(cmd)

items = os.listdir('prod')
for item in items:
    fullitem = os.path.join('prod', item)
    if not os.path.isdir(fullitem):
        continue

    cmd = 'svn rm prod/' + item
    # print(cmd)
    subprocess.check_output(cmd)
