import Lemmatizer
import Reader
import Kmeans
import Vectrizer
import KMeans2
import time
from sklearn.decomposition import PCA as sklearnPCA

start_time = time.time()


# Read JSON ######################################
##################################################
corpus = Reader.load_descr()
print("--- Read Json: %s seconds ---" % (time.time() - start_time))
start_time = time.time()


# Lemmatizing #######################################
##################################################
corp2= []
for el in corpus:
        str3 = Lemmatizer.stem(el)
        corp2.append(str3)
print("--- Lemmatizing: %s seconds ---" % (time.time() - start_time))
start_time = time.time()


# Vectorizer ######################################
###################################################
df = Vectrizer.text_to_vec(corp2)

# DataFrame to NDFrame
df = df.values


print("--- Vectorizer: %s seconds ---" % (time.time() - start_time))
start_time = time.time()

# PCA #############################################
###################################################
sklearn_pca = sklearnPCA(n_components=100)
sklearn_transf = sklearn_pca.fit_transform(df)

#print(sklearn_transf.shape)

print("--- PCA: %s seconds ---" % (time.time() - start_time))
start_time = time.time()


# K-Means #########################################
###################################################

##Second implementation
KMeans2.Kmeans2(sklearn_transf,20,1000)

##First implementation (Marcel)
#Kmeans.TFKMeansCluster(sklearn_transf, 20)
print("--- KMeans: %s seconds ---" % (time.time() - start_time))





