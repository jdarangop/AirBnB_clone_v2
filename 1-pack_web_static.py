#!/usr/bin/python3
""" Module Pack Web Static """
from fabric.api import local
import datetime
def do_pack():
    """ Do pack """
    now = datetime.datetime.now()
    fail = local("tar -cvzf versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
								  now.month,
							          now.day,
								  now.hour,
								  now.minute,
                                                                  now.second))
     if fail.failed:
         return None
