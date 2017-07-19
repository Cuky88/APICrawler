import json
import sys


def checkDup(fin, map, pay, eco, mes):
    for a in fin:
        for b in map:
            for c in pay:
                for d in eco:
                    for e in mes:
                        if e == d or e == c or e == b or e == a:
                            print("ID-Error in Messaging: " + str(e), (e == d), (e == c), (e == b), (e == a))

                    if d == c or d == b or d == a:
                        print("ID-Error in eCommerce: " + str(d), d == c, d == b, d == a)

                if c == b or c == a:
                    print("ID-Error in Payments: " + str(c), c == b, c == a)

            if b == a:
                print("ID-Error in Mapping: " + str(b), b == a)


def main(argv):
    financial = []
    mapping = []
    payments = []
    ecommerce = []
    messaging = []

    fin = []
    map = []
    pay = []
    eco = []
    mes = []

    clusters = []
    cluster_api = []

    cnt = 0

    with open('31-Financial_clusters.json') as reader:
        read = json.load(reader)
        for t in read:
            cnt += 1
            fin.append(t['cluster_id'])
            financial.append(t)

            dic = {}
            dic['cluster'] = t['cluster_id']
            dic['api'] = t['id']

            cluster_api.append(dic)
            clusters.append(t['cluster_id'])

    with open('32-Mapping_clusters.json') as reader:
        read = json.load(reader)
        for t in read:
            map.append(t['cluster_id'])
            mapping.append(t)

            dic = {}
            dic['cluster'] = t['cluster_id']
            dic['api'] = t['id']

            cluster_api.append(dic)
            clusters.append(t['cluster_id'])

    with open('113-Payments_clusters.json') as reader:
        read = json.load(reader)
        for t in read:
            pay.append(t['cluster_id'])
            payments.append(t)

            dic = {}
            dic['cluster'] = t['cluster_id']
            dic['api'] = t['id']

            cluster_api.append(dic)
            clusters.append(t['cluster_id'])

    with open('399-eCommerce_clusters_final.json') as reader:
        read = json.load(reader)
        for t in read:
            eco.append(t['cluster_id'])
            ecommerce.append(t)

            dic = {}
            dic['cluster'] = t['cluster_id']
            dic['api'] = t['id']

            cluster_api.append(dic)
            clusters.append(t['cluster_id'])

    with open('529-Messaging_clusters.json') as reader:
        read = json.load(reader)
        for t in read:
            if 'cluster_id' in t:
                mes.append(t['cluster_id'])
                messaging.append(t)

                dic = {}
                dic['cluster'] = t['cluster_id']
                dic['api'] = t['id']

                cluster_api.append(dic)
                clusters.append(t['cluster_id'])
            else:
                print("Missing:" + str(t['id']))

    # check for duplicate cluster ids in different files
    # checkDup(fin, map, pay, eco, mes)

    clusters = list(set(clusters))

    total = []
    acnt = 0

    for cid in clusters:
        api = []
        cnt2 = 0

        for ca in cluster_api:
            if ca['cluster'] == cid:
                api.append(ca['api'])
                cnt2 += 1
                acnt += 1

        total.append({'cid': cid, 'aid': api, 'cnt': cnt2})

    avg_size = acnt / len(clusters)
    print("Avg. Size of Cluster: ", avg_size)

    i = 0
    j = 0
    big_cluster = []
    idToDelete = []

    for cl in total:
        if cl['cnt'] < 10:
            i += 1
        if cl['cnt'] < 5:
            j += 1
            idToDelete.append(cl['cid'])
        if cl['cnt'] > 5:
            big_cluster.append(cl)

    print("\nNumber of clusters smaller than 10: ", i)
    print("\nNumber of clusters smaller than 5: ", j)
    print("\nTotal number of clusters: ", len(clusters))

    file = 'AllClusterApiStats.json'
    file2 = 'BigClusterApiStats.json'
    file3 = 'IDToDelete.json'

    #print(big_cluster)

    with open(file, mode='w') as writer:
        json.dump(total, writer, indent=2)
        writer.write('\n')

    with open(file2, mode='w') as writer:
        json.dump(big_cluster, writer, indent=2)
        writer.write('\n')

    with open(file3, mode='w') as writer:
        json.dump(idToDelete, writer, indent=2)
        writer.write('\n')


if __name__ == "__main__":
    main(sys.argv)
