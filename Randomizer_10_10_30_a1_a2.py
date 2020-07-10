"""
Problem statement : Given a number in range (0-50), split the given number into random parts such that the output file has numbers x,y,z,a1,a2
where x : 6<=x<=10
      y : 5<=y<=10
      z : z<=30
      a1: a1<=30
      a2: a2<=30 
      also, z is average of a1 and a2.

Assume that the excel file for input has only one column named as 'data' which contains a list of such numbers to be split into random parts
"""


import random
import pandas as pd


def break_50(n):
    list1 = list()
    list1.append(random.randint(6, 10))  # x
    list1.append(random.randint(5, 10))  # y
    list1.append(n - (list1[0] + list1[1]))  # z

    if list1[2] > 30:
        surplus = list1[2] - 30
        minindex = list1.index(min(list1))
        list1[minindex] += surplus
        list1[2] -= surplus

    if list1[0] > 10:
        surplus = list1[0] - 10
        list1[1] += surplus
        list1[0] -= surplus

    if list1[1] > 10:
        surplus = list1[1] - 10
        list1[0] += surplus
        list1[1] -= surplus

    return list1


def break_avg(t):
    n = t * 2
    list2 = list()
    list2.append(random.randint(t - 5, t + 5))
    list2.append(n - list2[0])
    if list2[0] > 30:
        s = list2[0] - 30
        list2[0] -= s
        list2[1] += s
    if list2[1] > 30:
        s = list2[1] - 30
        list2[1] -= s
        list2[0] += s
    return list2    # list of a1 & a2


def combine(x):
    result = list()
    out_50 = break_50(x)
    out_avg = break_avg(out_50[2])
    result.extend(out_50)
    result.extend(out_avg)
    return result


def main():
    print('The output generated in the excel file contains the following columns respectively: x, '
          'y, z, a1 and a2')
    out = list()
    file = input('Enter file name with extension: ')
    sheet = input('Enter sheet name: ')
    data = pd.read_excel(file, sheet_name=sheet)
    for x in data['data']:
        out.append(combine(x))
    df = pd.DataFrame(out)
    df.to_excel('attend_assign_mark.xlsx')


main()
