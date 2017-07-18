import json
import re
import JWriter as fw

#for reading the manual clustering
def load_manual_cluster(dummy):
    with open('../1_data/4_cluster_single/manuel_cluster/517-eCommerce_clusters_final.json') as data_file:
        data = json.load(data_file)
    apis=[]

    for x in range(0, len(data)):
        if "id" in data[x] and 'cluster_id' in data[x]:
            apis.append([data[x]['id'], data[x]['cluster_id']])

    with open('../1_data/4_cluster_single/manuel_cluster/529-Messaging_clusters.json') as data_file:
        data = json.load(data_file)

    for x in range(0, len(data)):
        if "id" in data[x] and 'cluster_id' in data[x]:
            apis.append([data[x]['id'], data[x]['cluster_id']])
            
    with open('../1_data/4_cluster_single/manuel_cluster/113-Payments_clusters.json') as data_file:
        data = json.load(data_file)

    for x in range(0, len(data)):
        if "id" in data[x] and 'cluster_id' in data[x]:
            apis.append([data[x]['id'], data[x]['cluster_id']])
    
    if dummy:
        fw.writeToJson(apis, "manualClusters.json")
    
    if not dummy:
        return apis

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
