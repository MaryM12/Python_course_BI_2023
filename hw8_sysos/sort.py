#!/usr/bin/env python3

import sys
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='sort.py [OPTION] [FILE]',
        description='''Write sorted concatenation of all FILE(s) to standard output.
        With no FILE, or when FILE is -, read standard input.''')

    parser.add_argument('input', nargs='*', help='read input from the files')
    args = parser.parse_args()
    input_lines = []
    try:
        if args.input:
            for file in args.input:
                with open(file, 'r') as inp_file:
                    for line in inp_file.readlines():
                        input_lines.append(line.strip())
        else:
            for line in sys.stdin:
                input_lines.append(line.strip())

        sorted_lines = sorted(input_lines)
        for line in sorted_lines:
            sys.stdout.write(line + '\n')
    except FileNotFoundError:
        sys.stderr.write(f"sort: cannot read: '{file}': No such file or directory\n")