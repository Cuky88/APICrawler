import string

punct = set(string.punctuation)
def removePunct(str):
    sansPunct = ''.join(x for x in str if x not in punct)
    return sansPunct
