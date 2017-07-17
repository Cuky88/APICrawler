import Lemmatizer
import Reader
import Kmeans
import Vectrizer
import KMeans2
import KMeans3
import time
from sklearn.decomposition import TruncatedSVD as sklearnLSA


start_time = time.time()


# Read JSON ######################################
##################################################
dataSetJson = Reader.load_descr("prog")
corpus = dataSetJson.descr

print("--- Read Json: %s seconds ---" % (time.time() - start_time))
start_time = time.time()


# Lemmatizing #######################################
##################################################
#not necessary for ProgWeb

"""
corp2= []
for el in corpus:
        str3 = Lemmatizer.stem(el)
        corp2.append(str3)
print("--- Lemmatizing: %s seconds ---" % (time.time() - start_time))
start_time = time.time()
"""

# Vectorizer ######################################
###################################################
df = Vectrizer.text_to_vec(corpus)

# DataFrame to NDFrame
#df = df.values


print("--- Vectorizer: %s seconds ---" % (time.time() - start_time))
start_time = time.time()


print df

# .apiNR[rowNumber of sparse Matrix df] to get the real API ID
print dataSetJson.apiNr[0]
print dataSetJson.name[0]
# PCA #############################################
###################################################
##reduce dim to number of APIs

"""
sklearn_lsa = sklearnLSA(n_components=100, algorithm='randomized', n_iter=5,
        random_state=42, tol=0.0)
sklearn_transf = sklearn_lsa.fit_transform(df)

#print(sklearn_transf.shape)

print("--- LSA: %s seconds ---" % (time.time() - start_time))
start_time = time.time()


# K-Means #########################################
###################################################

##Second implementation
KMeans2.Kmeans2(sklearn_transf,20,1000)

#KMeans3.calc(sklearn_transf,20,1000)


##First implementation (Marcel)
#Kmeans.TFKMeansCluster(sklearn_transf, 20)
print("--- KMeans: %s seconds ---" % (time.time() - start_time))


"""


