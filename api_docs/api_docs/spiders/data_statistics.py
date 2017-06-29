import jsonlines
import sys
import time
from pprint import pprint


def main(argv):
    cnt_links = 0
    cnt = 0
    tags = []
    s_t = []

    start_time = time.time()
    with jsonlines.open('apispider_result.json') as reader:
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

    stmt += "Count of all Tags: " + str(len(s_t)) +"\n"
    f_t = list(set(s_t))
    stmt += "Count of unique Tags: " + str(len(f_t)) + "\n"

    stmt += "\nAll Tags:\n"
    for t in f_t:
        stmt += t + "\n"

    print stmt

    with open('stats.txt', mode='w') as writer:
        writer.write(stmt)

if __name__ == "__main__":
    main(sys.argv)
