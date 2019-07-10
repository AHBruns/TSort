#!/usr/bin/env bash

mkdir -p ~/.melzi/
cd Melzi/src
chmod +x melzi
cp -f melzi ~/.melzi/
cp -f node.py ~/.melzi/
cp -f read_write.py ~/.melzi/
ln -s -f ~/.melzi/melzi /usr/local/bin/melzi
ln -s -f ~/.melzi/melzi /usr/local/bin/melzi
cd ../..
rm -rf Melzi/
