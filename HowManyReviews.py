#!/usr/bin/env python3

# rudimentary script to find the largest number of customers
# that have left reviews for a product

def findMaxReviewers():
    file = open('amazon-meta.txt', "r", encoding="utf8")
    total = 0

    for i in range(1, 15010574):

        readLine = file.readline().splitlines()
        # print(f" readline: {readLine}")
        precursor = readLine[0].replace(' ', ':')
        step0 = precursor.split(':')
        step1 = [item.strip() for item in step0]
        step2 = [thing for thing in step1 if thing]
        #print(step2)

        try:
            if (step2[0] == 'reviews'):
                #print(step2)
                if (int(step2[2]) > total):
                    print(step2[2])
                    total = int(step2[2])
        except IndexError as IE:
            pass
        except TypeError as TE:
            pass

    file.close()
    return(total)

if __name__ == '__main__':
    print(findMaxReviewers())
    # The largest number of customers is 5545 from the code