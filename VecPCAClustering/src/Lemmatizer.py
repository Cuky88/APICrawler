import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer


def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return wn.NOUN


def change_all(liste):
    list1 = []
    for tup in liste:
        list1.append((tup[0], penn_to_wn(tup[1])))
    return list1


def add_pos(str1):
    liste = nltk.pos_tag(nltk.tokenize.word_tokenize(str1))
    return change_all(liste)


def stem(list2):
    text = ""
    wnl = WordNetLemmatizer()
    for tup in add_pos(list2):
        #if len(wn.synsets(tup[0])) > 0:
            text = text + " " + wnl.lemmatize(tup[0], tup[1])
    return text

