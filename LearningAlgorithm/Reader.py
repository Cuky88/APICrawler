import json
import re

def load_manual_cluster():
    # TO-DO
    with open('/home/jan-peter/PycharmProjects/APICrawler/LearningAlgorithm/resources/manual_cluster.json') as data_file:
        data = json.load(data_file)
    apis=[]

    for x in range(0, len(data)):
        apis.append([data[x]['id'], data[x]['cluster_id']])
    return apis
