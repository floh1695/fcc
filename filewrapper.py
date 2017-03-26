#!/usr/bin/env python3

import lexer

class FileWrapper:
    def __init__(self, filename):
        self.filename = filename
        self._init_data()

    def _init_data(self):
        self._init_tokens()

    def _init_tokens(self):
        lex = lexer.Lexer(self.filename)
        self.tokens = lex.tokenize()
        print self.tokens
