'''
Since the Learning Algorithm works on the preprocessed descriptions, we need to bring back the original descriptions (human readable)
'''

import json
import sys
import re

def fullDescr(file1, file2):
    descr = []
    tmp = []

    with open(file2) as reader:
        read = json.load(reader)
        for t in read:
            tmp.append(t)

    with open(file1) as reader:
        read = json.load(reader)
        for a in read:
            for b in tmp:
                if a['id'] == b['id']:
                    descr.append({'api_name': a['api_name'], 'id': a['id'], 'cluster_id': a['cluster_id'], 'progweb_descr': b['progweb_descr']})

    with open('../results/cosine_500_500_descr.json', mode='w') as writer:
        json.dump(descr, writer, indent=2)
        writer.write('\n')


def main(argv):
    file1 = '../results/kmeansresults/cosine_500_500.json'
    file2 = '../../api_docs/progweb_final_filtered.json'

    fullDescr(file1, file2)


if __name__ == "__main__":
    main(sys.argv)
