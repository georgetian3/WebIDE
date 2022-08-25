#!/bin/bash

curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
sudo apt install -y jq nodejs build-essential g++ libx11-dev libxkbfile-dev libsecret-1-dev python-is-python3 git quilt
sudo npm install yarn --global
git clone https://github.com/coder/code-server.git
cd code-server
git submodule update --init
quilt push -a
yarn
yarn build
yarn build:vscode
yarn release
cd release
yarn --production

mkdir ~/.config
mkdir ~/.config/code-server
echo "bind-addr: 0.0.0.0:8080
auth: password
password:
cert: false" > ~/.config/code-server/config.yaml
