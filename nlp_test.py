import nltk
from textblob import TextBlob
from nltk.stem import SnowballStemmer
snowball = SnowballStemmer(language="russian")
snowball.stem("Хороший")
print(snowball.stem("Хороший"))
ин
wiki = TextBlob("Python is a high-level, general-purpose programming language. Hi")


# for i in wiki.sentences:
#     print(i)
# print(wiki.tags)
# print(wiki.noun_phrases)
# print(wiki.words)
# print(wiki.sentences)



# это для выявление основы слов и для исправление неправельных слов
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
example_sent = morph.parse(input())[0].normal_form

word_list2 = [SnowballStemmer(language="russian").stem(w[0])
              for w in TextBlob(example_sent).tags
              if w[0] not in nltk.corpus.stopwords.words('russian')]

print(word_list2)