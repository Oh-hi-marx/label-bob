#!/bin/sh
python downloadFromTxt.py
python extractFrames.py
python edit.py
python segment.py
