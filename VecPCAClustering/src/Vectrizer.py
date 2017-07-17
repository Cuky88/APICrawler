import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

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
    feature_names = vectorizer.get_feature_names()

    #dense = tfidf_matrix.todense()
    # denselist = dense.tolist()
    #pd_sparse = pd.SparseDataFrame([pd.SparseSeries(tfidf_matrix[i].toarray().ravel())
    #                    for i in np.arange(tfidf_matrix.shape[0])])

    #del dense
    #df = pd.DataFrame(pd_sparse)
    df = tfidf_matrix
    ### Print the Top 10 Keyords
    # s = pd.Series(df.iloc[0,:])
    # print(s[s > 0].sort_values(ascending=False)[:10])


    #eg word Nr. 6643
    print vectorizer.get_feature_names()[6643]
    #return result: tfidf-Saprse-Matrix
    #(row,column) => (API,word)
    return df
