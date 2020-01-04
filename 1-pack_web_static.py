#!/usr/bin/python3
""" Module Pack Web Static """
from fabric.api import local
import datetime
import os


def do_pack():
    """ Do pack """
    if not os.path.isdir("./versions"):
        os.mkdir("versions")
    now = datetime.datetime.now()
    fail = local("tar -cvzf versions/web_static_{}{}{}{}{}{}.tgz \
                  web_static".format(now.year,
                                     now.month, now.day,
                                     now.hour, now.minute,
                                     now.second))
