import json

def writeToJson(input, name):
    path="results/" + name
    with open(path,mode="w") as writer:
        json.dump(input, writer, indent=2)
        writer.write("\n")