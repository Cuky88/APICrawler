import json
import re


def load_descr():
    with open('/home/caro/PycharmProjects/KDD/resources/final.json') as data_file:
        data = json.load(data_file)
    descr=[]

    for x in xrange(0, len(data)):
        if data[str(x)].get("progweb_descr"):
            text = data[str(x)]["progweb_descr"]
            output = re.sub(r'\d+', '', text)
            descr.append(output)
    return descr


