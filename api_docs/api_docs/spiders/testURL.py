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
        for i,obj in enumerate(read):
            dic = {}

            if 'api_url' in obj:
                host = obj["api_url"]
                url = obj["api_url_full"]
                title = obj["progweb_title"]

                # print("OBJ: %s", obj)

                if title not in lines:
                    dic['api_url'] = host
                    dic['api_url_full'] = url
                    dic['progweb_title'] = title

                    try:
                        a = urllib2.urlopen(url)

                        if i % 10 == 0:
                            print(str(i) + " .....Working....Status: " + a.getcode())

                        dic['error'] = 0
                    except (urllib2.HTTPError, ValueError) as e:
                        dic['error'] = 1
                        continue
                    except urllib2.URLError as e:
                        dic['error'] = 2
                        continue
                    except httplib.BadStatusLine as e:
                        dic['error'] = 3
                        continue
                    except:
                        dic['error'] = 4
                        continue

                    lines.append(dic)
                    # print("LINES: %s", lines)

    with jsonlines.open('dump.json', mode='w') as writer:
        # json.dump(lines, writer, indent=2)
        # writer.write('\n')
        writer.write(lines)

        # return lines


if __name__ == "__main__":
    main(sys.argv)
