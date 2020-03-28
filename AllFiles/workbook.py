import csv
nl=['TicTac','Spect','Monks1','Monks2','Monks3','Shuttle','SoyaBean']
acc=['69.41544885177453','77.54010695187165','71.29629629629629','62.96296296296296','97.22222222222221','93.33333333333333','87.2340425531915']
with open('workbook.csv',mode='w') as datafile:
	fieldnames=['DataSets','Accuracy']
	writer=csv.DictWriter(datafile,fieldnames=fieldnames)
	for i in range(0,6):
		writer.writerow({'DataSets':nl[i],'Accuracy':acc[i]})
