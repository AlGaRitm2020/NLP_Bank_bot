import nltk
from textblob import TextBlob
from nltk.stem import SnowballStemmer

import pymorphy2

def get_stems(message):
    morph = pymorphy2.MorphAnalyzer()
    example_sent = morph.parse(message)[0].normal_form
    word_list = [SnowballStemmer(language="russian").stem(w[0])
                 for w in TextBlob(example_sent).tags
                 if w[0] not in nltk.corpus.stopwords.words('russian')]

    return word_list


def check_stems(stems: list, key_words: list) -> bool:
    for word in stems:
        if word in key_words:
            return True

