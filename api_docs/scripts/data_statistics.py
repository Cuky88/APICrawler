'''
This script gives a overview of the crawled data and some statistics. It needs to be adjusted if you want to run it, e.g. data reading etc.
'''

import jsonlines
import json
import sys
import time


def progweb(filename):
    counter = {'total': 0, 'id': 0, 'api_name': 0, 'progweb_cat': 0, 'progweb_descr': 0, 'progweb_title': 0,
               'progweb_url': 0, 'api_url': 0, 'api_url_full': 0, 'progweb_date': 0, 'err0': 0, 'err1': 0,
               'err2': 0, 'err3': 0, 'err4': 0, 'err5': 0, 'from_g': 0}

    tags = []
    s_t1 = []
    s_t2 = []

    start_time = time.time()
    with open(filename) as reader:
        read = json.load(reader)
        for i, api in enumerate(read):
            counter['total'] += 1

            if 'id' in api:
                if api['id'] == 000000:
                    counter['id'] += 1

            if 'api_name' in api:
                if api['api_name'] == "NO NAME":
                    counter['api_name'] += 1

            if 'progweb_cat' in api:
                if api['progweb_cat'] == "NO CATEGORIES":
                    counter['progweb_cat'] += 1

                tags.append(api['progweb_cat'])

            if 'progweb_descr' in api:
                if api['progweb_descr'] == "NO DESCRIPTION":
                    counter['progweb_descr'] += 1

            if 'progweb_title' in api:
                if api['progweb_title'] == "NO TITLE":
                    counter['progweb_title'] += 1

            if 'progweb_url' in api:
                if api['progweb_url'] == "NO PROGWEBURL":
                    counter['progweb_url'] += 1

            if 'api_url' in api:
                if api['api_url'] == "NO URL":
                    counter['api_url'] += 1

            if 'api_url_full' in api:
                if api['api_url_full'] == "NO FULL-URL":
                    counter['api_url_full'] += 1

            if 'progweb_date' in api:
                if api['progweb_date'] == "01.01.2020":
                    counter['progweb_date'] += 1

            if 'error' in api:
                if api['error'] == 0:
                    counter['err0'] += 1

                if api['error'] == 1:
                    counter['err1'] += 1

                if api['error'] == 2:
                    counter['err2'] += 1

                if api['error'] == 3:
                    counter['err3'] += 1

                if api['error'] == 4:
                    counter['err4'] += 1

                if api['error'] == 5:
                    counter['err5'] += 1

            if 'from_g' in api:
                if api['from_g'] == 1:
                    counter['from_g'] += 1


    elapsed_time = time.time() - start_time
    stmt = 'It took ' + str(elapsed_time) + ' seconds\n'
    stmt += "##########################################\n"
    stmt += "Crawled data from ProgrammableWeb\n"
    stmt += "##########################################\n"
    stmt += "Count of total APIs: " + str(counter['total']) + "\n"
    stmt += "Count of APIs with url from programmableweb: " + str(counter['total'] - counter['api_url_full']) + "\n"
    stmt += "Count of APIs w/o url from programmableweb: " + str(counter['api_url_full']) + "\n"
    stmt += "Count of APIs with categories: " + str(counter['total'] - counter['progweb_cat']) + "\n"
    stmt += "Count of APIs with description: " + str(counter['total'] - counter['progweb_descr']) + "\n"
    stmt += "Count of APIs w/o description: " + str(counter['progweb_descr']) + "\n\n"

    for t in tags:
        for w in t.split(','):
            s_t1.append(w)

            if "NO CATEGORIES" not in w:
                s_t2.append(w)

    stmt += "Count of all Tag-Combination: " + str(len(s_t2)) + "\n"
    stmt += "Count of missing Tags: " + str(len(s_t1) - len(s_t2)) + "\n\n"

    stmt += "Links w/o error: " + str(counter['err0']) + "\n"
    stmt += "Links with HTTPError: " + str(counter['err1']) + "\n"
    stmt += "Links with URLError: " + str(counter['err2']) + "\n"
    stmt += "Links with BadStatusLine: " + str(counter['err3']) + "\n"
    stmt += "Links with unknown error: " + str(counter['err4']) + "\n"
    stmt += "Links not verified: " + str(counter['err5']) + "\n"
    if counter['from_g'] > 0:
        stmt += "Links found from Google: " + str(counter['from_g']) + "\n"

    # f_t = list(set(s_t2))
    # stmt += "Count of unique Tags: " + str(len(f_t)) + "\n"
    # stmt += "\nAll Tags:\n"
    # for t in f_t:
    #     stmt += t + "\n"

    outname = filename + '_stats.txt'

    with open(outname, mode='w') as writer:
        writer.write(stmt)


