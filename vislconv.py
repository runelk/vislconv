#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
import vislconv.cg3 as cg3
import vislconv.conversion as conv


def main(filename, input_enc='ISO-8859-1', output_enc='utf-8'):
    cg3_data = cg3.read(
        codecs.open(filename, 'r', input_enc) if filename
        else codecs.getreader(input_enc)(sys.stdin))
    print conv.to_conll_words_all(cg3_data).encode(output_enc)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
