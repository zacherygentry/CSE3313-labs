# Zachery Gentry

import csv


f = open('data-communications.csv', 'rt')

reader = csv.reader(f)

for row in reader:
    for col in row:
        print(col)


