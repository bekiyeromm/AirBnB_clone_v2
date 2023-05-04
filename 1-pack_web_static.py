#!/usr/bin/python3
"""
Fabric script that generates a tgz archive from the contents of the web_static
folder of the AirBnB Clone repo
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generates a tgz archive"""
    local("mkdir -p versions")
    date_now = datetime.now()
    time_format = date_now.strftime("%Y%m%d%H%M%S")
    file_name = = "web_static_" + time_format + ".tgz"
    """do file compression"""
    arch_file = local("tar -cvzf versions/{} web_static".format(file_name))
    if arch_file.failed:
        return None
    else:
        return ("versions/{}".format(file_name))
