import csv
with open('SPECT.csv',mode='r') as file1,open('tf.csv',mode='w') as datafile:
	csvread1=csv.DictReader(file1,delimiter=',')
	fieldnames=['Class','a1','a2','a3','a4','a5','a6','a7','a8','a9','a10','a11','a12','a13','a14','a15','a16','a17','a18','a19','a20','a21','a22']
	writer=csv.DictWriter(datafile,fieldnames=fieldnames)
	writer.writeheader()
	csv1copy=[]
	for row2 in csvread1:
		csv1copy.append(row2)
	for row1 in csv1copy:
		writer.writerow({'Class':row1['Class'],'a1':row1['a1'],'a2':row1['a2'],'a3':row1['a3'],'a4':row1['a4'],'a5':row1['a5'],'a6':row1['a6'],'a7':row1['a7'],'a8':row1['a8'],'a9':row1['a9'],'a10':row1['a10'],'a11':row1['a11'],'a12':row1['a12'],'a13':row1['a13'],'a14':row1['a14'],'a15':row1['a15'],'a16':row1['a16'],'a17':row1['a17'],'a18':row1['a18'],'a19':row1['a19'],'a20':row1['a20'],'a21':row1['a21'],'a22':row1['a22']})	
