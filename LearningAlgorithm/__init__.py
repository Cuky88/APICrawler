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
params = [['cosine', 'squared_euclidean'],[20, 50, 100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 5000]]
erg = RunKMeans.run(params, dataSet)

