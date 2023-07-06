#!/usr/bin/env bash
#A Bash script that sets up your web servers for the deployment of web_static
#install nginx
sudo apt-get update
sudo apt-get install nginx -y
sudo ufw allow 'Nginx HTTP'

#create directories '-p creates parent folders'
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

#create fake HTML file
cat > /data/web_static/releases/test/index.html << DATA
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
DATA

#Symbolic link
ln -sf /data/web_static/current /data/web_static/releases/test/

#Ownership
chown -R ubuntu /data
chgrp -R ubuntu /data

#update nginx config file
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default

#Restart nginx
sudo service nginx restart
exit 0
