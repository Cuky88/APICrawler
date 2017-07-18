import json
import re
from DSet import DataSet


def load_descr(dataset):
    apiNr = []
    descr = []
    name = []

    #load Programmable Web descriptions
    if dataset == 2:
        with open('../1_data/2_preprocessed/progweb_preprocessed.json') as data_file:
            data = json.load(data_file)

        for x in xrange(0, len(data)):
            if ("id" in data[x]) & ("progweb_descr" in data[x]) & ("api_name" in data[x]):
                apiNr.append(data[x]["id"])
                name.append(data[x]["api_name"])

                text = data[x]["progweb_descr"]
                #remove all digets
                output = re.sub(r'\d+', '', text)
                descr.append(output)

                dsJson = DataSet(apiNr, descr, name)
        return dsJson

    elif dataset == 3:
        with open('../1_data/2_preprocessed/complete_final.json') as data_file:
            data = json.load(data_file)

        for x in xrange(0, len(data)):
            if "id" in data[x] and ("descr1" in data[x] or "descr2" in data[x] or "descr3" in data[x] or "descr4" in data[x] or "descr5" in data[x]):
                apiNr.append(data[x]["id"])
                name.append(data[x]["api_name"])

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
                dsJson = DataSet(apiNr, descr, name)

        return dsJson
