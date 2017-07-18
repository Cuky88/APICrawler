import Reader

apisManCluster = Reader.load_manual_cluster()

#set of pairs that are in the same cluster
a = []

#set of pairs where only the first api is in the same cluster
b = []

#set of pairs where only the last api is in the same cluster
c = []

#set of pairs where none of apis are in the same cluster
d = []

#set of pairs that does not match any pattern - |e|=0 otherwise an error occured!
e = []

#return in [0] rand staistics and in [1] jaccard coefficient for input cluster and manual cluster
def compare(input):

    apis = []
    for x in range(0, len(input)):
        for y in range(0, len(apisManCluster)):
            if apisManCluster[y][0]==input[x]['id']:
                apis.append([input[x]['id'],input[x]['cluster_id']])

    print("List is: " + str(len(apis)) + ", other list is " + str(len(apisManCluster)))

    #Generate all unique API pairs
    for x in range(0, len(apis)):
        for y in range(len(apis)-1,x,-1):
            if apis[x][0]!=apis[y][0]:
                #print(str(apis[x]) + " vs " + str(apis[y]))
                comparePair(apis[x], apis[y])

    bigM = len(a) + len(b) + len(c) + len(d)
    randStatistics = round((len(a) + len(d)) / bigM,5)
    jaccard = round(len(a) / (len(a)+len(b)+len(c)),5)

    #clear all arrays

    return [randStatistics, jaccard]

#Compair for pair x1, x2 how apis are clustered in manual and in machine approach
def comparePair(x1, x2):

    #Find corresponding pair for x1, x2 in manual clustering

    y=apisManCluster

    y1 = None
    y2 = None

    for i in range(0, len(apisManCluster)):
        if y[i][0]==x1[0]:
            y1=y[0]
        elif y[i][0]==x2[0]:
            y2=y[0]

    #given points haven't been manually cluster -> no quality measureable -> break!
    if y1==None or y2==None:
        return

    # Check if first one of pair is in same cluster (derive Sy or Dy regarding to the paper)
    if x1[1]==x2[1]:
        first=True
    else:
        first=False

    #Check if second part of pair is in same cluster (derive SD|DD, SS|SD)
    if y1[1]==y2[1]:
        second=True
    else:
        second=False

    #Decide to which set the pair contains
    if first and second:
        a.append([x1,x2])
    elif first and not second:
        b.append([x1,x2])

    elif not first and second:
        c.append([x1,x2])

    elif not first and not second:
        d.append([x1,x2])

    else:
        e.append([x1,x2])