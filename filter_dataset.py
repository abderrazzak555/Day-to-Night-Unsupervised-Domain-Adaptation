# -*- coding: utf-8 -*-

import json
import glob

def main():

    result = {}

    for f in glob.glob("/home/abderrazzak/Desktop/test_json/*.json"):
        with open(f, "rb") as infile:
            jsonFile = json.load(infile)
            keys = jsonFile.keys()
            for key in keys:
                currentProduct = jsonFile[key]
                result[key] = currentProduct

    with open("mergedFile.json", "wb") as outfile:
        json.dump(result, outfile)

if __name__ == '__main__':
    main()
