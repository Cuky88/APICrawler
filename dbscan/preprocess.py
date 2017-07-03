import json
import re
import string
import Lemmatizer

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def load_json():
    with open('/Users/hanche/Google Drive/Studium/InWi Master/Seminar/KDD/APICrawler/dbscan/source/progweb_final_filtered.json') as data_file:
        data = json.load(data_file)
    descr=[]

    # for x in xrange(0, len(data)):
    #     if data[str(x)].get("progweb_descr"):
    #         text = data[str(x)]["progweb_descr"]
    #         output = re.sub(r'\d+', '', text)
    #         descr.append(output)
    return data

punct = set(string.punctuation)

def removePunct(str):
    sansPunct = ''.join(x for x in str if x not in punct)
    return sansPunct

stop_words = set(stopwords.words('english'))
stop_words.add(u'the')
stop_words.add(u'The')
stop_words.add(u'For')

def removeStopWords(str):
    words = word_tokenize(str)
    sansStopWords = [x for x in words if x not in stop_words]
    result = ' '.join(x for x in sansStopWords)
    return result

file = load_json()
preprocessFile = []

def preprocessDescr(str):
    sansPunct = removePunct(str)
    sansStopWords = removeStopWords(sansPunct)
    lemmatized = Lemmatizer.stem(sansStopWords)
    return lemmatized

not_exist = object()

for api in xrange(0, len(file)):
    activeApi = file[api]
    print  activeApi['id']
    d = {}
    d['id'] = activeApi['id']
    d['api_name'] = activeApi['api_name']

    try:
        d['progweb_descr'] = preprocessDescr(activeApi['progweb_descr'])
    except:
        d['progweb_descr'] = ""
    try:
        d['progweb_cat'] = activeApi['progweb_cat']
    except:
        d['progweb_cat'] = ""

    # if hasattr(activeApi, 'progweb_descr'):
    #     d['progweb_descr'] = ""
    # else:
    #     d['progweb_descr'] = activeApi['progweb_descr']
    #
    # if hasattr(activeApi, 'progweb_cat'):
    #     d['progweb_cat'] = ""
    # else:
    #     d['progweb_cat'] = activeApi['progweb_cat']

    preprocessFile.append(d)


json_string = json.dumps(preprocessFile, indent=4)


with open('/Users/hanche/Google Drive/Studium/InWi Master/Seminar/KDD/APICrawler/dbscan/preprocessed/preprocessed.json', "w") as f:
    f.write(json_string)

# {
#     "crawled_date": "2017-06-27T09:24:52.854585",
#     "progweb_title": "Instagram API",
#     "progweb_url": "https://www.programmableweb.com/api/instagram",
#     "progweb_descr": "Instagram is a photo sharing iPhone app and service. Users take photos and can share them with Instagram contacts, as well as friends on other social networks like Twitter and Facebook. The Instagram API provides access to user authentication, friend connections, photos and all the other elements of the iPhone app--including uploading new media.",
#     "api_url_full": "http://instagram.com/developer/",
#     "progweb_date": "12.15.2010",
#     "api_name": "Instagram",
#     "progweb_cat": "Photos,Mobile",
#     "id": 0,
#     "api_url": "instagram.com"
#   },

