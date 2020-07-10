"""
Problem statement : Given a number in range 0-30 (both inclusive), split the given number into random parts as required by the user (2 or 3).

Assume that the excel file for input has only one column named as 'data' which contains a list of such numbers to be split into random parts
"""


import random
import pandas as pd


def splitter2(t):
    """
    :param t: number to be split in n (here 2) unequal parts
    :return: list of random numbers having sum = t
    """
    res = list()
    res.append(random.randint(0, t))
    res.append(t-res[0])
    return res


def splitter3(t):
    """
    :param t: number to be split in n (here 3) unequal parts
    :return: list of random numbers having sum = t
    """
    res = list()
    res.append(random.randint(0, t))
    res.append(random.randint(0, t-res[0]))
    res.append(t-(res[0]+res[1]))
    return res


def main():
    out = list()
    n = eval(input('Enter number of random numbers required in output (2 or 3): '))
    file_name = input('Enter file name with extension: ')
    sheet = input('Enter the Sheet name: ')
    data = pd.read_excel(file_name, sheet_name=sheet)

    if n == 2:
        for x in data['data']:
            out.append(splitter2(x))
        df = pd.DataFrame(out)
        df.to_excel('output_split2.xlsx')

    if n == 3:
        for x in data['data']:
            out.append(splitter3(x))
        df = pd.DataFrame(out)
        df.to_excel('output_split3.xlsx')


main()
