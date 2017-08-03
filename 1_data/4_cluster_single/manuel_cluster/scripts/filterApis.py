'''
This file is used to check the manual clusters, if there are any APIs, which are not assigned to a cluster_id, for example
because it was forgotten or for any other reason. Those APIs will be deleted out of the file. Line 15 and Line 31 need
to be adjusted according to the json filename, which should be checked and saved!
'''

import json
import sys


def main(argv):
    final = []
    cnt = 0

    with open('../662-Financial_clusters.json') as reader:
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

    # File save name
    file = str(cnt) + '-Financial_clusters.json'

    with open('../' + file, mode='w') as writer:
        json.dump(final, writer, indent=2)
        writer.write('\n')


if __name__ == "__main__":
    main(sys.argv)
