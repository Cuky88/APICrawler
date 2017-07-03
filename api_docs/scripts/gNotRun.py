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


    with open('url_test_15877.json') as reader:
        read = json.load(reader)
        for t in read:
            dic = {}
            if t['progweb_title'] not in title:
                dic['progweb_title'] = t['progweb_title']
                dic['api_url'] = t['api_url']
                dic['api_url_full'] = t['api_url_full']
                dic['error'] = t['error']

                notinlist.append(dic)


    with open('notinlist_v2.json', 'w') as outfile:
        print(len(title))
        json.dump(notinlist, outfile, indent=2)
        outfile.write('\n')

if __name__ == "__main__":
    main(sys.argv)