import unicodedata

def removeUnicode(str):
    clean = unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')
    clean = clean.replace('\"', r"'")
    return clean