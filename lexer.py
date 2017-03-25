#!/usr/bin/env python3

class Lexer:

    def __init__(self, filename):
        self.filename = filename
        self.token_stack = []

    def _line_processor(self, line):
        for char in line:
            pass

    def _file_processor(self, f):
        for line in f:
            self._line_processor(line)

    def tokenize(self):
        with open(self.filename) as f:
            self._file_processor(f)
