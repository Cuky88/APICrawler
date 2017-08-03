'''
This script picks 100 random APIs. It was meant to be used for the manual clustering, but was not used at all. It will still remain
in case it could be useful at some time.
'''

from random import randint
import json


#Generate random numbers to pick 100 ids
ids =[]
ids_remove = []

# Select the apis according to the generated id for manually classification
selected = []
with open('manualLinkTestProgweb_62.json') as reader:
    read = json.load(reader)
    for api in read:
        ids_remove.append(api['id'])

with open('progweb_final_filtered.json') as reader:
    read = json.load(reader)
    for x in range(100):
        num = randint(0, 15839)
        if num not in ids:
            if num not in ids_remove:
                ids.append(num)
            else:
                x -= 1
        else:
            x -= 1

    for api in read:
        if api['id'] in ids:
            if api['error'] == 0:
                api['correct_link'] = 2
                selected.append(api)

with open('manualLinkTestProgweb_' + str(len(selected)) + '.json', mode='w') as writer:
    print(len(selected))
    json.dump(selected, writer, indent=2)
    writer.write("\n")