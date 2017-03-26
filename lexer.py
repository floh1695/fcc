#!/usr/bin/env python3

T_COMMENT = 'comment'
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
        self._process_file()  #self.filedata

        self.next_word = ''
        self.token_stack = []

    def _process_file(self):
        self.filedata = ''
        with open(self.filename) as f:
            for line in f:
                for char in line:
                    self.filedata += char

    def _push_word(self, token_type, next_word=None):
        if next_word is None:
            next_word = self.next_word
        self.token_stack.append(Token(token_type, next_word))
        self.next_word = ''

    def tokenize(self):
        self.token_stack = []
        return self.token_stack
