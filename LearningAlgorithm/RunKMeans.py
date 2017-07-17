import time
from sklearn.decomposition import TruncatedSVD as sklearnLSA
import KMeans_simple
import APIDescrReader
import Vectrizer
import Comparator



def run(params, dataset):
    start_time = time.time()


    # Read JSON ######################################
    ##################################################
    dataSetJson = APIDescrReader.load_descr(dataset)
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


    print("--- LSA: %s seconds ---" % (time.time() - start_time))
    start_time = time.time()


    # K-Means #########################################
    ###################################################
    erg = []

    for dist in params[0]:
        for k in params[1]:

            ##simple implementation
            assign = KMeans_simple.start(sklearn_transf, dist, k)

            print "distance:" + dist + " K:" + str(k)
            print assign
            print("--- KMeans: %s seconds ---" % (time.time() - start_time))
            start_time = time.time()

            # Comparison ##############################
            ###########################################
            assignment = []
            i = 0
            for x in assign:
                assignment.append({'id': dataSetJson.apiNr[i], 'name': dataSetJson.name[i], 'cluster_id': x})
                i = i + 1
            quality = Comparator.compare(assignment)
            erg.append({'param1': dist, 'param2': k, 'quality': quality})
            print quality
            print("--- Comparison: %s seconds ---" % (time.time() - start_time))

    return erg










