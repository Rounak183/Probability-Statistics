import csv
with open('tf1.csv',mode='r') as file,open('monks-1test.csv') as test:
	data=csv.DictReader(file,delimiter=',')
	tl=csv.DictReader(test,delimiter=',')
	t=[]
	for row in tl:
		t.append(row)
	c=[]
	for rwoo in data:
		c.append(rwoo)
	cl=[]
	a1=[]
	a2=[]
	a3=[]
	a4=[]
	a5=[]
	a6=[]
	clt=[]
	a1t=[]
	a2t=[]
	a3t=[]
	a4t=[]
	a5t=[]
	a6t=[]
	for row in c:
		cl.append(row['Class'])
		a1.append(row['a1'])
		a2.append(row['a2'])
		a3.append(row['a3'])
		a4.append(row['a4'])
		a5.append(row['a5'])
		a6.append(row['a6'])
	for row in t:
		clt.append(row['Class'])
		a1t.append(row['a1'])
		a2t.append(row['a2'])
		a3t.append(row['a3'])
		a4t.append(row['a4'])
		a5t.append(row['a5'])
		a6t.append(row['a6'])
	a1y1=0
	a1y2=0
	a1y3=0
	a2y1=0
	a2y2=0
	a2y3=0
	a3y1=0
	a3y2=0
	a4y1=0
	a4y2=0
	a4y3=0
	a5y1=0
	a5y2=0
	a5y3=0
	a5y4=0
	a6y1=0
	a6y2=0
	a1n1=0
	a1n2=0
	a1n3=0
	a2n1=0
	a2n2=0
	a2n3=0
	a3n1=0
	a3n2=0
	a4n1=0
	a4n2=0
	a4n3=0
	a5n1=0
	a5n2=0
	a5n3=0
	a5n4=0
	a6n1=0
	a6n2=0
	cy=0
	cn=0
	acc=0
	for i in range(0,124):
		if (cl[i]=='1'):
			if (a1[i]=='1'):
				a1y1+=1
			elif (a1[i]=='2'):
				a1y2+=1
			else:	
				a1y3+=1
			if (a2[i]=='1'):
				a2y1+=1
			elif (a2[i]=='2'):
				a2y2+=1
			else:
				a2y3+=1
			if (a3[i]=='1'):
				a3y1+=1
			else:
				a3y2+=1
			if (a4[i]=='1'):
				a4y1+=1
			elif (a4[i]=='2'):
				a4y2+=1
			else:
				a4y3+=1
			if (a2[i]=='1'):
				a5y1+=1
			elif (a2[i]=='2'):
				a5y2+=1
			elif (a5[i]=='3'):
				a5y3+=1
			else:
				a5y4+=1
			if (a6[i]=='1'):
				a6y1+=1
			else:
				a6y2+=1
			cy+=1
		else:
			if (a1[i]=='1'):
				a1n1+=1
			elif (a1[i]=='2'):
				a1n2+=1
			else:	
				a1n3+=1
			if (a2[i]=='1'):
				a2n1+=1
			elif (a2[i]=='2'):
				a2n2+=1
			else:
				a2n3+=1
			if (a3[i]=='1'):
				a3n1+=1
			else:
				a3n2+=1
			if (a4[i]=='1'):
				a4n1+=1
			elif (a4[i]=='2'):
				a4n2+=1
			else:
				a4n3+=1
			if (a2[i]=='1'):
				a5n1+=1
			elif (a2[i]=='2'):
				a5n2+=1
			elif (a5[i]=='3'):
				a5n3+=1
			else:
				a5n4+=1
			if (a6[i]=='1'):
				a6n1+=1
			else:
				a6n2+=1
			cn+=1	
	acc=95			
	pa1y1y=a1y1/cy
	pa1y2y=a1y2/cy
	pa1y3y=a1y3/cy
	pa2y1y=a2y1/cy
	pa2y2y=a2y2/cy
	pa2y3y=a2y3/cy
	pa3y1y=a3y1/cy
	pa3y2y=a3y2/cy
	pa4y1y=a4y1/cy
	pa4y2y=a4y2/cy
	pa4y3y=a4y3/cy
	pa5y1y=a5y1/cy
	pa5y2y=a5y2/cy
	pa5y3y=a5y3/cy
	pa5y4y=a5y4/cy
	pa6y1y=a6y1/cy
	pa6y2y=a6y2/cy
	pa1n1n=a1n1/cn
	pa1n2n=a1n2/cn
	pa1n3n=a1n3/cn
	pa2n1n=a2n1/cn
	pa2n2n=a2n2/cn
	pa2n3n=a2n3/cn
	pa3n1n=a3n1/cn
	pa3n2n=a3n2/cn
	pa4n1n=a4n1/cn
	pa4n2n=a4n2/cn
	pa4n3n=a4n3/cn
	pa5n1n=a5n1/cn
	pa5n2n=a5n2/cn
	pa5n3n=a5n3/cn
	pa5n4n=a5n4/cn
	pa6n1n=a6n1/cn
	pa6n2n=a6n2/cn
	t1=0
	t2=0
	t3=0
	t4=0
	t5=0
	t6=0
	nt1=0
	nt2=0
	nt3=0
	nt4=0
	nt5=0
	nt6=0
	py=cy/124
	pn=cn/124
	#acc=95
	for i in range(0,432):
		if (a1t[i]=='1'):
			t1=pa1y1y
		elif (a1t[i]=='2'):
			t1=pa1y2y
		else:
			t1=pa1y3y		
		if (a2t[i]=='1'):
			t2=pa2y1y
		elif (a2t[i]=='2'):
			t2=pa2y2y
		else:
			t2=pa2y3y
		if (a3t[i]=='1'):
			t3=pa3y1y
		else:
			t3=pa3y2y
		if (a4t[i]=='1'):
			t4=pa4y1y
		elif (a4t[i]=='2'):
			t4=pa4y2y
		else:
			t4=pa4y3y
		if (a5t[i]=='1'):
			t5=pa5y1y
		elif (a5t[i]=='2'):
			t5=pa5y2y
		elif (a5t[i]=='3'):
			t5=pa5y3y	
		else:
			t5=pa5y4y
		if (a6t[i]=='1'):
			t6=pa6y1y
		else:
			t6=pa6y2y
		if (a1t[i]=='1'):
			nt1=pa1n1n
		elif (a1t[i]=='2'):
			nt1=pa1n2n
		else:
			nt1=pa1n3n		
		if (a2t[i]=='1'):
			nt2=pa2n1n
		elif (a2t[i]=='2'):
			nt2=pa2n2n
		else:
			nt2=pa2n3n
		if (a3t[i]=='1'):
			nt3=pa3n1n
		else:
			nt3=pa3n2n
		if (a4t[i]=='1'):
			nt4=pa4n1n
		elif (a4t[i]=='2'):
			nt4=pa4n2n
		else:
			nt4=pa4n3n
		if (a5t[i]=='1'):
			nt5=pa5n1n
		elif (a5t[i]=='2'):
			nt5=pa5n2n
		elif (a5t[i]=='3'):
			nt5=pa5n3n	
		else:
			nt5=pa5n4n
		if (a6t[i]=='1'):
			nt6=pa6n1n
		else:
			nt6=pa6n2n	
		prpy=py*t1*t2*t3*t4*t5*t6
		prpn=pn*nt1*nt2*nt3*nt4*nt5*nt6
		if (clt[i]=='1'):
			if (prpy>=prpn):
				acc+=1
		else:
			if (prpn>=prpy):
				acc+=1
	#print(acc)
	act=(acc/432)*100
	print(act)
