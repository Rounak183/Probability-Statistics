import csv
with open('shuttle.csv',mode='r') as file:
	data=csv.DictReader(file,delimiter=',')
	c=[]
	for rwoo in data:
		c.append(rwoo)
	cl=[]
	st=[]
	er=[]
	si=[]
	wi=[]
	mg=[]
	vi=[]
	for row in c:
		cl.append(row['Class'])
		st.append(row['Stability'])
		er.append(row['Error'])
		si.append(row['Sign'])
		wi.append(row['Wind'])
		mg.append(row['Magnitude'])
		vi.append(row['Visibility'])
	yst1=[]
	yer1=[]
	ysi1=[]
	ywi1=[]
	ymg1=[]
	yvi1=[]
	yst2=[]
	yer2=[]
	ysi2=[]
	ywi2=[]
	ymg2=[]
	yvi2=[]
	yer3=[]
	yer4=[]	
	ymg3=[]
	ymg4=[]
	nst1=[]
	ner1=[]
	nsi1=[]
	nwi1=[]
	nmg1=[]
	nvi1=[]
	nst2=[]
	ner2=[]
	nsi2=[]
	nwi2=[]
	nmg2=[]
	nvi2=[]
	ner3=[]
	ner4=[]	
	nmg3=[]
	nmg4=[]
	c1=[]
	c2=[]
	acc=0
	for i in range(0,15):
		yst1.append(0)
		yer1.append(0)
		ysi1.append(0)
		ywi1.append(0)
		ymg1.append(0)
		yvi1.append(0)
		yst2.append(0)
		yer2.append(0)
		ysi2.append(0)
		ywi2.append(0)
		ymg2.append(0)
		yvi2.append(0)
		yer3.append(0)
		yer4.append(0)
		ymg3.append(0)
		ymg4.append(0)
		nst1.append(0)
		ner1.append(0)
		nsi1.append(0)
		nwi1.append(0)
		nmg1.append(0)
		nvi1.append(0)
		nst2.append(0)
		ner2.append(0)
		nsi2.append(0)
		nwi2.append(0)
		nmg2.append(0)
		nvi2.append(0)
		ner3.append(0)
		ner4.append(0)
		nmg3.append(0)
		nmg4.append(0)
		c1.append(0)
		c2.append(0)
	for j in range(0,15):
		for i in range(0,15):
			if (i!=j):
				if (cl[i]=='1'):
					if (st[i]=='1'):
						yst1[j]+=1 
					else:
						yst2[j]+=1
					if (er[i]=='1'):
						yer1[j]+=1
					elif (er[i]=='2'):
						yer2[j]+=1
					elif (er[i]=='3'):
						yer3[j]+=1
					else:
						yer4[j]+=1
					if (si[i]=='1'):
						ysi1[j]+=1
					else:
						ysi2[j]+=1
					if (wi[i]=='1'):
						ywi1[j]+=1
					else:
						ywi2[j]+=1
					if (mg[i]=='1'):
						ymg1[j]+=1
					elif (mg[i]=='2'):
						ymg2[j]+=1
					elif (mg[i]=='3'):
						ymg3[j]+=1
					else:
						ymg4[j]+=1		
					if (vi[i]=='1'):
						yvi1[j]+=1
					else:
						yvi2[j]+=1
					c1[j]+=1
				else:
					if (st[i]=='1'):
						nst1[j]+=1 
					else:
						nst2[j]+=1
					if (er[i]=='1'):
						ner1[j]+=1
					elif (er[i]=='2'):
						ner2[j]+=1
					elif (er[i]=='3'):
						ner3[j]+=1
					else:
						ner4[j]+=1
					if (si[i]=='1'):
						nsi1[j]+=1
					else:
						nsi2[j]+=1
					if (wi[i]=='1'):
						nwi1[j]+=1
					else:
						nwi2[j]+=1
					if (mg[i]=='1'):
						nmg1[j]+=1
					elif (mg[i]=='2'):
						nmg2[j]+=1
					elif (mg[i]=='3'):
						nmg3[j]+=1
					else:
						nmg4[j]+=1		
					if (vi[i]=='1'):
						nvi1[j]+=1
					else:
						nvi2[j]+=1
					c2[j]+=1
		pyst1=yst1[j]/c1[j]
		pyer1=yer1[j]/c1[j]
		pysi1=ysi1[j]/c1[j]
		pywi1=ywi1[j]/c1[j]
		pymg1=ymg1[j]/c1[j]
		pyvi1=yvi1[j]/c1[j]
		pyst2=yst2[j]/c1[j]
		pyer2=yer2[j]/c1[j]
		pysi2=ysi2[j]/c1[j]
		pywi2=ywi2[j]/c1[j]
		pymg2=ymg2[j]/c1[j]
		pyvi2=yvi2[j]/c1[j]
		pyer3=yer3[j]/c1[j]
		pyer4=yer4[j]/c1[j]	
		pymg3=ymg3[j]/c1[j]
		pymg4=ymg4[j]/c1[j]
		pnst1=nst1[j]/c2[j]
		pner1=ner1[j]/c2[j]
		pnsi1=nsi1[j]/c2[j]
		pnwi1=nwi1[j]/c2[j]
		pnmg1=nmg1[j]/c2[j]
		pnvi1=nvi1[j]/c2[j]
		pnst2=nst2[j]/c2[j]
		pner2=ner2[j]/c2[j]
		pnsi2=nsi2[j]/c2[j]
		pnwi2=nwi2[j]/c2[j]
		pnmg2=nmg2[j]/c2[j]
		pnvi2=nvi2[j]/c2[j]
		pner3=ner3[j]/c2[j]
		pner4=ner4[j]/c2[j]
		pnmg3=nmg3[j]/c2[j]
		pnmg4=nmg4[j]/c2[j]
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
		py=c1[j]/14
		pn=c2[j]/14
		if (st[j]=='1'):
			t1=pyst1
		else:
			t2=pyst2
		if (er[j]=='1'):
			t2=pyer1
		elif (er[j]=='2'):
			t2=pyer2
		elif (er[j]=='3'):
			t2=pyer3
		else:
			t2=pyer4
		if (si[j]=='1'):
			t3=pysi1
		else:
			t3=pysi2
		if (wi[j]=='1'):
			t4=pywi1
		else:
			t4=pywi2
		if (mg[j]=='1'):
			t5=pymg1
		elif (mg[j]=='2'):
			t5=pymg2
		elif (mg[j]=='3'):
			t5=pymg3
		else:
			t5=pymg4
		if (vi[j]=='1'):
			t6=pyvi1
		else:
			t6=pyvi2
		if (st[j]=='1'):
			nt1=pnst1
		else:
			nt2=pnst2
		if (er[j]=='1'):
			nt2=pner1
		elif (er[j]=='2'):
			nt2=pner2
		elif (er[j]=='3'):
			nt2=pner3
		else:
			nt2=pner4
		if (si[j]=='1'):
			nt3=pnsi1
		else:
			nt3=pnsi2
		if (wi[j]=='1'):
			nt4=pnwi1
		else:
			nt4=pnwi2
		if (mg[j]=='1'):
			nt5=pnmg1
		elif (mg[j]=='2'):
			nt5=pnmg2
		elif (mg[j]=='3'):
			nt5=pnmg3
		else:
			nt5=pnmg4
		if (vi[j]=='1'):
			nt6=pnvi1
		else:
			nt6=pnvi2														
		prpy=py*t1*t2*t3*t4*t5*t6
		prpn=pn*nt1*nt2*nt3*nt4*nt5*nt6
		if (cl[j]=='1'):
			if (prpy>=prpn):
				acc+=1
		else:
			if (prpn>=prpy):
				acc+=1
	act=(acc/15)*100
	print(act)				

