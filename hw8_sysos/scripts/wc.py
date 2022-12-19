#!/usr/bin/env python3

import sys
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        usage='wc.py [OPTION] [FILE]',
        description='''Print newline, word, and byte counts for FILE (a single one pls!).  A word is a non-zero-length sequence of characters delimited by white space.
            With no FILE, or when FILE is -, read standard input.''')

    parser.add_argument('-l', '--lines', action='store_true',
                        help='print the newline counts')
    parser.add_argument('-w', '--words', action='store_true',
                        help='print the character counts')
    parser.add_argument('-c', '--bytes', action='store_true',
                        help='print the byte counts')
    parser.add_argument('input_text', type=argparse.FileType('r'), default=sys.stdin, nargs='?',
                        help='read input from the file')
    args = parser.parse_args()

    input = args.input_text.read()
    #count lines
    def line_count(input):
        return input.count("\n")

    #count words
    def word_count(input):
        return len(input.split())

    # count bytes
    def byte_count(input):
        return len(input.encode("utf-8"))

    #dictionary to call functions
    commands = {'lines': line_count, 'words': word_count, 'bytes': byte_count}


    output = []
    # create a dictionary for storing -l, -w and -c values
    parameters = vars(args)
    # get the last key to remove from dict
    last_key = list(parameters)[-1]
    # remove the last key using .pop() method
    removed_tuple = parameters.pop(last_key)


    if parameters['lines'] == parameters['words'] == parameters['bytes'] == False:
        parameters['lines'] = True
        parameters['words'] = True
        parameters['bytes'] = True
    # execute needed functions
    for key, value in parameters.items():
        output.append(commands[key](input))

    sys.stdout.write('\t' + '\t'.join(map(str, output)) + '\n')