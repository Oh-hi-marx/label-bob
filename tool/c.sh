#!/bin/sh
echo Enter commit message
read varname
git add .
git commit -m "auto commit -$varname"
git push
