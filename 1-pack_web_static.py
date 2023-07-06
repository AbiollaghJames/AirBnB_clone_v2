#!/usr/bin/python3
"""
  A Fabric script that generates a .tgz
  archive from the contents of the web_static folder
"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """ func to compress file """
    local("mkdir -p versions")
    compressed = local("tar -czvf versions/web_static{}.tgz web_static"
        .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    if compressed.failed:
        return None
    return compressed
