"""
Title: Attendance Distributor
Author: Siddhant Thakur
Date: 23-12-2020
"""

import random
import pandas as pd

attendance = []
marks = []
file_name = input("Enter file name with extension: ")
data = pd.read_excel(file_name)

attendance_percent = pd.DataFrame((data['TOTAL PRESENT'] / data['TOTAL LECTURE']) * 100)
attendance_percent.rename(columns={0: "PRESENT PERCENT"}, inplace=True)
total_absent = pd.DataFrame(data['TOTAL LECTURE'] - data['TOTAL PRESENT'])
total_absent.rename(columns={0: "ABSENT"}, inplace=True)

raw = pd.DataFrame([data['Roll Number'], data['Student\'s Name'], data['marks'], data['TOTAL PRESENT'],
                    total_absent['ABSENT'], data['TOTAL LECTURE'], attendance_percent['PRESENT PERCENT']]).transpose()
# print(raw.head())
# print("\n\n\n")

for perc in raw['PRESENT PERCENT']:
    if perc < 75:
        marks.append(5)
    elif 75 <= perc < 81:
        marks.append(6)
    elif 81 <= perc < 86:
        marks.append(7)
    elif 86 <= perc < 90:
        marks.append(8)
    elif 90 <= perc < 94:
        marks.append(9)
    elif 94 <= perc <= 100:
        marks.append(10)
# print(marks)
out_marks = pd.DataFrame(marks)
out_marks.rename(columns={0: "Expected Marks"}, inplace=True)
# print(out_marks.head())

for absent in raw['ABSENT']:
    student_attendance = ["P"] * data['TOTAL LECTURE'][0]
    student_attendance[:absent] = ["A"] * absent
    random.shuffle(student_attendance)
    attendance.append(student_attendance)

out = pd.DataFrame(attendance)

output = pd.concat([raw, out_marks, out], axis=1)

output.drop(['ABSENT', 'PRESENT PERCENT'], axis=1, inplace=True)
# print(output.head())
output.to_excel("output.xlsx")
