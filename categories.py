#!/usr/bin/python3

import pandas as pd
import re

# Purpose is to compare the categories of items
# Number of categories is variable, but is

file = open('amazon-meta.txt', "r", encoding="utf8")

def stripCategories():
    dataframeTwo = []
    itemCategories = []
    index = 1

    for i in range (0, 15010574):
        readLine = file.readline().splitlines()
        step0 = readLine[0].split('|')
        #print(step0)
        step1 = step0[0].split(':')

        if(len(step0) == 1 and len(itemCategories) != 0):
            # pass most lines
            #itemCategories.insert(0, index)
            pass
        # and portion is for aiding in splitting dataset into .csv files
        elif(len(step0) > 1 and int(index) >= 352638):
            step0[0] = index
            #print(step0)
            # Fill out graph to be 12 columns
            # by filling in blank spaces with 0
            if(len(step0) < 12):
                for j in range(len(step0), 12):
                    step0.append(0);

            for item in step0:
                itemCategories.append(item)
            # we want to fill out the graph;
            # all products have 5-11 categories
            dataframeTwo.append(itemCategories)
            itemCategories = []
        elif(step1[0] == 'Id'):
            #index WHICH category goes to which product
            index = step1[1]
            #print(index)
    file.close()
    return dataframeTwo

if __name__ == '__main__':
    data = stripCategories()
    #
    df = pd.DataFrame(data, columns=["prodIndex", "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi"])
    #print(df)
    filename = 'categories3.csv'
    df.to_csv(filename)

    # Finished (note: add 1 to index and change categoriesx.csv name)
    # 0, 5323380 categories1 index = 194827
    # 5323380, 9419026 categories2 index = 352637
    # 9419026 15010574 categories3 index =



