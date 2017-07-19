import json
import re
import JWriter as fw


#for reading the manual clustering
def format_data(source):
    apis = []
    apis2 = []
    for s in source:
        with open(s) as data_file:
            data = json.load(data_file)
        for x in range(0, len(data)):
            if "id" in data[x] and 'cluster_id' in data[x]:
                apis.append([data[x]['id'], data[x]['cluster_id']])
                apis2.append({"id": data[x]['id'], "cluster_id": data[x]['cluster_id']})
    return [apis,apis2]

#for reading the manual clustering
def load_manual_cluster(dummy):
    source=[]
    source.append('../1_data/4_cluster_single/manuel_cluster/517-eCommerce_clusters_final.json')
    source.append('../1_data/4_cluster_single/manuel_cluster/529-Messaging_clusters.json')
    source.append('../1_data/4_cluster_single/manuel_cluster/113-Payments_clusters.json')

    erg= format_data(source)
    
    #for comparison with Java
    if dummy:
        fw.writeToJson(erg[1], "manualClusters.json")

    #for comparison with Python
    if not dummy:
        return erg[0]


#for reading the clustering through Tag Groups
def load_manual_cluster2():
    with open('/home/caro/Documents/KDD/APICrawler/1_data/3_tag_clustered/tag-clustered-result.json') as data_file:
        data = json.load(data_file)
    manuel = []
    labels = ["Photos","Messaging","Payments"]
    z = 0
    #for x in data:
    for x in labels:
        for i in data[x]:
            if (not(i =="total")) and ("ids" in data[x][i]):
                for id in data[x][i]["ids"]:
                    manuel.append([id,z,i])
                z=z+1

    return manuel
