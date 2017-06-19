import json
import json_lines as jsonlines
import sys
from pprint import pprint


def main(argv):

    full = {}
    final = {}

    f_progweb = jsonlines.open('apispider_result_v1.json')
    #f_google = jsonlines.open('gsearch_result_v1.json')
    f_sites = jsonlines.open('apidescr_result_v1.json')



    with open('apidescr_result_v1.json') as reader:
        tmp = json.load(reader)

    with jsonlines.open('apispider_result_v1.json') as reader:
        for i,api in enumerate(reader):
            id = str(i)
            full[id] = {}
            full[id]['api_name'] = api['api_name']
            full[id]['progweb_url'] = api['progweb_url']
            full[id]['progweb_cat'] = api['progweb_cat']
            full[id]['progweb_date'] = api['progweb_date']
            full[id]['crawled_date'] = api['crawled_date']
            full[id]['api_url'] = api['api_url']
            full[id]['progweb_descr'] = api['progweb_descr']
            full[id]['progweb_url'] = api['progweb_url']

            cnt = 0

            for descr in tmp:
                if api['api_url'] == descr['api_name']:
                    cnt += 1

            for descr in tmp:
                if api['api_url'] == descr['api_name']:
                    if cnt >= 0:
                        print(descr['api_name'])
                        print (cnt)
                        link_str = "link" + str(cnt)
                        descr_str = "descr" + str(cnt)
                        full[id][link_str] = descr['link']
                        full[id][descr_str] = descr['descr']

                        cnt -= 1

            #final.update({id:full})

        with open('final.json', 'w') as outfile:
            json.dump(full, outfile, indent=2)
            outfile.write('\n')

if __name__ == "__main__":
    main(sys.argv)