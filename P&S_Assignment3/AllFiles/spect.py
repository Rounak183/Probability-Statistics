import csv
with open('tf.csv',mode='r') as file,open('SPECTtest.csv') as test:	
	tl=csv.DictReader(test,delimiter=',')
	data=csv.DictReader(file,delimiter=',')
	c=[]
	for rwoo in data:
		c.append(rwoo)
	t=[]
	for row in tl:
		t.append(row)
	cl=[]
	a1=[]
	a2=[]
	a3=[]
	a4=[]
	a5=[]
	a6=[]
	a7=[]
	a8=[]
	a9=[]
	a10=[]
	a11=[]
	a12=[]
	a13=[]
	a14=[]
	a15=[]
	a16=[]
	a17=[]
	a18=[]
	a19=[]
	a20=[]
	a21=[]
	a22=[]
	clt=[]
	a1t=[]
	a2t=[]
	a3t=[]
	a4t=[]
	a5t=[]
	a6t=[]
	a7t=[]
	a8t=[]
	a9t=[]
	a10t=[]
	a11t=[]
	a12t=[]
	a13t=[]
	a14t=[]
	a15t=[]
	a16t=[]
	a17t=[]
	a18t=[]
	a19t=[]
	a20t=[]
	a21t=[]
	a22t=[]
	for row in c:
		cl.append(row['Class'])
		a1.append(row['a1'])
		a2.append(row['a2'])
		a3.append(row['a3'])
		a4.append(row['a4'])
		a5.append(row['a5'])
		a6.append(row['a6'])
		a7.append(row['a7'])
		a8.append(row['a8'])
		a9.append(row['a9'])
		a10.append(row['a10'])
		a11.append(row['a11'])
		a12.append(row['a12'])
		a13.append(row['a13'])
		a14.append(row['a14'])
		a15.append(row['a15'])
		a16.append(row['a16'])
		a17.append(row['a17'])
		a18.append(row['a18'])
		a19.append(row['a19'])
		a20.append(row['a20'])
		a21.append(row['a21'])
		a22.append(row['a22'])
	for row in t:
		clt.append(row['Class'])
		a1t.append(row['a1'])
		a2t.append(row['a2'])
		a3t.append(row['a3'])
		a4t.append(row['a4'])
		a5t.append(row['a5'])
		a6t.append(row['a6'])
		a7t.append(row['a7'])
		a8t.append(row['a8'])
		a9t.append(row['a9'])
		a10t.append(row['a10'])
		a11t.append(row['a11'])
		a12t.append(row['a12'])
		a13t.append(row['a13'])
		a14t.append(row['a14'])
		a15t.append(row['a15'])
		a16t.append(row['a16'])
		a17t.append(row['a17'])
		a18t.append(row['a18'])
		a19t.append(row['a19'])
		a20t.append(row['a20'])
		a21t.append(row['a21'])
		a22t.append(row['a22'])
	a1y1=0
	a1y0=0
	a2y1=0
	a2y0=0
	a3y1=0
	a3y0=0
	a4y1=0
	a4y0=0
	a5y1=0
	a5y0=0
	a6y1=0
	a6y0=0
	a7y1=0
	a7y0=0
	a8y1=0
	a8y0=0
	a9y1=0
	a9y0=0
	a10y1=0
	a10y0=0
	a11y1=0
	a11y0=0
	a12y1=0
	a12y0=0
	a13y1=0
	a13y0=0
	a14y1=0
	a14y0=0
	a15y1=0
	a15y0=0
	a16y1=0
	a16y0=0
	a17y1=0
	a17y0=0
	a18y1=0
	a18y0=0
	a19y1=0
	a19y0=0
	a20y1=0
	a20y0=0
	a21y1=0
	a21y0=0
	a22y1=0
	a22y0=0
	a1n1=0
	a1n0=0
	a2n1=0
	a2n0=0
	a3n1=0
	a3n0=0
	a4n1=0
	a4n0=0
	a5n1=0
	a5n0=0
	a6n1=0
	a6n0=0
	a7n1=0
	a7n0=0
	a8n1=0
	a8n0=0
	a9n1=0
	a9n0=0
	a10n1=0
	a10n0=0
	a11n1=0
	a11n0=0
	a12n1=0
	a12n0=0
	a13n1=0
	a13n0=0
	a14n1=0
	a14n0=0
	a15n1=0
	a15n0=0
	a16n1=0
	a16n0=0
	a17n1=0
	a17n0=0
	a18n1=0
	a18n0=0
	a19n1=0
	a19n0=0
	a20n1=0
	a20n0=0
	a21n1=0
	a21n0=0
	a22n1=0
	a22n0=0
	cy=0
	cn=0
	for i in range(0,80):
		if (cl[i]=='1'):
			if (a1[i]=='1'):
				a1y1+=1
			else:
				a1y0+=1	
			if (a2[i]=='1'):
				a2y1+=1
			else:
				a2y0+=1
			if (a3[i]=='1'):
				a3y1+=1
			else:
				a3y0+=1
			if (a4[i]=='1'):
				a4y1+=1
			else:
				a4y0+=1
			if (a5[i]=='1'):
				a5y1+=1
			else:
				a5y0+=1
			if (a6[i]=='1'):
				a6y1+=1
			else:
				a6y0+=1
			if (a7[i]=='1'):
				a7y1+=1
			else:
				a7y0+=1
			if (a8[i]=='1'):
				a8y1+=1
			else:
				a8y0+=1
			if (a9[i]=='1'):
				a9y1+=1
			else:
				a9y0+=1
			if (a10[i]=='1'):
				a10y1+=1
			else:
				a10y0+=1
			if (a11[i]=='1'):
				a11y1+=1
			else:
				a11y0+=1
			if (a12[i]=='1'):
				a12y1+=1
			else:
				a12y0+=1
			if (a13[i]=='1'):
				a13y1+=1
			else:
				a13y0+=1
			if (a14[i]=='1'):
				a14y1+=1
			else:
				a14y0+=1
			if (a15[i]=='1'):
				a15y1+=1
			else:
				a15y0+=1
			if (a16[i]=='1'):
				a16y1+=1
			else:
				a16y0+=1
			if (a17[i]=='1'):
				a17y1+=1
			else:
				a17y0+=1
			if (a18[i]=='1'):
				a18y1+=1
			else:
				a18y0+=1
			if (a19[i]=='1'):
				a19y1+=1
			else:
				a19y0+=1
			if (a20[i]=='1'):
				a20y1+=1
			else:
				a20y0+=1
			if (a21[i]=='1'):
				a21y1+=1
			else:
				a21y0+=1
			if (a22[i]=='1'):
				a22y1+=1
			else:
				a22y0+=1	
			cy+=1											
		else:
			if (a1[i]=='1'):
				a1n1+=1
			else:
				a1n0+=1	
			if (a2[i]=='1'):
				a2n1+=1
			else:
				a2n0+=1
			if (a3[i]=='1'):
				a3n1+=1
			else:
				a3n0+=1
			if (a4[i]=='1'):
				a4n1+=1
			else:
				a4n0+=1
			if (a5[i]=='1'):
				a5n1+=1
			else:
				a5n0+=1
			if (a6[i]=='1'):
				a6n1+=1
			else:
				a6n0+=1
			if (a7[i]=='1'):
				a7n1+=1
			else:
				a7n0+=1
			if (a8[i]=='1'):
				a8n1+=1
			else:
				a8n0+=1
			if (a9[i]=='1'):
				a9n1+=1
			else:
				a9n0+=1
			if (a10[i]=='1'):
				a10n1+=1
			else:
				a10n0+=1
			if (a11[i]=='1'):
				a11n1+=1
			else:
				a11n0+=1
			if (a12[i]=='1'):
				a12n1+=1
			else:
				a12n0+=1
			if (a13[i]=='1'):
				a13n1+=1
			else:
				a13n0+=1
			if (a14[i]=='1'):
				a14n1+=1
			else:
				a14n0+=1
			if (a15[i]=='1'):
				a15n1+=1
			else:
				a15n0+=1
			if (a16[i]=='1'):
				a16n1+=1
			else:
				a16n0+=1
			if (a17[i]=='1'):
				a17n1+=1
			else:
				a17n0+=1
			if (a18[i]=='1'):
				a18n1+=1
			else:
				a18n0+=1
			if (a19[i]=='1'):
				a19n1+=1
			else:
				a19n0+=1
			if (a20[i]=='1'):
				a20n1+=1
			else:
				a20n0+=1
			if (a21[i]=='1'):
				a21n1+=1
			else:
				a21n0+=1
			if (a22[i]=='1'):
				a22n1+=1
			else:
				a22n0+=1
			cn+=1
	pa1y1y=a1y1/cy
	pa1y0y=a1y0/cy
	pa2y1y=a2y1/cy
	pa2y0y=a2y0/cy
	pa3y1y=a3y1/cy
	pa3y0y=a3y0/cy
	pa4y1y=a4y1/cy
	pa4y0y=a4y0/cy
	pa5y1y=a5y1/cy
	pa5y0y=a5y0/cy
	pa6y1y=a6y1/cy
	pa6y0y=a6y0/cy
	pa7y1y=a7y1/cy
	pa7y0y=a7y0/cy
	pa8y1y=a8y1/cy
	pa8y0y=a8y0/cy
	pa9y1y=a9y1/cy
	pa9y0y=a9y0/cy		
	pa10y1y=a10y1/cy
	pa10y0y=a10y0/cy
	pa11y1y=a11y1/cy
	pa11y0y=a11y0/cy
	pa12y1y=a12y1/cy
	pa12y0y=a12y0/cy
	pa13y1y=a13y1/cy
	pa13y0y=a13y0/cy
	pa14y1y=a14y1/cy
	pa14y0y=a14y0/cy
	pa15y1y=a15y1/cy
	pa15y0y=a15y0/cy
	pa16y1y=a16y1/cy
	pa16y0y=a16y0/cy
	pa17y1y=a17y1/cy
	pa17y0y=a17y0/cy
	pa18y1y=a18y1/cy
	pa18y0y=a18y0/cy
	pa19y1y=a19y1/cy
	pa19y0y=a19y0/cy
	pa20y1y=a20y1/cy
	pa20y0y=a20y0/cy
	pa21y1y=a21y1/cy
	pa21y0y=a21y0/cy
	pa22y1y=a22y1/cy
	pa22y0y=a22y0/cy
	pa1n1n=a1n1/cn
	pa1n0n=a1n0/cn
	pa2n1n=a2n1/cn
	pa2n0n=a2n0/cn
	pa3n1n=a3n1/cn
	pa3n0n=a3n0/cn
	pa4n1n=a4n1/cn
	pa4n0n=a4n0/cn
	pa5n1n=a5n1/cn
	pa5n0n=a5n0/cn
	pa6n1n=a6n1/cn
	pa6n0n=a6n0/cn
	pa7n1n=a7n1/cn
	pa7n0n=a7n0/cn
	pa8n1n=a8n1/cn
	pa8n0n=a8n0/cn
	pa9n1n=a9n1/cn
	pa9n0n=a9n0/cn		
	pa10n1n=a10n1/cn
	pa10n0n=a10n0/cn
	pa11n1n=a11n1/cn
	pa11n0n=a11n0/cn
	pa12n1n=a12n1/cn
	pa12n0n=a12n0/cn
	pa13n1n=a13n1/cn
	pa13n0n=a13n0/cn
	pa14n1n=a14n1/cn
	pa14n0n=a14n0/cn
	pa15n1n=a15n1/cn
	pa15n0n=a15n0/cn
	pa16n1n=a16n1/cn
	pa16n0n=a16n0/cn
	pa17n1n=a17n1/cn
	pa17n0n=a17n0/cn
	pa18n1n=a18n1/cn
	pa18n0n=a18n0/cn
	pa19n1n=a19n1/cn
	pa19n0n=a19n0/cn
	pa20n1n=a20n1/cn
	pa20n0n=a20n0/cn
	pa21n1n=a21n1/cn
	pa21n0n=a21n0/cn
	pa22n1n=a22n1/cn
	pa22n0n=a22n0/cn
	t1=0
	t2=0
	t3=0
	t4=0
	t5=0
	t6=0
	t7=0
	t8=0
	t9=0
	t10=0
	t11=0
	t12=0
	t13=0
	t14=0
	t15=0
	t16=0
	t17=0
	t18=0
	t19=0
	t20=0
	t21=0
	t22=0
	nt1=0
	nt2=0
	nt3=0
	nt4=0
	nt5=0
	nt6=0
	nt7=0
	nt8=0
	nt9=0
	nt10=0
	nt11=0
	nt12=0
	nt13=0
	nt14=0
	nt15=0
	nt16=0
	nt17=0
	nt18=0
	nt19=0
	nt20=0
	nt21=0
	nt22=0
	py=cy/80
	pn=cn/80
	acc=0
	for i in range(0,187):
		if (a1t[i]=='1'):
			t1=pa1y1y
			nt1=pa1n1n
		else:
			t1=pa1y0y
			nt1=pa1n0n
		if (a2t[i]=='1'):
			t2=pa2y1y
			nt2=pa2n1n
		else:
			t2=pa2y0y
			nt2=pa2n0n
		if (a3t[i]=='1'):
			t3=pa3y1y
			nt3=pa3n1n
		else:
			t3=pa3y0y
			nt3=pa3n0n
		if (a4t[i]=='1'):
			t4=pa4y1y
			nt4=pa4n1n
		else:
			t4=pa4y0y
			nt4=pa4n0n
		if (a5t[i]=='1'):
			t5=pa5y1y
			nt5=pa5n1n
		else:
			t5=pa5y0y
			nt5=pa5n0n
		if (a6t[i]=='1'):
			t6=pa6y1y
			nt6=pa6n1n
		else:
			t6=pa6y0y
			nt6=pa6n0n
		if (a7t[i]=='1'):
			t7=pa7y1y
			nt7=pa7n1n
		else:
			t7=pa7y0y
			nt7=pa7n0n
		if (a8t[i]=='1'):
			t8=pa8y1y
			nt8=pa8n1n
		else:
			t8=pa8y0y
			nt8=pa8n0n
		if (a9t[i]=='1'):
			t9=pa9y1y
			nt9=pa9n1n
		else:
			t9=pa9y0y
			nt9=pa9n0n
		if (a10t[i]=='1'):
			t10=pa10y1y
			nt10=pa10n1n
		else:
			t10=pa10y0y
			nt10=pa10n0n		
		if (a11t[i]=='1'):
			t11=pa11y1y
			nt11=pa11n1n
		else:
			t11=pa11y0y
			nt11=pa11n0n
		if (a12t[i]=='1'):
			t12=pa12y1y
			nt12=pa12n1n
		else:
			t12=pa12y0y
			nt12=pa12n0n
		if (a13t[i]=='1'):
			t13=pa13y1y
			nt13=pa13n1n
		else:
			t13=pa13y0y
			nt13=pa13n0n
		if (a14t[i]=='1'):
			t14=pa14y1y
			nt14=pa14n1n
		else:
			t14=pa14y0y
			nt14=pa14n0n
		if (a15t[i]=='1'):
			t15=pa15y1y
			nt15=pa15n1n
		else:
			t15=pa15y0y
			nt15=pa15n0n
		if (a16t[i]=='1'):
			t16=pa16y1y
			nt16=pa16n1n
		else:
			t16=pa16y0y
			nt16=pa16n0n
		if (a17t[i]=='1'):
			t17=pa17y1y
			nt17=pa17n1n
		else:
			t17=pa17y0y
			nt17=pa17n0n
		if (a18t[i]=='1'):
			t18=pa18y1y
			nt18=pa18n1n
		else:
			t18=pa18y0y
			nt18=pa18n0n
		if (a19t[i]=='1'):
			t19=pa19y1y
			nt19=pa19n1n
		else:
			t19=pa19y0y
			nt19=pa19n0n
		if (a20t[i]=='1'):
			t20=pa20y1y
			nt20=pa20n1n
		else:
			t20=pa20y0y
			nt20=pa20n0n
		if (a21t[i]=='1'):
			t21=pa21y1y
			nt21=pa21n1n
		else:
			t21=pa21y0y
			nt21=pa21n0n
		if (a22t[i]=='1'):
			t22=pa22y1y
			nt22=pa22n1n
		else:
			t22=pa22y0y
			nt22=pa22n0n
		prpy=py*t1*t2*t3*t4*t5*t6*t7*t8*t9*t10*t11*t12*t13*t14*t15*t16*t17*t18*t19*t20*t21*t22
		prpn=pn*nt1*nt2*nt3*nt4*nt5*nt6*nt7*nt8*nt9*nt10*nt11*nt12*nt13*nt14*nt15*nt16*nt17*nt18*nt19*nt20*nt21*nt22
		if (clt[i]=='1'):
			if (prpy>prpn):
				acc+=1
		else:
			if (prpn>prpy):
				acc+=1
	act=(acc/187)*100
	print(act)				