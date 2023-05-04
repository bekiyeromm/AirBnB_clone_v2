#!/usr/bin/env bash
# a script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/
echo "hello world" | sudo tee /data/web_static/releases/test/index.html>/dev/null
sudo rm -rf /data/web_static/current
ls -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubunt /data/
sudo sed -i '38i \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
