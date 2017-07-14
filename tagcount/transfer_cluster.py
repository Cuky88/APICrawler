import json
import sys


def transferCluster():
    loaded = []
    final = []

    with open('selected_cuky_v2.json') as reader:
        read = json.load(reader)
        for api in read:
            loaded.append(api)


    with open('../1_data/4_cluster_single/singles/517-eCommerce.json') as reader:
        read = json.load(reader)
        for api in read:
            dic = {}
            dic['progweb_cat'] = api['progweb_cat']
            dic['api_name'] = api['api_name']
            dic['progweb_descr'] = api['progweb_descr']
            dic['id'] = api['id']
            for cluster in loaded:
                if api['id'] == cluster['id']:
                    if 'c' in cluster:
                        dic['cluster_id'] = cluster['c']
                        dic['c_comment'] = cluster['c_comment']

            final.append(dic)


    with open('../1_data/4_cluster_single/singles/517-eCommerce_clusters.json', mode='w') as writer:
        print(len(final))
        json.dump(final, writer, indent=2)
        writer.write("\n")


def main(argv):
    transferCluster()


if __name__ == "__main__":
    main(sys.argv)
