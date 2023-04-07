#!/usr/bin/python3
# Fabric script that distributes an archive to your web servers,
# using the function do_deploy
# based on 1-pack_web_static.py file
from fabric.api import *
import os
from datetime import datetime

env.hosts = ['localhost']


def do_pack():
    try:
        filepath = "versions/web_static_" + datetime.now().\
                   strftime("%Y%m%d%H%M%S") + ".tgz"
        local("mkdir -p versions")
        local("tar -zcvf versions/web_static_$(date +%Y%m%d%H%M%S).tgz\
        web_static")
        print("web_static packed: {} -> {}".
              format(filepath, os.path.getsize(filepath)))
    except:
        return None
