#!/bin/bash

pelican content -o output -s pelicanconf.py
ghp-import output
git push git@github.com:peeomid/peeomid.github.io.git gh-pages:master
