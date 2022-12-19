#!/usr/bin/env python

import os
import sys
import argparse
import shutil

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='rm.py [OPTION] [FILE]',
        description='Removes files or directories')

    parser.add_argument('paths', type=str, help='directory or file to delete', nargs='*')
    parser.add_argument('-r', action='store_true', help='delete directory recursively')

    args = parser.parse_args()

    for path in args.paths:
        try:
            if args.r:
                for path in args.paths:
                    shutil.rmtree(path)
            else:
                for path in args.paths:
                    os.remove(path)

        except (NotADirectoryError, FileNotFoundError):
            sys.stderr.write(f'rm: cannot remove \'{path}\': No such file or directory\n')
        except IsADirectoryError:
            sys.stderr.write(f'rm: cannot remove \'{path}\': Is a directory\n')
