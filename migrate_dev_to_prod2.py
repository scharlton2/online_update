import subprocess
import os

cmd = 'svn cp dev_src/packages prod_src/packages'
# print(cmd)
subprocess.check_output(cmd)

items = os.listdir('dev')
for item in items:
    fullitem = os.path.join('dev', item)
    if not os.path.isdir(fullitem):
        continue

    cmd = 'svn cp dev/' + item + ' prod/' + item
    # print(cmd)
    subprocess.check_output(cmd)

cmd = 'svn rm prod/Updates.xml'
cmd = 'svn cp dev/Updates.xml prod/Updates.xml'
# print(cmd)
subprocess.check_output(cmd)
