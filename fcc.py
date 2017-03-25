#!/usr/bin/env python3

import argparser
import command_compile

def main():
    args = argparser.parse_args()
    if args.main_command == 'compile':
        command_compile.main(args)

if __name__ == '__main__':
    main()
