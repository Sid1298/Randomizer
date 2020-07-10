"""
Problem statement : Given a number in range 0-30 (both inclusive), split the given number into 2 random parts such that no part is greater than 15.
Example: split the number 26 into two random numbers (x,y) such that 0<=x<=15, 0<=y<=15 x+y = 26

Assume that the excel file for input has only one column named as 'data' which contains a list of such numbers to be split into random parts
"""

# Code :


import random
import pandas as pd


def splitter(t):
    """
    function to perform the operation to split the given number t as required
    input: number (t) to be split in n parts
    output: list of n random numbers having sum = t
    """
    l = random.sample(range(0, 30), 2)
    s = sum(l)
    res = list()

    for x in range(0, 2):
        res.append(round((l[x] / s) * t))

    maxindex = res.index(max(res))
    minindex = res.index(min(res))
    tot = sum(res)
    if tot > 30:
        res[maxindex] = res[maxindex] - 1

    for i in range(0, t // 2):
        for num in range(len(res)):
            if res[num] > 15:
                minindex = res.index(min(res))
                surplus = res[num] - 15
                res[num] = res[num] - surplus
                res[minindex] = res[minindex] + surplus

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
    data = pd.read_excel(file_name, sheet_name=sheet)
    for x in data['data']:
        out.append(splitter(x))
    df = pd.DataFrame(out)
    df.to_excel('output.xlsx')


main()
