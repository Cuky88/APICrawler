import jsonlines
import json
import sys
import time


def progweb(filename):
    counter = {'total': 0, 'id': 0, 'api_name': 0, 'progweb_cat': 0, 'progweb_descr': 0, 'progweb_title': 0,
               'progweb_url': 0, 'api_url': 0, 'api_url_full': 0, 'progweb_date': 0}

    tags = []
    s_t1 = []
    s_t2 = []

    start_time = time.time()
    with open(filename) as reader:
        read = json.load(reader)
        for i, api in enumerate(read):
            counter['total'] += 1

            if api['id'] == 000000:
                counter['id'] += 1

            if api['api_name'] == "NO NAME":
                counter['api_name'] += 1

            if api['progweb_cat'] == "NO CATEGORIES":
                counter['progweb_cat'] += 1

            if api['progweb_descr'] == "NO DESCRIPTION":
                counter['progweb_descr'] += 1

            if api['progweb_title'] == "NO TITLE":
                counter['progweb_title'] += 1

            if api['progweb_url'] == "NO PROGWEBURL":
                counter['progweb_url'] += 1

            if api['api_url'] == "NO URL":
                counter['api_url'] += 1

            if api['api_url_full'] == "NO FULL-URL":
                counter['api_url_full'] += 1

            if api['progweb_date'] == "01.01.2020":
                counter['progweb_date'] += 1

            tags.append(api['progweb_cat'])

    elapsed_time = time.time() - start_time
    stmt = 'It took ' + str(elapsed_time) + ' seconds\n'
    stmt += "##########################################\n"
    stmt += "Crawled data from ProgrammableWeb\n"
    stmt += "##########################################\n"
    stmt += "Count of total APIs: " + str(counter['total']) + "\n"
    stmt += "Count of APIs with url from programmableweb: " + str(counter['total'] - counter['api_url_full']) + "\n"
    stmt += "Count of APIs with categories: " + str(counter['total'] - counter['progweb_cat']) + "\n"
    stmt += "Count of APIs with description: " + str(counter['total'] - counter['progweb_descr']) + "\n\n"

    for t in tags:
        for w in t.split(','):
            s_t1.append(w)

            if "NO CATEGORIES" not in w:
                s_t2.append(w)

    stmt += "Count of all Tags (dummy included): " + str(len(s_t1)) + "\n"
    stmt += "Count of all Tags (dummy not included): " + str(len(s_t2)) + "\n"
    f_t = list(set(s_t2))
    stmt += "Count of unique Tags: " + str(len(f_t)) + "\n"

    stmt += "\nAll Tags:\n"
    for t in f_t:
        stmt += t + "\n"

    outname = filename + '_stats.txt'

    with open(outname, mode='w') as writer:
        writer.write(stmt)


def statistics(filename):
    cnt_links = 0
    cnt = 0
    tags = []
    s_t = []

    start_time = time.time()
    with jsonlines.open(filename) as reader:
        for i, obj in enumerate(reader):
            cnt += 1

            if 'api_url_full' in obj:
                cnt_links += 1

            if 'progweb_cat' in obj:
                tags.append(obj['progweb_cat'])

    elapsed_time = time.time() - start_time
    stmt = 'It took ' + str(elapsed_time) + ' seconds\n'
    stmt += "##########################################\n"
    stmt += "Count of APIs: " + str(cnt) + "\n"
    stmt += "Count of APIs with url: " + str(cnt_links) + "\n\n"

    for t in tags:
        for w in t.split(','):
            s_t.append(w)

    stmt += "Count of all Tags: " + str(len(s_t)) + "\n"
    f_t = list(set(s_t))
    stmt += "Count of unique Tags: " + str(len(f_t)) + "\n"

    stmt += "\nAll Tags:\n"
    for t in f_t:
        stmt += t + "\n"

    # print stmt

    outname = filename + '_stats.txt'

    with open(outname, mode='w') as writer:
        writer.write(stmt)


def main(argv):
    filename1 = 'apispider_result_v2.json'
    statistics(filename1)

    filename2 = 'progweb_final_filtered.json'
    progweb(filename2)


if __name__ == "__main__":
    main(sys.argv)

