'''
This script combines the different Google data json to one file. It needs to be started after you've run gsearch crawler
with multiple interruptions.
'''

import json
import jsonlines
import sys
from pprint import pprint


def main(argv):

    title = []


    with jsonlines.open('gsearch_result_v1.json') as reader:
        for gsearch in reader:
            title.append(gsearch)
    print(len(title))

    with jsonlines.open('gsearch_result_v2.json') as reader:
        for gsearch in reader:
            title.append(gsearch)
    print(len(title))


    with open('gsearch_final.json', 'w') as outfile:
        print(len(title))
        json.dump(title, outfile, indent=2)
        outfile.write('\n')

if __name__ == "__main__":
    main(sys.argv)