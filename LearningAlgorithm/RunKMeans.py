import time
from sklearn.decomposition import TruncatedSVD as sklearnLSA
import KMeans2
import Reader2
import Vectrizer
import Comparator



def run(params, dataset):
    start_time = time.time()


    # Read JSON ######################################
    ##################################################
    dataSetJson = Reader2.load_descr(dataset)
    corpus = dataSetJson.descr

    print("--- Read Json: %s seconds ---" % (time.time() - start_time))
    start_time = time.time()


    # Vectorizer ######################################
    ###################################################
    df = Vectrizer.text_to_vec(corpus)

    print("--- Vectorizer: %s seconds ---" % (time.time() - start_time))
    start_time = time.time()

    # LSA #############################################
    ###################################################
    #reduce dimentions to 100
    sklearn_lsa = sklearnLSA(n_components=100, algorithm='randomized', n_iter=5,
            random_state=42, tol=0.0)
    sklearn_transf = sklearn_lsa.fit_transform(df)

    #print(sklearn_transf.shape)

    print("--- LSA: %s seconds ---" % (time.time() - start_time))
    start_time = time.time()


    # K-Means #########################################
    ###################################################
    erg=[]
    for p in params:
        ##Second implementation
        assign = KMeans2.Kmeans2(sklearn_transf, p, 1)

        erg_Kmeans=[]
        i=0
        for x in assign:
            erg_Kmeans.append({'id': dataSetJson.apiNr[i] , 'name' : 'API Name', 'cluster_id': x})
            i=i+1
        quality = Comparator.compare(erg_Kmeans)
        print quality
    return erg
    print("--- KMeans: %s seconds ---" % (time.time() - start_time))





