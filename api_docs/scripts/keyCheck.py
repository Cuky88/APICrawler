import json
import sys

def main(argv):
    full = []
    tmp = []

    # add information from google crawling to progweb dataset
    with open('url_test_15877.json') as reader:
        read = json.load(reader)
        for t in read:
            tmp.append(t)

    with open('progweb_final_15838.json') as reader:
        read = json.load(reader)

        for api in read:
            if 'id' not in api:
                api['id'] = 000000

            if 'api_name' not in api:
                api['api_name'] = "NO NAME"

            if 'progweb_cat' not in api:
                api['progweb_cat'] = "NO CATEGORIES"

            if 'progweb_descr' not in api:
                api['progweb_descr'] = "NO DESCRIPTION"

            if 'progweb_title' not in api:
                api['progweb_title'] = "NO TITLE"

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