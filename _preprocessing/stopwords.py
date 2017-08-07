from nltk.data import path
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

path.append('../api_docs/nltk')
stop_words = set(stopwords.words('english'))
stop_words.add(u'the')
stop_words.add(u'The')
stop_words.add(u'For')

def removeStopWords(str):
    words = word_tokenize(str)
    sansStopWords = [x for x in words if x not in stop_words]
    result = ' '.join(x for x in sansStopWords)
    return result