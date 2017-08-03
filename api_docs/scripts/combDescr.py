'''
This script combines the allready combined Google and Progweb data with the crawled documentation sites.
See Wiki on Github
'''

import json
import sys
from pprint import pprint


def main(argv):

    full = []
    tmp = []

    with open('apidescr_result.json') as reader:
        read = json.load(reader)
        for t in read:
            tmp.append(t)

    with open('combGnP.json') as reader:
        read = json.load(reader)
        for api in read:
            cnt = 0

            for descr in tmp:
                if api['progweb_title'] == descr['progweb_title']:
                    cnt += 1

            for descr in tmp:
                if api['progweb_title'] == descr['progweb_title']:
                    if cnt >= 0:
                        print(descr['progweb_title'])
                        print (cnt)

                        if 'descr1' in descr:
                            api['descr1'] = descr['descr1']
                        if 'descr2' in descr:
                            api['descr2'] = descr['descr2']
                        if 'descr3' in descr:
                            api['descr3'] = descr['descr3']
                        if 'descr4' in descr:
                            api['descr4'] = descr['descr4']
                        if 'descr5' in descr:
                            api['descr5'] = descr['descr5']

                        if 'HttpError' in descr:
                            api['HttpError'] = descr['HttpError']
                        if 'DNSLookupError' in descr:
                            api['DNSLookupError'] = descr['DNSLookupError']
                        if 'TimeoutError' in descr:
                            api['TimeoutError'] = descr['TimeoutError']
                        if 'UnknownError' in descr:
                            api['UnknownError'] = descr['UnknownError']

                        cnt -= 1
                        if cnt == 0:
                            full.append(api)

        with open('complete_final.json', 'w') as outfile:
            json.dump(full, outfile, indent=2)
            outfile.write('\n')

if __name__ == "__main__":
    main(sys.argv)