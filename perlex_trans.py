#!/usr/bin/python
# coding=utf-8
#
# Copyright 2012 Behnam Esfahbod <behnam@esfahbod.info>

from __future__ import unicode_literals


TRANS_TABLE = {
        "a": "ا",
        "â": "آ", "ā": "آ",
        "b": "ب",
        "p": "پ",
        "t": "ت",
        "ç": "ث",
        "j": "ج",
        "č": "چ",
        "ł": "ح", "ħ": "ح",
        "x": "خ",
        "d": "د",
        "đ": "ذ",
        "r": "ر",
        "z": "ز",
        "ž": "ژ",
        "s": "س",
        "š": "ش",
        "ş": "ص",
        "ź": "ض",
        "ţ": "ط",
        "ẓ": "ظ",
        "'": "ع",
        "q": "غ",
        "f": "ف",
        "ŕ": "ق",
        "k": "ک",
        "g": "گ",
        "l": "ل",
        "m": "م",
        "n": "ن",
        "w": "و",
        "e": "ه",
        "y": "ی",
        "á": "أ",
        "ú": "ؤ",
        "´": "ئ",
        "°": "\u0652",
        "˝": "\u064C",
        "-": "\u200c",
        "_": "\u200c",
        "=": "", ".": "",
        "#": "#",
        " ": " ",
        }


def transliterate(word):
    assert isinstance(word, unicode)
    res = ''
    i = 0
    for ch in word:
        try:
            res += TRANS_TABLE[ch]
        except KeyError:
            res += ch
        i += 1
    return res

def get_word(line):
    tokens1 = line.strip().split('\t')
    tokens2 = tokens1[0].split('__')
    my_word = tokens2[0]
    return my_word, [tokens2, tokens1]

def set_word(my_word, rest):
    tokens2, tokens1 = rest
    tokens2[0] = my_word
    tokens1[0] = '__'.join(tokens2)
    my_line    = '\t'.join(tokens1)
    return my_line

def main(fin, fout):
    for line in fin:
        my_word, rest = get_word(line)
        my_word = transliterate(my_word)
        my_line = set_word(my_word, rest)
        fout.write(my_line + '\n')

def usage(app_name):
    print "usage: %s <input_file> <output_file>" % app_name

if __name__=='__main__':
    import sys
    import codecs
    if len(sys.argv) < 3:
        usage(sys.argv[0])
        sys.exit(1)

    f1 = codecs.open(sys.argv[1], mode='r', encoding='utf-8')
    f2 = codecs.open(sys.argv[2], mode='w', encoding='utf-8')
    main(f1, f2)

