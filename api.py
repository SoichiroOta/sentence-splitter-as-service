import os
import json

import responder

from tokenization import Tokenizer


env = os.environ
DEBUG = env['DEBUG'] in ['1', 'True', 'true']
LANG = env.get('LANG')
MECAB_ARGS = env.get('MECAB_ARGS')

api = responder.API(debug=DEBUG)
tokenizer = Tokenizer(lang=LANG, mecab_args=MECAB_ARGS)


@api.route("/")
async def tokenize(req, resp):
    body = await req.text
    texts = json.loads(body)
    docs = [tokenizer.tokenize(text) for text in texts]
    resp.media = dict(data=docs)


if __name__ == "__main__":
    api.run()