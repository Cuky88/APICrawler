import Comparator

data = [{'id': 878, 'name' : 'API Name', 'cluster_id': 1},{'id': 233, 'name' : 'API2', 'cluster_id':1},{'id': 313, 'name' : 'API3', 'cluster_id':2},{'id': 1023, 'name' : 'API4', 'cluster_id':555},{'id': 571, 'name' : 'API5', 'cluster_id':666}, {'id': 621, 'name' : 'API6', 'cluster_id':333}, {'id': 777, 'name': 'API7','cluster_id':777}]

qualityStorage = []

print("******* Clustering Algorithm for Web APIs **********")

dataSet = input("Which data set do you want to cluster?\n  - (1) Linked-Data\n  - (2) Programmable Web\n  - (3) Crawled Data\n")

if dataSet=="1":
    dataSetName="Linked Data"
elif dataSet=="2":
    dataSetName="Programmable Web"
elif dataSet=="3":
    dataSetName="Crawled Data"
else:
    print("Unknown dataset chosen (" + str(dataSet) + ")")
    exit(1)


clusterAlgo = input("Which algorithm do you want to use?\n  - (1) K-Means-Clustering\n  - (2) Density-Clustering\n")

#K-Means clustering parameter
if clusterAlgo=="1":
    print("\nStart K-Means-Clustering for Dataset " + dataSetName + "...\n")
    #   params[0] => Clustersize, params[1] => ?
    params = [[3,5,10,25,50,100,350,500,1000,5000,10000],[20,30,40,50]]

#density clustering parameter
elif clusterAlgo=="2":
    print("\nStart Density-Clustering for Dataset " + dataSetName + "...\n")
    #   params[0] => Clustersize, params[1] => ?
    params = [[3,5,10,25,50,100,350,500,1000,5000,10000],[20,30,40,50]]
else:
    exit(1)

#call algorithm with parameter, dataset, algorithm in for loop, store results
for i in params[0]:
  param1 = i
  for j in params[1]:
       param2 = j
       quality = Comparator.compare(data)
       qualityStorage.append([quality,[param1, param2]])

       #print("Starting clustering for parameter " + str(param1) + " and parameter " + str(param2) + "...")

quality = qualityStorage[0]

for i in range(0, len(qualityStorage)):
    print("Parameter (#Cluster (k) => " + str(qualityStorage[i][1][0]) + ", #Improvementiterations (n) => " + str(qualityStorage[i][1][1]) + " has quality: Rand statistics " + str(qualityStorage[i][0][0]) + " and Jaccard Coeffcient " + str(qualityStorage[i][0][1]))
    #Look for best parameter due to Jaccard Coeff
    if quality[0][1] > qualityStorage[i][0][1]:
        quality = qualityStorage[i]

print("\n\n--> Best quality found for Jaccard Coeff: " + str(quality[1][1]) + " and Parameter k=" + str(quality[0][0]) + ", n=" + str(quality[0][1]))