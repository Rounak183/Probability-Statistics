import csv
with open('tic1.csv',mode='r') as file:
	data=csv.DictReader(file,delimiter=',')
	c=[]
	for rwoo in data:
		c.append(rwoo)
	p1=[]
	p2=[]
	p3=[]
	p4=[]
	p5=[]
	p6=[]
	p7=[]
	p8=[]
	p9=[]
	res=[]
	for row in c:
		p1.append(row['(1,1)'])
		p2.append(row['(1,2)'])
		p3.append(row['(1,3)'])
		p4.append(row['(2,1)'])
		p5.append(row['(2,2)'])
		p6.append(row['(2,3)'])
		p7.append(row['(3,1)'])
		p8.append(row['(3,2)'])
		p9.append(row['(3,3)'])
		res.append(row['result'])
	x1=[]
	x2=[]
	x3=[]
	x4=[]
	x5=[]
	x6=[]
	x7=[]
	x8=[]
	x9=[]
	o1=[]
	o2=[]
	o3=[]
	o4=[]
	o5=[]
	o6=[]
	o7=[]
	o8=[]
	o9=[]
	b1=[]
	b2=[]
	b3=[]
	b4=[]
	b5=[]
	b6=[]
	b7=[]
	b8=[]
	b9=[]
	pc=[]
	nx1=[]
	nx2=[]
	nx3=[]
	nx4=[]
	nx5=[]
	nx6=[]
	nx7=[]
	nx8=[]
	nx9=[]
	no1=[]
	no2=[]
	no3=[]
	no4=[]
	no5=[]
	no6=[]
	no7=[]
	no8=[]
	no9=[]
	nb1=[]
	nb2=[]
	nb3=[]
	nb4=[]
	nb5=[]
	nb6=[]
	nb7=[]
	nb8=[]
	nb9=[]
	nc=[]
	acc=0
	for i in range(0,958):
		x1.append(0)
		x2.append(0)
		x3.append(0)
		x4.append(0)
		x5.append(0)
		x6.append(0)
		x7.append(0)
		x8.append(0)
		x9.append(0)
		o1.append(0)
		o2.append(0)
		o3.append(0)
		o4.append(0)
		o5.append(0)
		o6.append(0)
		o7.append(0)
		o8.append(0)
		o9.append(0)
		b1.append(0)
		b2.append(0)
		b3.append(0)
		b4.append(0)
		b5.append(0)
		b6.append(0)
		b7.append(0)
		b8.append(0)
		b9.append(0)
		pc.append(0)
		nx1.append(0)
		nx2.append(0)
		nx3.append(0)
		nx4.append(0)
		nx5.append(0)
		nx6.append(0)
		nx7.append(0)
		nx8.append(0)
		nx9.append(0)
		no1.append(0)
		no2.append(0)
		no3.append(0)
		no4.append(0)
		no5.append(0)
		no6.append(0)
		no7.append(0)
		no8.append(0)
		no9.append(0)
		nb1.append(0)
		nb2.append(0)
		nb3.append(0)
		nb4.append(0)
		nb5.append(0)
		nb6.append(0)
		nb7.append(0)
		nb8.append(0)
		nb9.append(0)
		nc.append(0)
	for j in range(0,958):
		for i in range(0,958):
			if (i!=j):
				if (res[i]=='positive'):
					if (p1[i]=='x'):
						x1[j]=x1[j]+1
					elif (p1[i]=='o'):
						o1[j]+=1
					else:
						b1[j]+=1
					if (p2[i]=='x'):
						x2[j]+=1
					elif (p2[i]=='o'):
						o2[j]+=1
					else:
						b2[j]+=1
					if (p3[i]=='x'):
						x3[j]+=1
					elif (p3[i]=='o'):
						o3[j]+=1
					else:
						b3[j]+=1
					if (p4[i]=='x'):
						x4[j]+=1
					elif (p4[i]=='o'):
						o4[j]+=1
					else:
						b4[j]+=1
					if (p5[i]=='x'):
						x5[j]+=1
					elif (p5[i]=='o'):
						o5[j]+=1
					else:
						b5[j]+=1
					if (p6[i]=='x'):
						x6[j]+=1
					elif (p6[i]=='o'):
						o6[j]+=1
					else:
						b6[j]+=1
					if (p7[i]=='x'):
						x7[j]+=1
					elif (p7[i]=='o'):
						o7[j]+=1
					else:
						b7[j]+=1
					if (p8[i]=='x'):
						x8[j]+=1
					elif (p8[i]=='o'):
						o8[j]+=1
					else:
						b8[j]+=1
					if (p9[i]=='x'):
						x9[j]+=1
					elif (p9[i]=='o'):
						o9[j]+=1
					else:
						b9[j]+=1
					pc[j]+=1
				else:
					if (p1[i]=='x'):
						nx1[j]+=1
					elif (p1[i]=='o'):
						no1[j]+=1
					else:
						nb1[j]+=1
					if (p2[i]=='x'):
						nx2[j]+=1
					elif (p2[i]=='o'):
						no2[j]+=1
					else:
						nb2[j]+=1
					if (p3[i]=='x'):
						nx3[j]+=1
					elif (p3[i]=='o'):
						no3[j]+=1
					else:
						nb3[j]+=1
					if (p4[i]=='x'):
						nx4[j]+=1
					elif (p4[i]=='o'):
						no4[j]+=1
					else:
						nb4[j]+=1
					if (p5[i]=='x'):
						nx5[j]+=1
					elif (p5[i]=='o'):
						no5[j]+=1
					else:
						nb5[j]+=1
					if (p6[i]=='x'):
						nx6[j]+=1
					elif (p6[i]=='o'):
						no6[j]+=1
					else:
						nb6[j]+=1
					if (p7[i]=='x'):
						nx7[j]+=1
					elif (p7[i]=='o'):
						no7[j]+=1
					else:
						nb7[j]+=1
					if (p8[i]=='x'):
						nx8[j]+=1
					elif (p8[i]=='o'):
						no8[j]+=1
					else:
						nb8[j]+=1
					if (p9[i]=='x'):
						nx9[j]+=1
					elif (p9[i]=='o'):
						no9[j]+=1
					else:
						nb9[j]+=1
					nc[j]+=1
		x1p=x1[j]/pc[j]	
		x2p=x2[j]/pc[j]
		x3p=x3[j]/pc[j]
		x4p=x4[j]/pc[j]
		x5p=x5[j]/pc[j]
		x6p=x6[j]/pc[j]
		x7p=x7[j]/pc[j]
		x8p=x8[j]/pc[j]
		x9p=x9[j]/pc[j]
		o1p=o1[j]/pc[j]
		o2p=o2[j]/pc[j]
		o3p=o3[j]/pc[j]
		o4p=o4[j]/pc[j]
		o5p=o5[j]/pc[j]
		o6p=o6[j]/pc[j]
		o7p=o7[j]/pc[j]
		o8p=o8[j]/pc[j]
		o9p=o9[j]/pc[j]
		b1p=b1[j]/pc[j]
		b2p=b2[j]/pc[j]
		b3p=b3[j]/pc[j]
		b4p=b4[j]/pc[j]
		b5p=b5[j]/pc[j]
		b6p=b6[j]/pc[j]
		b7p=b7[j]/pc[j]
		b8p=b8[j]/pc[j]
		b9p=b9[j]/pc[j]
		pry=pc[j]/957
		nx1p=nx1[j]/nc[j]	
		nx2p=nx2[j]/nc[j]
		nx3p=nx3[j]/nc[j]
		nx4p=nx4[j]/nc[j]
		nx5p=nx5[j]/nc[j]
		nx6p=nx6[j]/nc[j]
		nx7p=nx7[j]/nc[j]
		nx8p=nx8[j]/nc[j]
		nx9p=nx9[j]/nc[j]
		no1p=no1[j]/nc[j]
		no2p=no2[j]/nc[j]
		no3p=no3[j]/nc[j]
		no4p=no4[j]/nc[j]
		no5p=no5[j]/nc[j]
		no6p=no6[j]/nc[j]
		no7p=no7[j]/nc[j]
		no8p=no8[j]/nc[j]
		no9p=no9[j]/nc[j]
		nb1p=nb1[j]/nc[j]
		nb2p=nb2[j]/nc[j]
		nb3p=nb3[j]/nc[j]
		nb4p=nb4[j]/nc[j]
		nb5p=nb5[j]/nc[j]
		nb6p=nb6[j]/nc[j]
		nb7p=nb7[j]/nc[j]
		nb8p=nb8[j]/nc[j]
		nb9p=nb9[j]/nc[j]
		npry=nc[j]/957
		t1=0
		t2=0
		t3=0
		t4=0
		t5=0
		t6=0
		t7=0
		t8=0
		t9=0
		nt1=0
		nt2=0
		nt3=0
		nt4=0
		nt5=0
		nt6=0
		nt7=0
		nt8=0
		nt9=0
		if (p1[j]=='x'):
			t1=x1p
		elif (p1[j]=='o'):
			t1=o1p
		else:
			t1=b1p
		if (p2[j]=='x'):
			t2=x2p
		elif (p2[j]=='o'):
			t2=o2p
		else:
			t2=b2p
		if (p3[j]=='x'):
			t3=x3p
		elif (p3[j]=='o'):
			t3=o3p
		else:
			t3=b3p
		if (p4[j]=='x'):
			t4=x4p
		elif (p4[j]=='o'):
			t4=o4p
		else:
			t4=b4p
		if (p5[j]=='x'):
			t5=x5p
		elif (p5[j]=='o'):
			t5=o5p
		else:
			t5=b5p
		if (p6[j]=='x'):
			t6=x6p
		elif (p6[j]=='o'):
			t6=o6p
		else:
			t6=b6p
		if (p7[j]=='x'):
			t7=x7p
		elif (p7[j]=='o'):
			t7=o7p
		else:
			t7=b7p
		if (p8[j]=='x'):
			t8=x8p
		elif (p8[j]=='o'):
			t8=o8p
		else:
			t8=b8p
		if (p9[j]=='x'):
			t9=x9p
		elif (p9[j]=='o'):
			t9=o9p
		else:
			t9=b9p
		if (p1[j]=='x'):
			nt1=nx1p
		elif (p1[j]=='o'):
			nt1=no1p
		else:
			nt1=nb1p
		if (p2[j]=='x'):
			nt2=nx2p
		elif (p2[j]=='o'):
			nt2=no2p
		else:
			nt2=nb2p
		if (p3[j]=='x'):
			nt3=nx3p
		elif (p3[j]=='o'):
			nt3=no3p
		else:
			nt3=nb3p
		if (p4[j]=='x'):
			nt4=nx4p
		elif (p4[j]=='o'):
			nt4=no4p
		else:
			nt4=nb4p
		if (p5[j]=='x'):
			nt5=nx5p
		elif (p5[j]=='o'):
			nt5=no5p
		else:
			nt5=nb5p
		if (p6[j]=='x'):
			nt6=nx6p
		elif (p6[j]=='o'):
			nt6=no6p
		else:
			nt6=nb6p
		if (p7[j]=='x'):
			nt7=nx7p
		elif (p7[j]=='o'):
			nt7=no7p
		else:
			nt7=nb7p
		if (p8[j]=='x'):
			nt8=nx8p
		elif (p8[j]=='o'):
			nt8=no8p
		else:
			nt8=nb8p
		if (p9[j]=='x'):
			nt9=nx9p
		elif (p9[j]=='o'):
			nt9=no9p
		else:
			nt9=nb9p		
		prpy=pry*(t1*t2*t3*t4*t5*t6*t7*t8*t9)
		prpn=npry*nt1*nt2*nt3*nt4*nt5*nt6*nt7*nt8*nt9
		if (res[j]=='positive'):
			if (prpy>prpn):
				acc+=1
		else:
			if (prpn>prpy):
				acc+=1
	#print(acc)
	act=(acc/958)*100
	print(act)		

