import json
import sys


def main(argv):
    final = []
    cnt = 0

    with open('662-Financial_clusters.json') as reader:
        read = json.load(reader)
        for i, api in enumerate(read):
            dic = {}
            if 'cluster_id' in api:
                dic['cluster_id'] = api['cluster_id']
                dic['progweb_descr'] = api['progweb_descr']
                dic['id'] = api['id']
                dic['progweb_cat'] = api['progweb_cat']
                dic['c_comment'] = api['c_comment']

                final.append(dic)

                cnt = i

    file = str(cnt) + '-Financial_clusters.json'

    with open(file, mode='w') as writer:
        json.dump(final, writer, indent=2)
        writer.write('\n')


if __name__ == "__main__":
    main(sys.argv)
