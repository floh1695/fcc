#!/usr/bin/env python3

import argparser

def main():
    args = argparser.parse_args()
    print(args.files)

if __name__ == '__main__':
    main()
