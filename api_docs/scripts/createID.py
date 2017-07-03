import jsonlines
import json
import sys
from pprint import pprint


def main(argv):
    lines = []

    cnt_name = 0
    cnt_title = 0
    cnt = 0

    #with jsonlines.open('gsearch_final.json') as reader:
    with open('gsearch_final.json') as reader:
        read = json.load(reader)
        mem = {}
        #for i, api in enumerate(reader):
        for i, api in enumerate(read):
            cnt = i
            if 'progweb_title' in api:
                cnt_name += 1
                name = api["progweb_title"]
                if name not in mem:
                    mem[name] = api

                    api['id'] = i

                    lines.append(api)
            if 'progweb_title' in api:
                cnt_title += 1

            #print mem.values()
            #pprint(lines)

        print("Total: " + str(cnt))
        print("Name: " + str(cnt_name))
        print("Title: " + str(cnt_title))

        #pprint(mem.values())


    with open('gsearch_final_filtered.json', mode='w') as writer:
        json.dump(lines, writer, indent=2)
        writer.write('\n')
        #writer.write(lines)

if __name__ == "__main__":
    main(sys.argv)
