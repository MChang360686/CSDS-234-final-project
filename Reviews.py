#!/usr/bin/python3

import pandas as pd

# purpose is to take into account the fact that some products have 5545 reviews,
# while others have very few, and some have none at all

file = open('amazon-meta.txt', "r", encoding="utf8")

def stripReviews():
    dataframeThree = []
    review = []
    index = 0
    iteration = 1

    for i in range(0, 15010574):
        readLine = file.readline().splitlines()
        # Can't use lstrip or rstrip on lists (readline), must use on string
        step0 = readLine[0].lstrip(' ')
        step1 = step0.split(' ')
        # Use list comprehension to fix inconsistent spacing
        # Alternatively, use a filter
        step2 = list(filter(None, step1)) #[i for i in step1 if i]

        if(len(step2) >= 1 and step2[0] == 'Id:'):
            index = step2[1]
            pass
        # The end of the following elif statement may contain an extra
        # and int(index) > previous index + 1
        # This is to ensure you skip all of the lines you already added
        # to other csv files
        elif(len(step2) > 2 and step2[1] == 'cutomer:'):
            # Instead of appending a list by appending all the values
            # I find it is more efficient to append a list of all the desired values directly
            # to the dataframe
            dataframeThree.append(list((iteration, step2[2], step2[4], step2[6], step2[8], index)))
            iteration += 1
            pass
    file.close()
    return dataframeThree

if __name__ == '__main__':
    # Create dataframe
    reviews = stripReviews()
    df = pd.DataFrame(reviews, columns=['index', 'customerid', 'rating', 'votes', 'helpful', 'fk'])
    #print(df)
    # Convert dataframe into csv file
    filename = 'review.csv'
    df.to_csv(filename)

    # File ending lines and indexes
    # reviews1.csv line = 1940048 index = 70625
    # reviews2.csv line = 3880102 index = 141670
    # reviews3.csv line = 5820137 index = 214005
    # reviews4.csv line = 7760188 index = 285280
    # reviews5.csv line = 9700251 index = 363053
    # reviews6.csv line = 11640299 index = 436171
    # reviews7.csv line = 13580366 index = 512133

    #and int(index) >= 512134