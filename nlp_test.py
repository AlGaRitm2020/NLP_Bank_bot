import nltk
from textblob import TextBlob
from nltk.stem import SnowballStemmer
snowball = SnowballStemmer(language="russian")
snowball.stem("Хороший")
print(snowball.stem("Хороший"))

wiki = TextBlob("Python is a high-level, general-purpose programming language. Hi")


# for i in wiki.sentences:
#     print(i)
# print(wiki.tags)
# print(wiki.noun_phrases)
# print(wiki.words)
# print(wiki.sentences)



example_sent = """500 рублнй"""
word_list2 = [SnowballStemmer(language="russian").stem(TextBlob(w[0]).correct()) for w in TextBlob(example_sent).tags if w[0].strip() not in nltk.corpus.stopwords.words('russian')]

print(word_list2)