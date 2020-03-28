import csv
with open ('shuttle-landing-control.csv',mode='r') as file1,open('shuttle.csv',mode='w') as datafile:
	csvread1=csv.DictReader(file1,delimiter=',')
	fieldnames=['Class','Stability','Error','Sign','Wind','Magnitude','Visibility']
	writer=csv.DictWriter(datafile,fieldnames=fieldnames)
	writer.writeheader()
	csv1copy=[]
	for row2 in csvread1:
		csv1copy.append(row2)
	for row1 in csv1copy:
		writer.writerow({'Class':row1['Class'],'Stability':row1['Stability'],'Error':row1['Error'],'Sign':row1['Sign'],'Wind':row1['Wind'],'Magnitude':row1['Magnitude'],'Visibility':row1['Visibility']})