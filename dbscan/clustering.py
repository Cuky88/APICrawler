import numpy as np
import codecs, json
from sklearn.cluster import DBSCAN

from sklearn.feature_extraction.text import TfidfVectorizer


def loadDescr(file):
    documents = []
    for api in xrange(0, len(file)):
        documents.append(file[api]['progweb_descr'])
    return documents


print "START TDIDF"

def tdidf(descr):
    vect = TfidfVectorizer(min_df=1)
    X = vect.fit_transform(descr)
    X = X.todense()
    return X

# print "START KMEANS"


# from sklearn.cluster import KMeans

# kmeans = KMeans(n_clusters=10, random_state=0).fit(X)

# km_labels = kmeans.labels_.tolist()

# file_path_kmeans = '/Users/hanche/Google Drive/Studium/InWi Master/Seminar/KDD/APICrawler/dbscan/dest/kmeans.json'
# json_kmeans = json.dumps(km_labels , codecs.open(file_path_kmeans, 'w', encoding='utf-8'),separators=(',', ':'), indent=4)

# with open(file_path_kmeans, "w") as f:
#     f.write(json_kmeans)

print "START DBSCAN"

def dbscan(vect):
    db = DBSCAN(eps=1.2, min_samples= 2).fit(vect)
    db_labels = db.labels_.tolist()
    return db_labels

def main(file):
    descr = loadDescr(file)
    vect = tdidf(descr)
    labels = dbscan(vect)
    return labels


# pca = PCA(n_components=2).fit(X)
# data2D = pca.transform(X)
# plt.scatter(data2D[:,0], data2D[:,1], c = db.labels_)
# plt.show()
