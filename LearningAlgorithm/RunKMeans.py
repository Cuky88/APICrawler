import time
from sklearn.decomposition import TruncatedSVD as sklearnLSA
import KMeans_simple
import APIDescrReader
import Vectrizer
import Comparator
import JWriter as fw
from subprocess import call
import Reader


def run(params, dataset, delTMP, compJar):
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



    # K-Means #########################################
    ###################################################
    erg = []

    for dist in params[0]:
        for k in params[1]:
            for n in params[2]:

                # LSA #############################################
                ###################################################
                # reduce dimentions to n
                sklearn_lsa = sklearnLSA(n_components=n, algorithm='randomized', n_iter=5,
                                         random_state=42, tol=0.0)
                sklearn_transf = sklearn_lsa.fit_transform(df)

                print("--- LSA: %s seconds ---" % (time.time() - start_time))
                start_time = time.time()


                ##simple implementation
                assign = KMeans_simple.start(sklearn_transf, dist, k)

                print "distance:" + dist + " K:" + str(k) + " dim:"+ str(n)

                print("--- KMeans: %s seconds ---" % (time.time() - start_time))
                start_time = time.time()

                # Comparison ##############################
                ###########################################
                assignment = []

                i = 0
                for x in assign:
                    assignment.append({'id': dataSetJson.apiNr[i], 'cluster_id': x, 'api_name': dataSetJson.name[i],
                                       'progweb_descr': dataSetJson.descr[i]})
                    i = i + 1
                fw.writeToJson(assignment, "kmeansresults/"+dist +"_"+ str(k)+"_"+str(n)+".json")

                Reader.load_manual_cluster(1)

                quality = Comparator.compare(assignment)

                erg.append({'distance': dist, 'K': k, 'dim': n,'quality': quality})
                print(quality)
                print("--- Comparison: %s seconds ---" % (time.time() - start_time))

                if delTMP:
                    print("\n--- Deleting /tmp folder ---\n")
                    call('chmod +x delTMP.sh', shell=True)
                    call("./delTMP.sh")

    fw.writeToJson(erg, "JaccardResults.json")

    if compJar:
        start_time = time.time()
        print("\n--- Starting Comparator.jar ---\n")
        call('chmod +x compJar.sh', shell=True)
        call("./compJar.sh")
        print("\n--- Comparator.jar %s seconds\nCheck working directory! ---" % (time.time() - start_time))









