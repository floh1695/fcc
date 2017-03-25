#!/usr/bin/env python3

import argparse

def _compile_args(subparsers):
    compile_subparser = subparsers.add_parser('compile',
            help='Compile LC File(s) to the target language. Default: C')
    compile_subparser.add_argument('files', metavar='FILE', type=str,
            nargs='+', help='Input LC files')

def parse_args(args=None):
    parser = argparse.ArgumentParser(
            description='FC Language Compiler Toolset')
    main_subparsers = parser.add_subparsers(help='Main Tools',
            dest='main_command')
    _compile_args(main_subparsers)
    if args is None:
        return parser.parse_args()
    else:
        return parser.parse_args(args)
