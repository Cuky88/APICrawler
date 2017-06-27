import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def text_to_vec(corp2):
    # Stopwords ######################################
    ##################################################

    my_stopword_list = ['and','to','the','of','be','can','their','into','also','with','it']

    # Vectorizer #####################################
    ##################################################

    vectorizer = TfidfVectorizer(stop_words=my_stopword_list, sublinear_tf=True)

    tfidf_matrix = vectorizer.fit_transform(corp2)
    feature_names = vectorizer.get_feature_names()

    dense = tfidf_matrix.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist, columns=feature_names, index=corp2)

    ### Print the Top 10 Keyords
    # s = pd.Series(df.iloc[0,:])
    # print(s[s > 0].sort_values(ascending=False)[:10])

    return df