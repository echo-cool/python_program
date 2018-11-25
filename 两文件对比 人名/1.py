import csv
import os
def main():
    a = []
    b = []
    file1 = csv.reader(open("md.csv"))
    file2 = csv.reader(open("now.csv"))
    file1 = list(file1)
    file2 = list(file2)
    for i in file1:
        a.append(i[0])
    for i in file2:
        b.append(i[0])
    for i in a:
        if i not in b :
            print(i)




main()