def statistics(filename):
    counter = {'total': 0, 'id': 0, 'api_name': 0, 'progweb_cat': 0, 'progweb_descr': 0, 'progweb_title': 0,
               'progweb_url': 0, 'api_url': 0, 'api_url_full': 0, 'progweb_date': 0, 'err0': 0, 'err1': 0,
               'err2': 0, 'err3': 0, 'err4': 0, 'err5': 0, 'from_g': 0, 'link1': 0, 'link2': 0, 'link3': 0, 'link4': 0,
               'link5': 0, 'descr1': 0, 'descr2': 0, 'descr3': 0, 'descr4': 0, 'descr5': 0}

    tags = []
    s_t1 = []
    s_t2 = []

    start_time = time.time()
    with open(filename) as reader:
        read = json.load(reader)
        for i, api in enumerate(read):
            counter['total'] += 1

            if 'id' in api:
                if api['id'] == 000000:
                    counter['id'] += 1

            if 'api_name' in api:
                if api['api_name'] == "NO NAME":
                    counter['api_name'] += 1

            if 'progweb_cat' in api:
                if api['progweb_cat'] == "NO CATEGORIES":
                    counter['progweb_cat'] += 1

                tags.append(api['progweb_cat'])

            if 'progweb_descr' in api:
                if api['progweb_descr'] == "NO DESCRIPTION":
                    counter['progweb_descr'] += 1

            if 'progweb_title' in api:
                if api['progweb_title'] == "NO TITLE":
                    counter['progweb_title'] += 1

            if 'progweb_url' in api:
                if api['progweb_url'] == "NO PROGWEBURL":
                    counter['progweb_url'] += 1

            if 'api_url' in api:
                if api['api_url'] == "NO URL":
                    counter['api_url'] += 1

            if 'api_url_full' in api:
                if api['api_url_full'] == "NO FULL-URL":
                    counter['api_url_full'] += 1

            if 'progweb_date' in api:
                if api['progweb_date'] == "01.01.2020":
                    counter['progweb_date'] += 1

            if 'error' in api:
                if api['error'] == 0:
                    counter['err0'] += 1

                if api['error'] == 1:
                    counter['err1'] += 1

                if api['error'] == 2:
                    counter['err2'] += 1

                if api['error'] == 3:
                    counter['err3'] += 1

                if api['error'] == 4:
                    counter['err4'] += 1

                if api['error'] == 5:
                    counter['err5'] += 1

            if 'from_g' in api:
                if api['from_g'] == 1:
                    counter['from_g'] += 1

            if 'link1' in api:
                counter['link1'] += 1

            if 'link2' in api:
                counter['link2'] += 1

            if 'link3' in api:
                counter['link3'] += 1

            if 'link4' in api:
                counter['link4'] += 1

            if 'link5' in api:
                counter['link5'] += 1

            if 'descr1' in api:
                counter['descr1'] += 1

            if 'descr2' in api:
                counter['descr2'] += 1

            if 'descr3' in api:
                counter['descr3'] += 1

            if 'descr4' in api:
                counter['descr4'] += 1

            if 'descr5' in api:
                counter['descr5'] += 1


    elapsed_time = time.time() - start_time
    stmt = 'It took ' + str(elapsed_time) + ' seconds\n'
    stmt += "##########################################\n"
    stmt += "Crawled data from ProgrammableWeb\n"
    stmt += "##########################################\n"
    stmt += "Count of total APIs: " + str(counter['total']) + "\n"
    stmt += "Count of APIs with url from programmableweb: " + str(counter['total'] - counter['api_url_full']) + "\n"
    stmt += "Count of APIs w/o url from programmableweb: " + str(counter['api_url_full']) + "\n"
    stmt += "Count of APIs with categories: " + str(counter['total'] - counter['progweb_cat']) + "\n"
    stmt += "Count of APIs with description: " + str(counter['total'] - counter['progweb_descr']) + "\n"
    stmt += "Count of APIs w/o description: " + str(counter['progweb_descr']) + "\n\n"

    for t in tags:
        for w in t.split(','):
            s_t1.append(w)

            if "NO CATEGORIES" not in w:
                s_t2.append(w)

    stmt += "Count of all Tag-Combination: " + str(len(s_t2)) + "\n"
    stmt += "Count of missing Tags: " + str(len(s_t1) - len(s_t2)) + "\n\n"

    stmt += "Links w/o error: " + str(counter['err0']) + "\n"
    stmt += "Links with HTTPError: " + str(counter['err1']) + "\n"
    stmt += "Links with URLError: " + str(counter['err2']) + "\n"
    stmt += "Links with BadStatusLine: " + str(counter['err3']) + "\n"
    stmt += "Links with unknown error: " + str(counter['err4']) + "\n"
    stmt += "Links not verified: " + str(counter['err5']) + "\n"
    if counter['from_g'] > 0:
        stmt += "Links found from Google: " + str(counter['from_g']) + "\n"
    stmt += "Count of Link1: " + str(counter['link1']) + "\n"
    stmt += "Count of Link2: " + str(counter['link2']) + "\n"
    stmt += "Count of Link3: " + str(counter['link3']) + "\n"
    stmt += "Count of Link4: " + str(counter['link4']) + "\n"
    stmt += "Count of Link5: " + str(counter['link5']) + "\n"
    stmt += "Count of Descr1: " + str(counter['descr1']) + "\n"
    stmt += "Count of Descr2: " + str(counter['descr2']) + "\n"
    stmt += "Count of Descr3: " + str(counter['descr3']) + "\n"
    stmt += "Count of Descr4: " + str(counter['descr4']) + "\n"
    stmt += "Count of Descr5: " + str(counter['descr5']) + "\n"

    # f_t = list(set(s_t2))
    # stmt += "Count of unique Tags: " + str(len(f_t)) + "\n"
    # stmt += "\nAll Tags:\n"
    # for t in f_t:
    #     stmt += t + "\n"

    outname = filename + '_stats.txt'

    with open(outname, mode='w') as writer:
        writer.write(stmt)


def main(argv):
    filename = 'zwischenspeicher/bckp/apidescr_result_v1.json'
    statistics(filename)

    #filename1 = 'progweb_final_filtered.json'
    #progweb(filename1)

    #filename2 = 'complete_final.json'
    #progweb(filename2)

    #filename3 = 'zwischenspeicher/bckp/gsearch_final.json'
    #progweb(filename3)


if __name__ == "__main__":
    main(sys.argv)

