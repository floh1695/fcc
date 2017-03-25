#!/usr/bin/env python3

import sys

import argparser
import filewrapper

def main(args=None):
    if args == None:
        args = argparser.parse_args(['compile'] + sys.args)
    files = args.files  # Really just filenames

    filewrappers = []
    for f in files:
        filewrappers.append(filewrapper.FileWrapper(f))
