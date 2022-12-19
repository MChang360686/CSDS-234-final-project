#!/usr/bin/env python3

def findMaxCategories():
    file = open('amazon-meta.txt', "r", encoding="utf8")
    max = 0
#15010574
    for i in range(20, 15010574):
        readLine = file.readline().splitlines()
        step0 = readLine[0].split('|')
        #step1 = step0.pop(0)
        #print(f"step0: {step0}")
        #print(f"step1: {step1}")

        length = len(step0)
        if(length > max and len(step0) > 1):
            max = length
            print(max)

    file.close()
    return(max)

if __name__ == '__main__':
    findMaxCategories()
    #This implies that the max categories is 12