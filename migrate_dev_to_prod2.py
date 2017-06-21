"""
Script to migrate softwares in dev environment to prod environment.

To run this script, copy qt_ifw_path.template.py to qt_ifw_path.py,
and modify the path to fit your environment.
"""

from datetime import datetime
import subprocess
import os
from qt_ifw_path import QT_IFW_PATH

def copy_dev_src():
    """Copy dev_src folder to prod_src folder"""

    cmd = 'svn cp dev_src/packages prod_src/packages'
    subprocess.check_output(cmd)
    print('prod_src copied')

def copy_dev():
    """Copy folders under dev folder prod folder"""

    items = os.listdir('dev')
    for item in items:
        fullitem = os.path.join('dev', item)
        if not os.path.isdir(fullitem):
            continue

        cmd = 'svn cp dev/' + item + ' prod/' + item
        subprocess.check_output(cmd)

    print('prod copied')

def modify_qs():
    """Modify iRIC GUI installscript.qs"""

    qs_path = 'prod_src/packages/gui.prepost/meta/installscript.qs'
    f = open(qs_path, 'r')
    content = f.read()
    f.close()

    content = content.replace('(develop)', '')

    f = open(qs_path, 'w')
    f.write(content)
    f.close()

    print('iRIC GUI installscript.qs modified')

def build_repository():
    """Run repogen to build files for online update"""

    repogen = QT_IFW_PATH + '\\bin\\repogen.exe'
    cmd = repogen + ' -p prod_src\\packages --update --include gui.prepost prod'
    subprocess.check_output(cmd)
    print('Online update repository updated')

def build_installer():
    """Run binarycreator to build offline installer"""

    binc = QT_IFW_PATH + '\\bin\\binarycreator.exe'
    now = datetime.now()
    installer_name = 'iRIC_Installer_' + now.strftime('%y%m%d')

    cmd = binc + ' --offline-only -c prod_src/config/config.xml'
    cmd += ' -p prod_src\\packages prod\\' + installer_name

    subprocess.check_output(cmd)


#copy_dev_src()
#copy_dev()
#modify_qs()
#build_repository()
build_installer()
