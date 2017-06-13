"""
Script to build installer and repository, with updated iRIC GUI.

Please note that this script only update iRIC GUI. When you updated
other solvers, please do not use this to build installer and repository.

To run this script, copy qt_ifw_path.template.py to qt_ifw_path.py,
and modify the path to fit your environment.
"""

import subprocess
from datetime import datetime
import xml.etree.ElementTree as ET
from qt_ifw_path import QT_IFW_PATH

# Qt installer framework path

def update_version_number():
    """
    Update version number of iRIC GUI
    This function is not finished, and not used now.
    """

    def_path = 'packages/gui.prepost/data/definition.xml'
    tree = ET.parse(def_path)
    # tree.register_namespace('', 'www.iric.net/GuiDefinition/1.0')
    root = tree.getroot()
    version = root.attrib['version']

    (major, minor, fix, release) = version.split('.')
    # update fix number
    fix = str(int(fix) + 1)
    # update release number
    release = str(int(release) + 1)

    newversion = ".".join([major, minor, fix, release])

    print ('new version: ' + newversion)
    root.attrib['version'] = newversion

    # @TODO IMCOMPLETE!

def build_installer():
    """
    Run binarycreator to build offline installer
    """

    print('building installer...')

    binc = QT_IFW_PATH + '\\bin\\binarycreator.exe'
    now = datetime.now()
    installer_name = 'iRIC_Installer_' + now.strftime('%y%m%d')

    cmd = binc + ' --offline-only -c config/config.xml'
    cmd += ' -p packages ..\\prod\\' + installer_name

    subprocess.check_output(cmd)

def build_repository():
    """
    Run repogen build files for online update
    Note that this only update iRIC GUI.
    """

    print('updating repository...')

    repogen = QT_IFW_PATH + '\\bin\\repogen.exe'
    cmd = repogen + ' -p packages --update --include gui.prepost ..\\dev'

    subprocess.check_output(cmd)

# update_version_number()
#build_installer()
build_repository()

print('finished')
