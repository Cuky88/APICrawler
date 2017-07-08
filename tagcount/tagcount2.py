import json
import sys


def progweb(filename):
    loaded = []
    tags = []
    tmp = []
    prime = []
    second = []
    final = []

    with open('../api_docs/' + filename) as reader:
        read = json.load(reader)
        for api in read:
            loaded.append(api)

            tags.append(api['progweb_cat'])
            prime.append(api['progweb_cat'].split(',')[0])
            second.append(api['progweb_cat'].split(',')[1:])


    with open('u_tags.json') as reader:
        read = json.load(reader)
        for tag in read:

            dic = {'progweb_cat': tag, 'total': 0, 'api': []}
            for api in loaded:
                if api['progweb_cat'] == tag:

                    dic['total'] += 1
                    dic['api'].append({'id': api['id'], 'progweb_title': api['progweb_title']})

            final.append(dic)

    with open('tagcount_result_v2.json', mode='w') as writer:
        json.dump(final, writer, indent=2)
        writer.write("\n")

    # Code to get unique tag combinations; used to generate u_tags.json and then commented!
    #for t in tags:
    #    if t not in tmp:
    #        tmp.append(t)

    # pp(prime)
    # print(len(prime))

    # pp(second)
    # print(len(second))

    # Print unique tags
    #with open('u_tags.json', mode='w') as writer:
    #    json.dump(tmp, writer, indent=2)
    #    writer.write("\n")


def main(argv):
    filename = 'progweb_final_filtered.json'
    progweb(filename)


if __name__ == "__main__":
    main(sys.argv)
