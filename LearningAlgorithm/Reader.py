import json
import JWriter as fw

#for reading the manual clustering
def format_data(source, toDelete):
    apis = []
    apis2 = []
    for s in source:
        with open(s) as data_file:
            data = json.load(data_file)
        for x in range(0, len(data)):
            if "id" in data[x] and 'cluster_id' in data[x]:
                if str(data[x]['cluster_id']) not in toDelete:
                    apis.append([data[x]['id'], data[x]['cluster_id']])
                    apis2.append({"id": data[x]['id'], "cluster_id": data[x]['cluster_id']})
    return [apis,apis2]

#for reading the manual clustering
def load_manual_cluster(dummy):
    source=[]
    source.append('../1_data/4_cluster_single/manuel_cluster/399-eCommerce_clusters_final.json')
    source.append('../1_data/4_cluster_single/manuel_cluster/529-Messaging_clusters.json')
    source.append('../1_data/4_cluster_single/manuel_cluster/113-Payments_clusters.json')
    source.append('../1_data/4_cluster_single/manuel_cluster/32-Mapping_clusters.json')
    source.append('../1_data/4_cluster_single/manuel_cluster/31-Financial_clusters.json')
    # Clusters with less then 5 apis will be deleted
    toDelete = '../1_data/4_cluster_single/manuel_cluster/IDToDelete.json'

    erg= format_data(source, toDelete)
    
    #for comparison with Java
    if dummy:
        fw.writeToJson(erg[1], "manualClusters.json")

    #for comparison with Python
    if not dummy:
        return erg[0]