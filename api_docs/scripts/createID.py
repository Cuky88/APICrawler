'''
This script creates unique IDs for crawled Progweb data.
See Wiki on Github
'''

import jsonlines
import json
import sys
import os


def main(argv):
    print("******* Create unique IDs for APIs in dataset and filter duplicates **********")

    dataSet = input(
        "Which data set do you want to process?\n  - (1) Programmable Web\n  - (2) Google Crawled Data\n")

    if dataSet == 1:
        dataSetName = "apispider_result.json"
        print("You chose (1) Programmable Web, processing " + dataSetName)
        if not os.path.isfile('./' + dataSetName):
            print("Error, the file you chose does not exist, yet. Please start the apispider crawler. See Github Readme file!")
            exit(1)
        outName = "apispider_result_id.json"
    elif dataSet == 2:
        dataSetName = "gsearch_result.json"
        print("You chose (2) Google Crawled Data, processing " + dataSetName)
        if not os.path.isfile('./' + dataSetName):
            print("Error, the file you chose does not exist, yet. Please start the gsearch crawler. See Github Readme file!")
            exit(1)
        outName = "gsearch_result_id.json"
    else:
        print("Unknown dataset chosen (" + str(dataSet) + ")")
        exit(1)

    lines = []

    cnt_name = 0
    cnt_title = 0
    cnt = 0

    with jsonlines.open(dataSetName) as reader:
    #with open(dataSetName) as reader:
        #read = json.load(reader)
        mem = {}
        for i, api in enumerate(reader):
        #for i, api in enumerate(read):
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


    with open(outName, mode='w') as writer:
        json.dump(lines, writer, indent=2)
        writer.write('\n')
        #writer.write(lines)

if __name__ == "__main__":
    main(sys.argv)
