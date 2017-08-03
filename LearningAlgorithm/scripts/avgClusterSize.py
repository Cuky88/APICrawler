'''
This file checks the average cluster sizes of the final KMeans clusters and exports them in json and in csv.
'''

import json
import sys
import csv


def main(argv):
    cnt = 0
    clusters = []
    api = []

    #with open('BigClusterApiStats.json') as reader:
    with open('../results/cosine_500_500_descr.json') as reader:
        read = json.load(reader)
        for t in read:
            cnt += 1
            clusters.append(t['cluster_id'])
            api.append(t)

    clusters = list(set(clusters))



    total = []
    acnt = 0

    for cid in clusters:
        a = []
        cnt2 = 0

        for ca in api:
            if ca['cluster_id'] == cid:
                a.append(ca['id'])
                cnt2 += 1
                acnt += 1

        total.append({'cid': cid, 'aid': a, 'cnt': cnt2})

    file = 'ClusterSizeKMeans.json'

    with open(file, mode='w') as writer:
        json.dump(total, writer, indent=2)
        writer.write('\n')

    # thislineworks
    #with open('ClusterSizeKMeans.csv', 'wb') as f:
    #    w = csv.writer(f)
    #    w.writerows(total)  # notice there are no parens here

    with open('ClusterSizeKMeans.csv', 'wb+') as f:
        dict_writer = csv.DictWriter(f, fieldnames=['cid', 'aid', 'cnt'])
        dict_writer.writeheader()
        dict_writer.writerows(total)


if __name__ == "__main__":
    main(sys.argv)
