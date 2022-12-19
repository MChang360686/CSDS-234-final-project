#!/usr/bin/python3

import pandas as pd
import numpy as np

# Open file
file = open('amazon-meta.txt', "r", encoding="utf8")


# The idea is to use NL/completely blank line to chunk the data?
# Next parse other data i.e. separate by : and ' '

# If you can find the customer name key, you could probably figure
# out the co-purchasing stuff too.

# Need to create a mutable object from scratch within the loop according to
#https://sopython.com/canon/128/appending-in-a-loop-creates-a-list-of-unexpected-duplicates/
# The fix is to use a for i in range() loop, not a while loop

def concatWithComma(string1, string2):
    return string1 + ',' + string2
    pass

def parseData():
    dataframe = []
    currentItem = []

    # range is 0 to 15010574
    for i in range(0, 15010574):
        readLine = file.readline().splitlines()
        #print(f" readline: {readLine}")
        step0 = readLine[0].split(':')
        step1 = [item.strip() for item in step0]
        step2 = step1[0].split(' ')


        if(step1[0] == ''):
            #append to list on blank line
            dataframe.append(currentItem)
            #print(f"dataframe: {dataframe}")
            currentItem = []
            pass
        elif(step1[0] == 'Id'):
            #print(step1[1])
            currentItem.append(step1[1])
            pass
        elif(step1[0] == 'ASIN'):
            #print(step1[1])
            currentItem.append(step1[1])
            pass
        elif(step1[0] == 'title'):
            #print(step1[1])
            # Some titles have colons in them
            # put them back together with a join
            title = (': '.join(step1[1: len(step1)]))
            currentItem.append(title)
            pass
        elif(step1[0] == 'group'):
            #print(step1[1])
            currentItem.append(step1[1])
            pass
        elif(step1[0] == 'salesrank'):
            #print(step1[1])
            currentItem.append(step1[1])
            pass
        elif(step1[0] == 'similar'):
            # We never have more than 5 similar product ASINs
            # step1[1] needs to be stripped of spaces and the leading number
            # which denotes how many similar items there are and
            # we can have similar1 - similar5 as items in our dataframe
            similarItems = step1[1].split(' ')
            for j in range (1, len(similarItems)):
                if(similarItems[j] != ''):
                    currentItem.append(similarItems[j])
            pass
        #elif(len(step2) > 2 and step2[2] == 'cutomer'):
        #    item = ''
        #    # idea; we have a 4 part system
        #    # Customer 1 - 5455 ID, ratingNum, numVotes, numHelpful
        #    # Separate values in string with commas
        #    # We can always query the string and then clean it off later
        #    for customerIndex in range (1, 4):
        #        stringToSplit = step1[customerIndex]
        #        stringSplit = stringToSplit.split(' ')
        #        if(stringSplit[2] == 'rating' and len(stringSplit) > 1):
        #            item = stringSplit[0]
        #        elif(stringSplit[2] == 'votes' and len(stringSplit) > 1):
        #            item = item + ',' + stringSplit[0]
        #        elif(stringSplit[2] == 'helpful' and len(stringSplit) > 1):
        #            item = item + ',' + stringSplit[0]
        #            item = item + ',' + step1[4]
        #    currentItem.append(item)
        #    pass
        elif(step1[0] == 'discontinued product'):
            #print("Product discontinued, no info available")
            currentItem.append(step1[0])
            pass
        i += 1
    # Close fine because muh good practice
    file.close()
    #print(f"This is the dataframe: {dataframe}")
    return dataframe


if __name__ == '__main__':
    dframe = parseData()
    df = pd.DataFrame(dframe, columns=['Index', 'ASIN', 'Title', 'Type', 'salesrank', 'similar1', 'similar2', 'similar3', 'similar4', 'similar5'])
    #print(df)
    filename = 'mmc175_CSDS234_finalproject.csv'
    df.to_csv(filename)