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
params = [['cosine', 'squared_euclidean'],[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710,720,730,740,750,760,770,780,790,800,810,820,830,840,850,860,870,880,890,900,910,920,930,940,950,960,970,980,990,1000]]

#erg = RunKMeans.run(params, dataSet)
RunKMeans.run(params, dataSet)

