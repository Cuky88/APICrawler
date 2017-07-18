from sklearn.cluster import KMeans


def calc(sklearn_transf, clusters, iterations):
    km = KMeans(n_clusters=clusters, init='k-means++', max_iter=iterations, n_init=1)
    km.fit_predict(sklearn_transf)

    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    for i in range(20):
        print("Cluster %d:" % i)
        for ind in order_centroids[i, :10]:
            print(ind)
        print()
