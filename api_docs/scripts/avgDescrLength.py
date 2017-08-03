'''
This script counts the average length of the descriptions.
'''
import json
import sys
import re

def countAvgLength(file, dummy):
    descr = []
    cnt = 0

    with open(file) as reader:
        read = json.load(reader)
        for t in read:
            cnt += 1

            if dummy:
                descr.append(t['website_descr'])
            else:
                descr.append(t['progweb_descr'])

    leng = []
    sum = 0

    for d in descr:
        leng.append(len(re.findall(r'\w+', d)))

    for s in leng:
        sum += s

    avg_size = sum / cnt
    print("Avg. Length of Description: ", avg_size)

    return avg_size


def main(argv):
    source = []
    source.append({'progweb': countAvgLength('progweb_final_filtered.json', 0), 'linked': countAvgLength('../data/linked_data.json', 1)})

    file = 'AvgDescrLength.json'

    with open(file, mode='w') as writer:
        json.dump(source, writer, indent=2)
        writer.write('\n')


if __name__ == "__main__":
    main(sys.argv)
