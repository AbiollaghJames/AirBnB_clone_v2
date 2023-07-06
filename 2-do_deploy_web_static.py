#!/usr/bin/python3
"""
  a Fabric script that distributes
  an archive to your web servers
"""


from fabric.api import run, put, env
from os.path import exists


env.user = 'ubuntu'
env.hosts = ['34.204.61.182','18.207.234.131']


def do_deploy(archive_path):
    """distribute archive to web servers"""

    #if archive doesn't exists return false
    if not exists(archive_path):
        return False

    #file name/path
    f_path = archive_path.split("/")
    no_extension = f_path[1].split(".")[0]

    #Uploading
    put(archive_path, "/tmp")
    run("sudo mkdir -p /data/web_static/releases/" + no_extension + "/")
    run("sudo tar -xzf /tmp/" no_extension + ".tgz" + " -C /data/web_static/releases/" + no_extension  + "/")
    run("sudo rm /tmp/" + no_extension + ".tgz")
    run("sudo mv /data/web_static/releases/" + no_extension + "/web_static/* /data/web_static/releases/" + no_extension + "/")
    run("sudo rm -rf /data/web_static/releases/" + no_extension + "/web_static")
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s /data/web_static/releases/" + no_extension + "/ /data/web_static/current")
    if exists("/data/web_static/releases/" + no_extension):
        return True
    else:
        return False
