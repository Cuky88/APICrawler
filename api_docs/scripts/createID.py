import jsonlines
import json
import sys
from pprint import pprint


def main(argv):
    lines = []

    with jsonlines.open('apispider_result.json') as reader:
        for i, obj in enumerate(reader):

            if 'id' in obj:
                obj['id'] = i

            lines.append(obj)
            #print(obj)

    with open('progweb_final.json', mode='w') as writer:
        json.dump(lines, writer, indent=2)
        writer.write('\n')
        #writer.write(lines)




if __name__ == "__main__":
    main(sys.argv)
