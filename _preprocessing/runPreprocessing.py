import json
import os
import json_reader
import lemmatizer
import punctuations
import stopwords
import unicode
import lowercase

print("******* Start preprocessing of dataset. Please choose one: **********")

dataSet = input(
    "Which dataset do you want to process?\n  - (1) Programmable Web\n  - (2) Google Crawled Data\n")

if dataSet == 1:
    dataSetName = "progweb_final_filtered.json"
    print("You chose (1) Programmable Web, processing " + dataSetName)
    if not os.path.isfile('../api_docs/' + dataSetName):
        print(
        "Error, the file you chose does not exist, yet. Please start the apispider crawler. See Github Readme file!")
        exit(1)
    path_input = '../api_docs/' + dataSetName
    path_output = "../1_data/2_preprocessed/progweb_preprocessed.json"
elif dataSet == 2:
    dataSetName = "complete_final.json"
    print("You chose (2) Google Crawled Data, processing " + dataSetName)
    if not os.path.isfile('../api_docs/' + dataSetName):
        print(
        "Error, the file you chose does not exist, yet. Please start the gsearch crawler. See Github Readme file!")
        exit(1)
    path_input = '../api_docs/' + dataSetName
    path_output = "../1_data/2_preprocessed/complete_preprocessed.json"
else:
    print("Unknown dataset chosen (" + str(dataSet) + ")")
    exit(1)

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
    print(activeApi['id'])
    d = {}
    d['id'] = activeApi['id']

    try:
        d['api_name'] = unicode.removeUnicode(activeApi['prowgeb_title'])
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

json_string = json.dumps(preprocessedFile, indent=2)

with open(path_output, "w") as f:
    f.write(json_string)