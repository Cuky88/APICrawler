import RunKMeans


qualityStorage = []

print("******* Clustering Algorithm for Web APIs **********")

dataSet = input("Which data set do you want to cluster?\n  - (1) Linked-Data\n  - (2) Programmable Web\n  - (3) Crawled Data\n")

if dataSet == 1:
    dataSetName = "Linked Data"
elif dataSet == 2:
    dataSetName = "Programmable Web"
elif dataSet == 3:
    dataSetName = "Crawled Data"
else:
    print("Unknown dataset chosen (" + str(dataSet) + ")")
    exit(1)

#K-Means clustering parameter

print("\nStart K-Means-Clustering for Dataset " + dataSetName + "...\n")
#   params[0] => Clustersize, params[1] =>

##dist, k Clusters, n Dimensions
params = [['cosine', 'squared_euclidean'],[1,5,10,20,50,100,300,500,700,1000,2500,5000,7500],[10,100,500]]





#erg = RunKMeans.run(params, dataSet)
RunKMeans.run(params, dataSet)

