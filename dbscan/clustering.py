import numpy as np
import codecs, json
from sklearn.cluster import DBSCAN

from sklearn.feature_extraction.text import TfidfVectorizer
# from pylev import levenshtein

# def mylev(s, u, v):
#     return levenshtein(s[int(u)], s[int(v)])

def lev_metric(x, y):
    print x
    print y
    return 1


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

def dbscan(vect, epsi, min_samp):
    db = DBSCAN(eps=epsi, min_samples= min_samp, metric='jaccard').fit(vect)
    db_labels = db.labels_.tolist()
    return db_labels

def main(file, epsi, min_samp):
    descr = loadDescr(file)
    vect = tdidf(descr)
    labels = dbscan(vect,epsi, min_samp)
    return labels


# pca = PCA(n_components=2).fit(X)
# data2D = pca.transform(X)
# plt.scatter(data2D[:,0], data2D[:,1], c = db.labels_)
# plt.show()
