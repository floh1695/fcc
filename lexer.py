#!/usr/bin/env python3

T_STRING = 'string'

class Token:

    def __init__(self, mtype, word):
        self.mtype = mtype
        self.word = word

    def __str__(self):
        return 'Token({}, \"{}\")'.format(self.mtype, self.word)

    def __repr__(self):
        return str(self)

class Lexer:

    def __init__(self, filename):
        self.filename = filename
        self.next_word = ''
        self.token_stack = []
        self.string_mode = False

    # TODO: This needs to be finished to accept and
    #       correctly process all FC samples living
    #       in ./fc/
    def _line_processor(self, line):
        for char in line:
            if self.string_mode:
                if char != self.escapse_string:
                    self.next_word += char
                else:
                    self.token_stack.append(Token(T_STRING, self.next_word))
            if char in ['"', "'", '`']:
                self.string_mode = True
                self.escapse_string = char

    def _file_processor(self, f):
        for line in f:
            self._line_processor(line)

    def tokenize(self):
        with open(self.filename) as f:
            self._file_processor(f)
        return self.token_stack
