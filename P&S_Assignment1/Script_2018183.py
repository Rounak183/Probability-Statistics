import csv;
import math;
with open('f.csv',mode='r') as file1,open('processed_iFactor.csv',mode='r') as file2,open('theone.csv',mode='w') as datafile:
	csvread1=csv.DictReader(file1,delimiter=';');
	csvread2=csv.DictReader(file2,delimiter=',');
	fieldnames=['Title','H index','impact factor']
	writer=csv.DictWriter(datafile,fieldnames=fieldnames);
	writer.writeheader();
	csv2copy=[];
	count=0;
	for row2 in csvread2:
		csv2copy.append(row2);
	for row1 in csvread1:
		for row3 in csv2copy:
			if ({row3["Titles"].lower()}=={row1["Title"].lower()}):
				count=count+1;
				writer.writerow({'Title':row1["Title"],'H index':row1["H index"],'impact factor':row3["IF"]});
with open('theone.csv',mode='r') as ans:
	data=csv.DictReader(ans,delimiter=',')
	sx=0;
	SX=0
	sy=0;
	SY=0;
	sxy=0;
	SXY=0;
	sx2=0;
	SX2=0;
	sy2=0;
	SY2=0;
	x=0;
	y=0;
	xy=0;
	x2=0;
	y2=0;
	ct=math.ceil(count*0.8);
	i=0;
	c=[];
	for rwoo in data:
		c.append(rwoo);
	for row in c:
		sx=sx+float(row['H index']);
		sy=sy+float(row['impact factor']);
		sxy=sxy+float(row['H index'])*float(row['impact factor']);
		sx2=sx2+float(row['H index'])*float(row['H index']);
		sy2=sy2+float(row['impact factor'])*float(row['impact factor']);
		if (i<206):
			SX=SX+float(row['H index']);
			SY=SY+float(row['impact factor']);
			SXY=SXY+float(row['H index'])*float(row['impact factor']);
			SX2=SX2+float(row['H index'])*float(row['H index']);
			SY2=SY2+float(row['impact factor'])*float(row['impact factor']);
	num=count*sxy-sx*sy;
	d1=math.sqrt(count*sx2-sx*sx);
	d2=math.sqrt(count*sy2-sy*sy);
	den=d1*d2;
	cc=num/den;
	mx=SX/ct;
	my=SY/ct;
	VARX=SX2/ct-(SX/ct)*(SX/ct);
	STX=math.sqrt(VARX);
	VARY=SY2/ct-(SY/ct)*(SY/ct);
	STY=math.sqrt(VARY);
	a=cc*(STY/STX);
	b=my-a*mx;
	i=0;
	sumy=0;
	caly=0;
	for roww in c:
		if (i>=206):
			x=float(roww['H index']);
			y=float(roww['impact factor']);
			caly=a*x+b;
			sumy=sumy+(caly-y)*(caly-y);
		else:
			i=i+1;
	meansqe=sumy/(count-ct);
	print('Mean squared error = ',meansqe);
	print('Regression line is','y = ',a,'x +',b);		


