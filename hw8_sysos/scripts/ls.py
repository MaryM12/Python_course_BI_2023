#! /usr/bin/env python3
# ls_function_analogue
import os
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='./ls.py  [OPTION]... [FILE]...',
        description='''List information about the FILEs (the current directory by default).
        Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.''')

    parser.add_argument('-a', '--all', action='store_true',
                        help='do not ignore entries starting with .')
    parser.add_argument('directory_path', type=str, default='.', nargs='*')

    args = parser.parse_args()

    target_dir = args.directory_path


    # multiple directrories may be indicated, iterate over them
    for directory in args.directory_path:
        # check if a directory exists
        if not os.path.exists(directory):
            sys.stderr.write(f'ls: cannot access \'{directory}\': No such file or directory\n')
            raise sys.exit(0)
            # continue
        #if it's not a directory - print itself
        if not os.path.isdir(directory):
            sys.stdout.write(f'{directory}' + '\n')
        else:
            contents = list(sorted(os.listdir(directory)))
            if args.all:
                contents.extend(['.', '..'])
            else:
                contents = list(filter(lambda x: not x.startswith('.'), contents))

            # diff outputs depending on number of directories
            if len(args.directory_path) > 1:
                sys.stdout.write(directory + ": \n")
                for content in sorted(contents):
                    sys.stdout.write(content + "\n")
            elif len(args.directory_path) == 1:
                for content in sorted(contents):
                    sys.stdout.write(content + "\n")