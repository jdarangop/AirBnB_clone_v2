#!/usr/bin/python3
""" Module Pack Web Static """
from fabric.api import local, env, put, cd
import datetime
import os

env.hosts = ["35.243.168.55", "34.74.7.41"]

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

    if not os.path.isfile(archive_path):
        return False

    #put(archive_path, "/tmp/")
    put_ver = put(archive_path, "/tmp")
    if pur_ver.failed:
        return False
    name_file = archive_path.split("/")[1].split(".")[0]
    with cd("/tmp/"):
        run("mkdir /data/web_static/releases/{}".format(name_file))
    uncomp_ver = run("tar zxvf /tmp/{}.tgz -C \
                      /data/web_static/releases/{}".format(name_file, name_file))
    if uncomp_ver.failed:
        return False
    rm_ver = run("rm /data/web_static/releases/{}.tgz".format(name_file))
    rm_ver = run("rm /tmp/{}.tgz".format(name_file))
    if rm_ver.failed:
        return False
    rm_link_ver = run("rm /data/web_static/current")
    if rm_link_ver.failed:
        return False
    new_link = run("ln -snf /data/web_static/releases/{} \
                    /data/web_static/current".format(name_file))
    if new_link.failed:
        return False
    return True
