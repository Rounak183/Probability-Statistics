import csv
import math
import numpy
with open('tic-tac-toe.csv',mode='r') as file1,open('tic1.csv',mode='w') as datafile:
	csvread1=csv.DictReader(file1,delimiter=',')
	fieldnames=['(1,1)','(1,2)','(1,3)','(2,1)','(2,2)','(2,3)','(3,1)','(3,2)','(3,3)','result']
	writer=csv.DictWriter(datafile,fieldnames=fieldnames)
	writer.writeheader()
	csv1copy=[]
	for row2 in csvread1:
		csv1copy.append(row2)
	for row1 in csv1copy:
		writer.writerow({'(1,1)':row1['(1,1)'],'(1,2)':row1['(1,2)'],'(1,3)':row1['(1,3)'],'(2,1)':row1['(2,1)'],'(2,2)':row1['(2,2)'],'(2,3)':row1['(2,3)'],'(3,1)':row1['(3,1)'],'(3,2)':row1['(3,2)'],'(3,3)':row1['(3,3)'],'result':row1['result']})
	