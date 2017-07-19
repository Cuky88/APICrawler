import json

import json_reader
import lemmatizer
import punctuations
import stopwords
import unicode
import lowercase

path_progweb_final = '/Users/hanche/Google Drive/Studium/InWi Master/Seminar/KDD/APICrawler/1_data/1_raw/progweb_final.json'
path_complete_final = '/Users/hanche/Downloads/complete_final.json'
path_progweb_preprocessed = '/Users/hanche/Google Drive/Studium/InWi Master/Seminar/KDD/APICrawler/1_data/2_preprocessed/progweb_preprocessed.json'
path_complete_preprocessed = '/Users/hanche/Google Drive/Studium/InWi Master/Seminar/KDD/APICrawler/1_data/2_preprocessed/complete_preprocessed.json'

path_input = path_complete_final
path_output = path_complete_preprocessed


file = json_reader.load(path_input)

process_amount = len(file)

preprocessedFile = []

def preprocess(data):
    sansPunct = punctuations.removePunct(data)
    sansStopWords = stopwords.removeStopWords(sansPunct)
    sansUnicode = unicode.removeUnicode(sansStopWords)
    sansCase = lowercase.removeCase(sansUnicode)
    lemmatized = lemmatizer.stem(sansCase)

    return lemmatized



for api in xrange(0, process_amount):
    activeApi = file[api]
    print  activeApi['id']
    d = {}
    d['id'] = activeApi['id']

    try:
        d['api_name'] = unicode.removeUnicode(activeApi['api_name'])
        d['progweb_descr'] = preprocess(activeApi['progweb_descr'])
    except:
        d['progweb_descr'] = ""

    
    
    try:
        d['descr1'] = preprocess(activeApi['descr1'])
        try:
            d['descr2'] = preprocess(activeApi['descr2'])
        except:
            pass

        try:
            d['descr3'] = preprocess(activeApi['descr3'])
        except:
            pass

        try:
            d['descr4'] = preprocess(activeApi['descr4'])
        except:
            pass

        try:
            d['descr5'] = preprocess(activeApi['descr5'])
        except:
            pass
    except:
        pass

    try:
        d['progweb_cat'] = activeApi['progweb_cat']
    except:
        d['progweb_cat'] = ""

    preprocessedFile.append(d)

json_string = json.dumps(preprocessedFile, indent=4)

with open(path_output, "w") as f:
    f.write(json_string)