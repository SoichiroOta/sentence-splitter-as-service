import sengiri
from sentence_splitter import SentenceSplitter


class JaTokenizer:
    def __init__(self, mecab_args=None):
        self.mecab_args = mecab_args
        if mecab_args:
            self.tokenize = self.tokenize_with_mecab_args
        else:
            self.tokenize = self.tokenize_without_mecab_args

    def tokenize_with_mecab_args(self, text):
        return sengiri.tokenize(text, mecab_args=self.mecab_args)

    def tokenize_without_mecab_args(self, text):
        return sengiri.tokenize(text)


class MlTokenizer:
    def __init__(self, lang=None):
        self.splitter = SentenceSplitter(language=lang)

    def tokenize(self, text):
        return self.splitter.split(text=text)


class Tokenizer:
    def __init__(self, lang=None, mecab_args=None):
        if lang == 'ja':
            self.tokenizer = JaTokenizer(mecab_args=mecab_args)
        else:
            self.tokenizer = MlTokenizer(lang=lang)

    def tokenize(self, text):
        return self.tokenizer.tokenize(text)
