import itertools
import VecPCAClustering

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
    print("\nStart Density-Clustering  for Dataset " + dataSetName + "...\n")
    #   params[0] => Clustersize, params[1] => ?
    params = [[3,5,10,25,50,100,350,500,1000,5000,10000],[20,30,40,50]]
else:
    exit(1)


#call algorithm with parameter, dataset, algorithm in for loop, store results
for i in params[0]:
  param1 = i
  for j in params[1]:
       param2 = j
       print("Starting clustering for parameter " + str(param1) + " and parameter " + str(param2) + "...")

