##This section opens a file dialog window so the user can choose the comma separated variable file 
from tkinter import filedialog
from tkinter import *
root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/",
                                           title = "Select file",
                                           filetypes=(("all files","*.*"),
                                                      ("comma separated variable files","*.csv"),

                                                       ("text files","*.txt")))
root.destroy() #destroy the window after we choose our file 

#initialize the totals of each column to be zero
totalOfColumnB = 0
totalOfColumnC = 0

import csv #need to import csv if we are going to use the csv functions available in python
with open(root.filename) as csv_file: #open the file we chose as a csv file 
    csv_reader = csv.reader(csv_file, delimiter=',') #create a csv.reader object from the csv file we chose,
                                                     #telling the system that each field will be separated (delimited) with commas
    line_count = 0
    for row in csv_reader:  #loop through each of the rows in our file
        if line_count == 0: #the first time we loop through we just print out the column headers 
            print(f'Column names are {row[0]}, {row[1]}, and {row[2]}')
            line_count = line_count + 1 #and then increase the line_count by 1
        else: #each subsequent time through the loop we do the following
            print(f'\t First Column = {row[0]} Second Column = {row[1]} Third Column = {row[2]}') #print out the row
            line_count = line_count + 1 #increase the line count by 1
            totalOfColumnB = totalOfColumnB + int(row[1]) #add columnB to the totalOfColumnB variable
            totalOfColumnC = totalOfColumnC + int(row[2]) #add columnC to the totalOfColumnC variable
            
    #the averages are just the total of the column divided by the number of rows minus one (we're not counting the header row)
    averageOfColumnB = totalOfColumnB/(line_count - 1) 
    averageOfColumnC = totalOfColumnC/(line_count - 1)

    #print out the results
    print(f'Processed {line_count} lines.')
    print(f'Average of ColumnB = {averageOfColumnB}')
    print(f'Average of ColumnC = {averageOfColumnC}')


