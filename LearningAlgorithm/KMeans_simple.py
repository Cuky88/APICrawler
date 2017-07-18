import tensorflow as tf




def start(hw_frame, dist, k):

    def input_fn():
        return tf.constant(hw_frame, tf.float32, hw_frame.shape), None

    tf.logging.set_verbosity(tf.logging.ERROR)
    #or distance_metric='squared_euclidean'
    #own distance metric could be written by modifiying  tensorflow/tensorflow/contrib/factorization/python/ops/clustering_ops.py
    kmeans = tf.contrib.learn.KMeansClustering(num_clusters=k, relative_tolerance=0.0001, distance_metric=dist)
    kmeans = kmeans.fit(input_fn=input_fn)

    clusters = kmeans.clusters()
    assignments = list(kmeans.predict_cluster_idx(input_fn=input_fn))


    return assignments



