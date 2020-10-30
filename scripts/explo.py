import csv
import pandas
# with open('summer-olympics.csv', newline='') as file:
#     reader = csv.reader(file, delimiter=',')
#     for row in reader:
#         print(', '.join(row))

df = pandas.read_csv('summer-olympics.csv')
print(df)