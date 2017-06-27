import Lemmatizer
import Reader
import Kmeans
import Vectrizer
import time
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
df = df.values
print(df)

print("--- Vectorizing: %s seconds ---" % (time.time() - start_time))
start_time = time.time()


# K-Means #########################################
###################################################

Kmeans.TFKMeansCluster(df, 20)
print("--- KMeans: %s seconds ---" % (time.time() - start_time))





