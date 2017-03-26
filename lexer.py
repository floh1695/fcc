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

    def tokenize(self):
        self.token_stack = []
        try:
            self._tokenize_sub()
        except TypeError:
            pass
        return self.token_stack

    def _push_word(self, token_type, next_word=None):
        if next_word is None:
            next_word = self.next_word
        self.token_stack.append(Token(token_type, next_word))
        self.next_word = ''

    def _get_char(self):
        for char in self.filedata:
            yield char
        yield None

        def _throw_away(self):
            self._get_char()

    def _tokenize_sub(self):
        for char in self._get_char():
            self.next_word += char
