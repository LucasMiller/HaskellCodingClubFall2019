import os
import csv #need to import csv if we are going to use the csv functions available in python
from tkinter import filedialog
from tkinter import *

root = Tk()
root.withdraw()

folder_selected = filedialog.askdirectory()


path = folder_selected.replace('/', '\\') + '\\'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))

for f in files:
    print('File Name Is: ' + f)
    #columnA_List = list()
    #columnB_List = list()
    #columnC_List = list()

    with open(f) as csv_file: #open the file we chose as a csv file
        
        csv_reader = csv.reader(csv_file, delimiter=',') #create a csv.reader object from the csv file we chose,
                                                         #telling the system that each field will be separated (delimited) with commas
        line_count = 0
        for row in csv_reader:  #loop through each of the rows in our file
            if line_count == 0: #the first time we loop through we just print out the column headers
                print('Column names are', end = ' ')
                column_names = []
                for i in range(len(row)):
                    print(f'{row[i]}', end = ' ')
                    column_names.append(row[i])
                line_count = line_count + 1 #and then increase the line_count by 1
                data = [ [] for i in range(len(row))]
            else: #each subsequent time through the loop we do the following
                #print(f'\t First Column = {row[0]} Second Column = {row[1]} Third Column = {row[2]}') #print out the row
                line_count = line_count + 1 #increase the line count by 1
                for i in range(len(row)):
                    data[i].append(int(row[i]))
                
    average_list = list()
    for i in range(len(data)):
        average_list.append(sum(data[i])/len(data[i]))

    print(f'\nProcessed {line_count} lines.')

    for i in range(len(average_list)):
        print(f'Average of column {column_names[i]} = {average_list[i]}')

##    averageOfColumnA = sum(columnA_List)/len(columnA_List)
##    averageOfColumnB = sum(columnB_List)/len(columnB_List)
##    averageOfColumnC = sum(columnC_List)/len(columnC_List)
##
    #print out the results
##    print(f'\nProcessed {line_count} lines.')
##    print(f'Average of columnA = {averageOfColumnA}')
##    print(f'Average of ColumnB = {averageOfColumnB}')
##    print(f'Average of ColumnC = {averageOfColumnC}')
