#!/usr/bin/env python3

import string

T_COMMENT = 'comment'
T_STRING = 'string'
T_WORD = 'word'

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
        self._char_gen = self._get_char()
        try:
            self._tokenize_sub()
        except TypeError:
            pass
        return self.token_stack

    def _push_word(self, token_type, next_word=None):
        if next_word is None:
            next_word = self.next_word
        self._push_token(Token(token_type, next_word))
        self.next_word = ''

    def _push_token(self, token):
        self.token_stack.append(token)

    def _pop_token(self):
        if self.token_stack:
            return self.token_stack.pop()
        return None

    def _peek_token(self):
        peeked = self._pop_word()
        if not peeked:
            self._push_token(peeked)
        return peeked

    def _get_char(self):
        for char in self.filedata:
            yield char

    def _tokenize_sub(self):
        for char in self._char_gen:
            self._tokenize_sorter(char)

    def _tokenize_sorter(self, char):
        if char in ['#']:
            self._tokenize_comment()
        elif char in ['\"', '`', '\'']:
            self._tokenize_string(char)
        elif char.isspace():
            return
        elif char in (string.ascii_lowercase + string.ascii_uppercase):
            self._tokenize_word(char)

    def _tokenize_comment(self):
        for char in self._char_gen:
            if char in ['\n', '\r']:
                break
            self.next_word += char
        self._push_word(T_COMMENT)

    def _tokenize_string(self, quote):
        for char in self._char_gen:
            if char in [quote]:
                break
            self.next_word += char
        self._push_word(T_STRING)

    def _tokenize_word(self, first):
        self.next_word += first
        for char in self._char_gen:
            if char in (string.ascii_lowercase + string.ascii_uppercase
                    + string.digits):
                self.next_word += char
            else:
                self._push_word(T_WORD)
                self._tokenize_sorter(char)
                return
