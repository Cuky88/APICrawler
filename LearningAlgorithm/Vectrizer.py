from sklearn.feature_extraction.text import TfidfVectorizer

def make_corpus(corp):
    for el in corp:
        yield el


def text_to_vec(corp):
    # Stopwords ######################################
    ##################################################

    my_stopword_list = ['and', 'to', 'the', 'of', 'be', 'can', 'their', 'into', 'also', 'with', 'it']

    # Vectorizer #####################################
    ##################################################

    vectorizer = TfidfVectorizer(stop_words=my_stopword_list, sublinear_tf=True, max_features=16000)

    corp2 = make_corpus(corp)
    tfidf_matrix = vectorizer.fit_transform(corp2)

    return tfidf_matrix
