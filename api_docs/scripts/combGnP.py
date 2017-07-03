import json
import sys
from pprint import pprint


def main(argv):
    full = []
    tmp = []

    # add information from google crawling to progweb dataset
    with open('gsearch_final_filtered.json') as reader:
        read = json.load(reader)
        for t in read:
            tmp.append(t)

    with open('progweb_final_15838.json') as reader:
        read = json.load(reader)

        for api in read:
            dic = {}
            if 'id' in api:
                dic['id'] = api['id']
            else:
                dic['id'] = 000000


            if 'api_name' in api:
                dic['api_name'] = api['api_name']
            else:
                dic['api_name'] = "NO NAME"

            if 'progweb_cat' in api:
                dic['progweb_cat'] = api['progweb_cat']
            else:
                dic['progweb_cat'] = "NO CATEGORIES"

            if 'progweb_descr' in api:
                dic['progweb_descr'] = api['progweb_descr']
            else:
                dic['progweb_descr'] = "NO DESCRIPTION"

            if 'progweb_title' in api:
                dic['progweb_title'] = api['progweb_title']
            else:
                dic['progweb_title'] = "NO TITLE"

            if 'progweb_url' in api:
                dic['progweb_url'] = api['progweb_url']
            else:
                dic['progweb_url'] = "NO PROGWEBURL"

            if 'api_url' in api:
                dic['api_url'] = api['api_url']
            else:
                dic['api_url'] = "NO URL"

            if 'api_url_full' in api:
                dic['api_url_full'] = api['api_url_full']
            else:
                dic['api_url_full'] = "NO FULL-URL"

            if 'progweb_date' in api:
                dic['progweb_date'] = api['progweb_date']
            else:
                dic['progweb_date'] = "01.01.2020"

            dic['crawled_date'] = api['crawled_date']

            for gsearch in tmp:
                if 'api_url_full' in api:
                    if api['progweb_title'] == gsearch['progweb_title']:
                        if 'link1' in gsearch:
                            dic['link1'] = gsearch['link1']
                        if 'link2' in gsearch:
                            dic['link2'] = gsearch['link2']
                        if 'link3' in gsearch:
                            dic['link3'] = gsearch['link3']
                        if 'link4' in gsearch:
                            dic['link4'] = gsearch['link4']
                        if 'link5' in gsearch:
                            dic['link5'] = gsearch['link5']

                        if 'gHttpError' in gsearch:
                            dic['gHttpError'] = gsearch['gHttpError']
                        if 'gDNSLookupError' in gsearch:
                            dic['gDNSLookupError'] = gsearch['gDNSLookupError']
                        if 'gTimeoutError' in gsearch:
                            dic['gTimeoutError'] = gsearch['gTimeoutError']
                        if 'gUnknownError' in gsearch:
                            dic['gUnknownError'] = gsearch['gUnknownError']

                        dic['from_g'] = gsearch['from_g']
                        dic['error'] = gsearch['error']

            full.append(dic)

        #pprint(full)

        with open('combGnP.json', 'w') as outfile:
            json.dump(full, outfile, indent=2)
            outfile.write('\n')

if __name__ == "__main__":
    main(sys.argv)