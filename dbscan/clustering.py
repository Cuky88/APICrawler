import numpy as np
import codecs, json

from sklearn.feature_extraction.text import TfidfVectorizer



def load_json():
    with open(
            '/Users/hanche/Google Drive/Studium/InWi Master/Seminar/KDD/APICrawler/dbscan/preprocessed/preprocessed.json') as data_file:
        data = json.load(data_file)
    return data


file = load_json()
documents = []

for api in xrange(0, len(file)):
    documents.append(file[api]['progweb_descr'])

print "START TDIDF"

vect = TfidfVectorizer(min_df=1)
X = vect.fit_transform(documents)

X = X.todense()

print "START KMEANS"

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=40, random_state=0).fit(X)

km_labels = kmeans.labels_.tolist()

file_path_kmeans = '/Users/hanche/Google Drive/Studium/InWi Master/Seminar/KDD/APICrawler/dbscan/dest/kmeans.json'
json_kmeans = json.dumps(km_labels , codecs.open(file_path_kmeans, 'w', encoding='utf-8'),separators=(',', ':'), indent=4)

with open(file_path_kmeans, "w") as f:
    f.write(json_kmeans)

print "START DBSCAN"

from sklearn.cluster import DBSCAN

db = DBSCAN(eps=1.2, min_samples= 2).fit(X)

db_labels = db.labels_.tolist()

file_path_db = '/Users/hanche/Google Drive/Studium/InWi Master/Seminar/KDD/APICrawler/dbscan/dest/db.json'
json_db = json.dumps(db_labels , codecs.open(file_path_db, 'w', encoding='utf-8'),separators=(',', ':'), indent=4)

with open(file_path_db, "w") as f:
    f.write(json_db)

# pca = PCA(n_components=2).fit(X)
# data2D = pca.transform(X)
# plt.scatter(data2D[:,0], data2D[:,1], c = db.labels_)
# plt.show()
