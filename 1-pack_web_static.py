#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
based on 1-pack_web_static.py file
"""
from fabric.api import *
import time
from datetime import date


def do_pack():
    timestamp = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".
              format(timestamp))
        return ("versions/web_static_{:s}.tgz".format(timestamp))
    except:
        return None
