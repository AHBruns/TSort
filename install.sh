#!/usr/bin/env bash

mkdir -p ~/.melzi/
cd Melzi/src
chmod +x melze
cp -f melzi ~/.melzi/
cp -f node.py ~/.melzi/
cp -f read_write.py ~/.melzi/
ln -s -f ~/.tsort/tsort /usr/local/bin/tsort
ln -s -f ~/.tsort/tsort /usr/local/bin/melzi
cd ../..
rm -rf Melzi/
