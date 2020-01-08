#!/usr/bin/python3
""" Module Pack Web Static """
from fabric.api import local, env, put, cd, run
import datetime
import os

env.hosts = ["35.243.168.55", "34.74.7.41"]


def do_pack():
    """ Do pack """
    if not os.path.isdir("./versions"):
        os.mkdir("versions")
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    fail = local("tar -cvzf versions/web_static_{}{}{}{}{}{}.tgz \
                  web_static".format(year,
                                     month, day,
                                     hour, minute,
                                     second))
    if fail.failed:
        return None
    return "versions/web_static_{}{}{}{}{}{}.tgz".format(year,
                                                         month, day,
                                                         hour, minute,
                                                         second)


def do_deploy(archive_path):
    """ Do deploy """

    if not os.path.exists(archive_path):
        return False

    put_ver = put(local_path=archive_path, remote_path="/tmp/")
    if put_ver.failed:
        return False
    name_file = archive_path.split("/")[1].split(".")[0]
    run("mkdir -p /data/web_static/releases/{}".format(name_file))
    uncomp_ver = run("tar -xzf /tmp/{}.tgz -C \
                      /data/web_static/releases/{}".format(
                     name_file, name_file))
    if uncomp_ver.failed:
        return False
    rm_ver = run("rm /tmp/{}.tgz".format(name_file))
    if rm_ver.failed:
        return False
    run("mv /data/web_static/releases/{}/web_static/* \
        /data/web_static/releases/{}".format(name_file, name_file))
    run("rm -rf /data/web_static/releases/{}/web_static".format(name_file))
    rm_link_ver = run("rm -rf /data/web_static/current")
    if rm_link_ver.failed:
        return False
    new_link = run("ln -s /data/web_static/releases/{} \
                    /data/web_static/current".format(name_file))
    if new_link.failed:
        return False
    return True


def deploy():
    """ Deploy """
    archive_path = do_pack()
    if archive_path is None:
        return False
    result = do_deploy(archive_path)
    return result
