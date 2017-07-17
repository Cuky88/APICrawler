import tensorflow as tf
import time


def bucket_mean(data, bucket_ids, num_buckets):
    total = tf.unsorted_segment_sum(data, bucket_ids, num_buckets)
    count = tf.unsorted_segment_sum(tf.ones_like(data), bucket_ids, num_buckets)
    return total / count


def Kmeans2(df,K,MAX_ITERS):
    N = df.shape[0]
    dim = df.shape[1]

    start = time.time()

    with tf.Session() as sess:
        tf.global_variables_initializer().run()

        points = tf.constant(df)
        print(points.eval())

    points = tf.Variable(points)


    #points = tf.Variable(tf.random_uniform([N, 100]))
    print "########################"
    print points.get_shape()

    init_op = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init_op) #execute init_op
        #print the random values that we sample
        print (sess.run(points))


    cluster_assignments = tf.Variable(tf.zeros([N], dtype=tf.int64))

    #TODO: good initialization:
    centroids = tf.Variable(tf.slice(points.initialized_value(), [0, 0], [K, dim]))

    # Replicate to N copies of each centroid and K copies of each
    # point, then subtract and compute the sum of squared distances.
    rep_centroids = tf.reshape(tf.tile(centroids, [N, 1]), [N, K, dim])
    rep_points = tf.reshape(tf.tile(points, [1, K]), [N, K, dim])
    sum_squares = tf.reduce_sum(tf.square(rep_points - rep_centroids),
                                reduction_indices=2)

    # Use argmin to select the lowest-distance point
    best_centroids = tf.argmin(sum_squares, 1)
    did_assignments_change = tf.reduce_any(tf.not_equal(best_centroids,
                                                        cluster_assignments))

    means = bucket_mean(points, best_centroids, K)

    # Do not write to the assigned clusters variable until after
    # computing whether the assignments have changed - hence with_dependencies
    with tf.control_dependencies([did_assignments_change]):
        do_updates = tf.group(
            centroids.assign(means),
            cluster_assignments.assign(best_centroids))

    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    changed = True
    iters = 0

    while changed and iters < MAX_ITERS:
        iters += 1
        [changed, _] = sess.run([did_assignments_change, do_updates])

    [centers, assignments] = sess.run([centroids, cluster_assignments])
    end = time.time()
    print ("Found in %.2f seconds" % (end - start)), iters, "iterations"
    print "Cluster assignments:", assignments

    return assignments





