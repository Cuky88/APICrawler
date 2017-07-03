import jsonlines
import json
import sys
from pprint import pprint


def main(argv):
    lines = []

    cnt_name = 0
    cnt_title = 0
    cnt_error = 0
    cnt = 0
    cnt_id = 0
    cnt_cat = 0

    #with jsonlines.open('gsearch_result_v1.json') as reader:
    with open('gsearch_final.json') as reader:
        read = json.load(reader)
        #for i, api in enumerate(reader):
        for i, api in enumerate(read):
            cnt = i
            if 'api_url' in api:
                cnt_name += 1

            if 'progweb_title' in api:
                cnt_title += 1

            if 'error' in api:
                cnt_error += 1

            if 'id' in api:
                cnt_id += 1

            if 'progweb_cat' in api:
                cnt_cat += 1


        print("Total: " + str(cnt))
        print("Name: " + str(cnt_name))
        print("Title: " + str(cnt_title))
        print("Error: " + str(cnt_error))
        print("ID: " + str(cnt_id))
        print("Cat: " + str(cnt_cat))

if __name__ == "__main__":
    main(sys.argv)
