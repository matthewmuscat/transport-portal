#!/bin/bash

# python
add-apt-repository -y ppa:jonathonf/python-3.6

#rethinkdb
echo "deb http://download.rethinkdb.com/apt xenial main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
curl -fsSL https://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -

# docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Install
apt update
apt install -y software-properties-common
apt install -y python-software-properties
apt install -y curl
apt install -y apt-transport-https
apt install -y docker-ce
apt install -y rethinkdb
apt install -y python3.6
apt install -y python3.6-dev
apt install -y build-essential
apt install -y python3-distutils

# Pip
curl -s https://bootstrap.pypa.io/get-pip.py | python3.6 -
python3.6 -m pip install pipenv

# RethinkDB config
tee /etc/rethinkdb/instances.d/rethinkdb.conf <<EOF
runuser=root
rungroup=root
bind=0.0.0.0
driver-port=28015
http-port=28010
EOF

service rethinkdb restart

cat > /etc/environment <<EOL
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games"
VIRTUALENV_ALWAYS_COPY=1
PIPENV_VENV_IN_PROJECT=1
PIPENV_IGNORE_VIRTUALENVS=1
EOL
