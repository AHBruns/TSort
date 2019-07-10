#!/usr/bin/env bash

mkdir -p ~/.tsort/
cd TSort/src
chmod +x tsort
cp -f tsort ~/.tsort/
cp -f node.py ~/.tsort/
cp -f read_write.py ~/.tsort/
ln -s -f ~/.tsort/tsort /usr/local/bin/tsort
ln -s -f ~/.tsort/tsort /usr/local/bin/moen
ln -s -f ~/.tsort/tsort /usr/local/bin/moenize
cd ../..
rm -rf TSort/
