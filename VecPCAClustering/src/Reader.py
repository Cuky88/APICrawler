import json
import re
import numpy
from DataSet import DataSet


def load_descr(dataset):
    apiNr = []
    descr = []
    namen = []

    #load Programmable Web descriptions
    if dataset == "prog":
        with open('/home/caro/Documents/KDD/VecPCAClustering/resources/ProgWeb_preprocessed.json') as data_file:
            data = json.load(data_file)

        for x in xrange(0, len(data)):
            if ("id" in data[x]) & ("progweb_descr" in data[x]) & ("api_name" in data[x]):
                apiNr.append(data[x]["id"])
                namen.append(data[x]["api_name"])

                text = data[x]["progweb_descr"]
                #remove all digets
                output = re.sub(r'\d+', '', text)
                descr.append(output)

                dsJson = DataSet(apiNr, descr, namen)
        return dsJson

    else:
        with open('/home/caro/Documents/APICrawler/VecPCAClustering/resources/complete.json') as data_file:
            data = json.load(data_file)

        for x in xrange(0, len(data)):
            if "id" in data[x] & ("descr1" in data[x] | "descr2" in data[x] | "descr3" in data[x] | "descr4" in data[x] | "descr5" in data[x]):
                apiNr.append(data[x]["id"])
                text = ""
                if "descr1" in data[x]:
                    text = text + " " +data[x].get("descr1")
                if "descr2" in data[x]:
                    text = text + " " +data[x].get("descr2")
                if "descr3" in data[x]:
                    text = text + " " +data[x].get("descr3")
                if "descr4" in data[x]:
                    text = text + " " +data[x].get("descr4")
                if "descr5" in data[x]:
                    text = text + " " +data[x].get("descr5")

                # remove all digets
                output = re.sub(r'\d+', '', text)
                descr.append(output)
                dsJson = DataSet(apiNr, descr)

        return dsJson




