"""
Problem statement : Given a number in range 0-30 (both inclusive), split the given number into 3 random parts such that no part is greater than 10.
Example: split the number 26 into three random numbers (x,y,z) such that 0<=x<=10, 0<=y<=10 and 0<=z<=10 and x+y+z = 26

Assume that the excel file for input has only one column named as 'data' which contains a list of such numbers to be split into random parts
"""


# Code: 


import random
import pandas as pd


def splitter(t):
    """
    function to perform the operation to split the given number t as required
    input: number (t) to be split in n parts
    output: list of n random numbers having sum = t
    """
    l = random.sample(range(0, 30), 3)
    s = sum(l)
    res = list()

    for x in range(0, 3):
        res.append(round((l[x] / s) * t))

    maxindex = res.index(max(res))    # index of maximum value among random numbers
    minindex = res.index(min(res))    # index of minimum value among random numbers
    tot = sum(res)    # total of all numbers
    if tot > 30:
        res[maxindex] = res[maxindex] - 1    # adjustments for surplus because of rounding off of numbers

    # loop for adjustment of surplus in list of numbers for output to satisfy constraints of the problem statement
    for i in range(0, t // 2):
        for num in range(len(res)):
            if res[num] > 10:
                minindex = res.index(min(res))
                surplus = res[num] - 10
                res[num] = res[num] - surplus
                res[minindex] = res[minindex] + surplus

    # final adjustments in output list
    if sum(res) < t:
        res[minindex] += 1
        return res

    elif sum(res) > t:
        res[maxindex] -= 1
        return res

    else:
        return res


def main():
    sheet = input('Enter the Sheet name: ')
    file_name = input('Enter file name with extension: ')
    out = list()
    data = pd.read_excel(file_name, sheet_name=sheet)    # reading the excel file data using pandas and loading into dataframe
    # applying the splitter() function on each data input from the file and appending to a list
    for x in data['data']:
        out.append(splitter(x))
    df = pd.DataFrame(out)    # converting the list into dataframe object to write to an excel file
    df.to_excel('random_10_10_10.xlsx')    # writing final output into an excel file


main()
