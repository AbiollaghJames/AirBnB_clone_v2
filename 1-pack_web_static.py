#!/usr/bin/python3
"""
  A Fabric script that generates
  a .tgz archive from the contents
  of the web_static folder
"""


from fabric.api import local
from datetime import datetime


def do_pack():
    """ func to compress file """
    local("mkdir -p versions")
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    comp = local("tar -cvzf versions/web_static_{}.tgz\n
            web_static".format(date))
    if comp.failed:
        return None
    return comp
