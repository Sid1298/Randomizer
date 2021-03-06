"""
Problem Statement : Given a number in range 12-100 (both inclusive), split data having values up to 100 (here, 5th value is a minimum of 12)

Assume that the excel file for input has only one column named as 'data' which contains a list of such numbers to be split into random parts
"""


import random
import pandas as pd


def split_100(t):
    l = random.sample(range(0, 15), 5)
    s = sum(l)
    res = list()
    if t <= 12:
        res = [0, 0, 0, 0, t]
        return res
    else:
        for x in range(0, 5):
            res.append(round((l[x] / s) * t))
        maxindex = res.index(max(res))
        minindex = res.index(min(res))
        tot = sum(res)
        if tot > 100:
            res[maxindex] -= 1
        for i in range(0, t // 2):
            for num in range(len(res)):
                if res[num] > 20:
                    minindex = res.index(min(res))
                    surplus = res[num] - 20
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


def shuf_100(lst):
    while max(lst) < 12:
        lst = split_100(sum(lst))
    while lst[-1] < 12:
        random.shuffle(lst)
    return lst


def main():
    file_name = input('Enter file name with extension: ')
    sheet = input('Enter sheet name: ')
    # n = eval(input('Enter type of data (25/50/100): '))
    out = list()
    data = pd.read_excel(file_name, sheet_name=sheet)
    for x in data['data']:
        out.append(shuf_100(split_100(x)))

    df = pd.DataFrame(out)
    df.to_excel('split_.xlsx')


main()
