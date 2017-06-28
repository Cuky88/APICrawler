import jsonlines
import json
import sys
import urllib2
import httplib
import time
from pprint import pprint


def main(argv):
    lines = []

    with open('dump_v1.json') as reader:
        read = json.load(reader)
        start_time = time.time()
        for i, obj in enumerate(read):
            dic = {}

            if 'api_url' in obj:
                host = obj["api_url"]
                url = obj["api_url_full"]
                title = obj["progweb_title"]

                if title not in lines:
                    dic['api_url'] = host
                    dic['api_url_full'] = url
                    dic['progweb_title'] = title

                    try:
                        a = urllib2.urlopen(url)

                        print(str(i) + " Status: " + str(a.getcode()))

                        dic['error'] = 0

                        lines.append(dic)
                    except (urllib2.HTTPError, ValueError) as e:
                        dic['error'] = 1
                        lines.append(dic)
                        continue
                    except urllib2.URLError as e:
                        dic['error'] = 2
                        lines.append(dic)
                        continue
                    except httplib.BadStatusLine as e:
                        dic['error'] = 3
                        lines.append(dic)
                        continue
                    except:
                        dic['error'] = 4
                        lines.append(dic)
                        continue

    elapsed_time = time.time() - start_time
    print('It took ' + str(elapsed_time) + ' seconds')


    with jsonlines.open('dump.json', mode='w') as writer:
        # json.dump(lines, writer, indent=2)
        # writer.write('\n')
        writer.write(lines)

        # return lines

if __name__ == "__main__":
    main(sys.argv)
