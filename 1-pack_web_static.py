#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    local("mkdir -p versions")
    date = datetime.now()
    date_now = date.strftime("%Y%m%d%H%M%S")

    file_name = "web_static_" + date_now + ".tgz"
    # Compress files into archive
    arch_file = local("tar -cvzf versions/{} web_static".format(file_name))
    if arch_file.succeeded:
        return "versions/{}".format(file_name)
    else:
        return None
