import pandas as pd
import csv

name = []
score = []
global all_score
all_score = []
global list_data
list_data = []
global df
def open_new_file(name):
    global df
    df = pd.DataFrame(pd.read_excel(name))
    df.fillna(value = 0)
    df.set_index('name')
    df.sort_index()
    get_name()

def get_name():
    global df
    for i in range(1,len(df.index)):
        name.append(df.loc[i][0])
        
def add_score():
    global df
    global all_score
    score = []
    for i in range(1,len(df.index)):
        score.append(df.loc[i][15])
    all_score.append(score)

def write_csv():
    file = open("2.csv","w",newline='')
    writer = csv.writer(file)
    list_data = process()
    writer.writerows(list_data)
    print(name)
    file.close()
def process():
    global list_data
    list_data.append(name)
    for i in range(len(all_score)):
        this_score  = []
        for i2 in range(len(all_score[i])):
            this_score.append(all_score[i][i2])
        list_data.append(this_score)
    return list_data
while True:
    sign = input("name:")
    if sign == "c":
        break
    else:
        open_new_file(sign)  
        add_score()
        write_csv()

