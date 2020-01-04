#!/usr/bin/python3
""" Module Pack Web Static """
from fabric.api import local, env, put, cd
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
    if fail.failed:
        return False

def do_deploy(archive_path):
    """ Do deploy """

    env.hosts = ["35.243.168.55", "34.74.7.41"]
    if not os.path.exists(archive_path):
        return False

    put_ver = put(local_path=archive_path, remote_path="/tmp/")
    if pur_ver.failed:
        return False
    name_file = archive_path.split("/")[1].split(".")[0]
    uncomp_ver = run("tar zxvf \
                      /data/web_static/releases/{}".format(name_file))
    if uncomp_ver.failed:
        return False
    rm_ver = run("rm /data/web_static/releases/{}".format(name_file))
    if rm_ver.failed:
        return False
    rm_link_ver = run("rm /data/web_static/current")
    if rm_link_ver.failed:
        return False
    new_link = run("ln -snf /data/web_static/releases/{} \
                    /data/web_static/current".format(name_file))
    if new_link.failed:
        return False
