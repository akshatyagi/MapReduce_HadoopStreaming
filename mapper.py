#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import re

def read_input(file):
    for line in file:
        # split the line into words
        line = re.sub('[^a-zA-Z0-9]+',' ', line)
        yield line.split()

def main(separator='\t'):
    # input comes from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if(len(words) == 1):
            print '%s%s%d' % (word, separator, 1)
        else:
            creator = zip(words,words[1:])
            for word in creator:
                print '%s%s%d' % (word, separator, 1)

if __name__ == "__main__":
    main()
