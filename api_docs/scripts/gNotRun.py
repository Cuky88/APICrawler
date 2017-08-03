'''
This script is only needed, when the Google crawler is disrupted due to any reason. The crawled data from Google will be
saved anyway. This data will be loaded here and will be compared with the url_test.json. Every API in url_test.json which
is not in the Google crawled set, will be written in a tmp file notinlist_v1.json. This json needs to be imported by the
gsearch crawler and used for further crawling. If the gsearch crawler is interrupted several times, then this procedure
needs to be done multiple times. Each time, you have to add the Google crawled partial data into this script as input.
At the end, you should not get any APIs after the comparison, when every API was crawled.

You can use the combG.py to combine the partial data from Google.
'''

import json
import jsonlines
import sys
from pprint import pprint


def main(argv):
    title =[]
    notinlist = []

    with jsonlines.open('gsearch_result_v1.json') as reader:
        for gsearch in reader:
            title.append(gsearch['progweb_title'])
    print(len(title))

    with jsonlines.open('gsearch_result.json') as reader:
        for gsearch in reader:
            title.append(gsearch['progweb_title'])
    print(len(title))


    with open('url_test.json') as reader:
        read = json.load(reader)
        for t in read:
            dic = {}
            if t['progweb_title'] not in title:
                dic['progweb_title'] = t['progweb_title']
                dic['api_url'] = t['api_url']
                dic['api_url_full'] = t['api_url_full']
                dic['error'] = t['error']

                notinlist.append(dic)


    with open('notinlist_v1.json', 'w') as outfile:
        print(len(title))
        json.dump(notinlist, outfile, indent=2)
        outfile.write('\n')

if __name__ == "__main__":
    main(sys.argv)