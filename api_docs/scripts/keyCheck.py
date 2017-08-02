import json
import sys
import unicodedata

def main(argv):
    full = []
    tmp = []

    # add information from google crawling to progweb dataset
    with open('url_test.json') as reader:
        read = json.load(reader)
        for t in read:
            tmp.append(t)

    with open('apispider_results_id.json') as reader:
        read = json.load(reader)

        for api in read:
            if 'id' not in api:
                api['id'] = 000000

            if 'api_name' not in api:
                api['api_name'] = "NO NAME"
            else:
                api['api_name'] = unicodedata.normalize('NFKD', api['api_name']).encode('ascii', 'ignore')
                api['api_name'] = api['api_name'].replace('\"', r"'")

            if 'progweb_cat' not in api:
                api['progweb_cat'] = "NO CATEGORIES"

            if 'progweb_descr' not in api:
                api['progweb_descr'] = "NO DESCRIPTION"
            else:
                api['progweb_descr'] = unicodedata.normalize('NFKD', api['progweb_descr']).encode('ascii', 'ignore')
                api['progweb_descr'] = api['progweb_descr'].replace('\"', r"'")

            if 'progweb_title' not in api:
                api['progweb_title'] = "NO TITLE"
            else:
                api['progweb_title'] = unicodedata.normalize('NFKD', api['progweb_title']).encode('ascii', 'ignore')
                api['progweb_title'] = api['progweb_title'].replace('\"', r"'")

            if 'progweb_url' not in api:
                api['progweb_url'] = "NO PROGWEBURL"

            if 'api_url' not in api:
                api['api_url'] = "NO URL"

            if 'api_url_full' not in api:
                api['api_url_full'] = "NO FULL-URL"

            if 'progweb_date' not in api:
                api['progweb_date'] = "01.01.2020"

            api['error'] = 5

            for test in tmp:
                if api['progweb_title'] == test['progweb_title']:
                    api['error'] = test['error']

            full.append(api)

        with open('progweb_final_filtered.json', 'w') as outfile:
            json.dump(full, outfile, indent=2)
            outfile.write('\n')

if __name__ == "__main__":
    main(sys.argv)