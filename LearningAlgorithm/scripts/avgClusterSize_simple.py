import json
tmp = {}

with open("../results/final_results/1_run/kmeansresults/squared_euclidean_300_500.json", "rw") as reader:
    read = json.load(reader)

    for api in read:
        num = api["cluster_id"]
        if num in tmp:
            tmp[num] += 1
        else:
            tmp[num] = 1

print(len(tmp))
