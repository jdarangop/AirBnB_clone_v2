#!/usr/bin/env bash
# Prepare web server

apt-get -y update
apt-get -y install nginx

if [ ! -d "/data" ];
then
	mkdir /data
fi


if [ ! -d "/data/web_static" ];
then
	mkdir /data/web_static
fi

if [ ! -d "/data/web_static/releases" ];
then
	mkdir /data/web_static/releases
fi

if [ ! -d "/data/web_static/shared" ];
then
	mkdir /data/web_static/shared
fi

if [ ! -d "/data/web_static/releases/test" ];
then
	mkdir /data/web_static/releases/test
fi

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -snf /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -ie "s/^server {$/server {\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current;\n\t\tautoindex off;\n\t}/g" /etc/nginx/sites-available/default
service nginx restart
