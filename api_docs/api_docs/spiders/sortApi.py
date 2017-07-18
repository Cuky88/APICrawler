from random import randint
import json

# Generate random numbers to pick 100 ids
# ids =[]
#
# for x in range(100):
#     num = randint(0, 15878)
#     if num not in ids:
#         ids.append(num)
#     else:
#         x -= 1

# Sort the api list
sorted = []
ids =[]
with open('tagcount_result_v2.json') as reader:
    read = json.load(reader)
    for tag in read:
        sorted.append(tag)

def extract_total(json):
    try:
        return int(json['total'])
    except KeyError:
        return 0

sorted.sort(key=extract_total, reverse=True)

print(len(sorted))

# Extract api ids from the top 5 biggest tags
for i, entry in enumerate(sorted):
    if i < 5:
        print(entry['progweb_cat'])
        for id in entry['api']:
            ids.append(id['id'])

# Select the apis according to the generated id for manually classification
selected = []

with open('../api_docs/progweb_final_filtered.json') as reader:
    read = json.load(reader)
    for api in read:
        if api['id'] in ids:
            selected.append(api)

with open('selected_cuky.json', mode='w') as writer:
    json.dump(selected, writer, indent=2)
    writer.write("\n")