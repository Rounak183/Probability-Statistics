import csv
with open('monks-2.csv',mode='r') as file1,open('tf2.csv',mode='w') as datafile:
	csvread1=csv.DictReader(file1,delimiter=',')
	fieldnames=['Class','a1','a2','a3','a4','a5','a6']
	writer=csv.DictWriter(datafile,fieldnames=fieldnames)
	writer.writeheader()
	csv1copy=[]
	for row2 in csvread1:
		csv1copy.append(row2)
	for row1 in csv1copy:
		writer.writerow({'Class':row1['Class'],'a1':row1['a1'],'a2':row1['a2'],'a3':row1['a3'],'a4':row1['a4'],'a5':row1['a5'],'a6':row1['a6']})