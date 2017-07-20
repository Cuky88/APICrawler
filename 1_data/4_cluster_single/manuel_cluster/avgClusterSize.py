import json
import sys


def main(argv):
    leng = 0
    cnt = 0

    with open('BigClusterApiStats.json') as reader:
        read = json.load(reader)
        for t in read:
            cnt += 1
            leng += t['cnt']


    avg_size = leng / cnt
    print("Avg. Size of Cluster: ", avg_size)

    file = 'avgClusterSize.json'

    with open(file, mode='w') as writer:
        json.dump(avg_size, writer, indent=2)
        writer.write('\n')


if __name__ == "__main__":
    main(sys.argv)
