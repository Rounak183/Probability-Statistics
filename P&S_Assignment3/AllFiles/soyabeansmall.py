import csv
with open('soybean-small.csv',mode='r') as file:
	data=csv.DictReader(file,delimiter=',')
	c=[]
	for rwoo in data:
		c.append(rwoo)
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
	a23=[]
	a24=[]
	a25=[]
	a26=[]
	a27=[]
	a28=[]
	a29=[]
	a30=[]
	a31=[]
	a32=[]
	a33=[]
	a34=[]
	a35=[]
	cl=[]
	for row in c:
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
		a23.append(row['a23'])
		a24.append(row['a24'])
		a25.append(row['a25'])
		a26.append(row['a26'])
		a27.append(row['a27'])
		a28.append(row['a28'])
		a29.append(row['a29'])
		a30.append(row['a30'])
		a31.append(row['a31'])
		a32.append(row['a32'])
		a33.append(row['a33'])
		a34.append(row['a34'])
		a35.append(row['a35'])
		cl.append(row['class'])
	d1a10=[]
	d1a11=[]
	d1a12=[]
	d1a13=[]
	d1a14=[]
	d1a15=[]
	d1a16=[]
	d1a20=[]
	d1a21=[]
	d1a30=[]
	d1a31=[]
	d1a32=[]
	d1a40=[]
	d1a41=[]
	d1a42=[]
	d1a50=[]
	d1a51=[]
	d1a60=[]
	d1a61=[]
	d1a62=[]
	d1a63=[]
	d1a70=[]
	d1a71=[]
	d1a72=[]
	d1a73=[]
	d1a81=[]
	d1a82=[]
	d1a90=[]
	d1a91=[]
	d1a100=[]
	d1a101=[]
	d1a102=[]
	d1a111=[]
	d1a120=[]
	d1a121=[]
	d1a130=[]
	d1a142=[]
	d1a152=[]
	d1a160=[]
	d1a170=[]
	d1a180=[]
	d1a191=[]
	d1a200=[]
	d1a201=[]
	d1a210=[]
	d1a211=[]
	d1a212=[]
	d1a213=[]
	d1a220=[]
	d1a221=[]
	d1a222=[]
	d1a223=[]
	d1a230=[]
	d1a231=[]
	d1a240=[]
	d1a241=[]
	d1a250=[]
	d1a251=[]
	d1a260=[]
	d1a262=[]
	d1a270=[]
	d1a271=[]
	d1a280=[]
	d1a283=[]
	d1a294=[]
	d1a300=[]
	d1a310=[]
	d1a320=[]
	d1a330=[]
	d1a340=[]
	d1a350=[]
	d1a351=[]
	d2a10=[]
	d2a11=[]
	d2a12=[]
	d2a13=[]
	d2a14=[]
	d2a15=[]
	d2a16=[]
	d2a20=[]
	d2a21=[]
	d2a30=[]
	d2a31=[]
	d2a32=[]
	d2a40=[]
	d2a41=[]
	d2a42=[]
	d2a50=[]
	d2a51=[]
	d2a60=[]
	d2a61=[]
	d2a62=[]
	d2a63=[]
	d2a70=[]
	d2a71=[]
	d2a72=[]
	d2a73=[]
	d2a81=[]
	d2a82=[]
	d2a90=[]
	d2a91=[]
	d2a100=[]
	d2a101=[]
	d2a102=[]
	d2a111=[]
	d2a120=[]
	d2a121=[]
	d2a130=[]
	d2a142=[]
	d2a152=[]
	d2a160=[]
	d2a170=[]
	d2a180=[]
	d2a191=[]
	d2a200=[]
	d2a201=[]
	d2a210=[]
	d2a211=[]
	d2a212=[]
	d2a213=[]
	d2a220=[]
	d2a221=[]
	d2a222=[]
	d2a223=[]
	d2a230=[]
	d2a231=[]
	d2a240=[]
	d2a241=[]
	d2a250=[]
	d2a251=[]
	d2a260=[]
	d2a262=[]
	d2a270=[]
	d2a271=[]
	d2a280=[]
	d2a283=[]
	d2a294=[]
	d2a300=[]
	d2a310=[]
	d2a320=[]
	d2a330=[]
	d2a340=[]
	d2a350=[]
	d2a351=[]
	d3a10=[]
	d3a11=[]
	d3a12=[]
	d3a13=[]
	d3a14=[]
	d3a15=[]
	d3a16=[]
	d3a20=[]
	d3a21=[]
	d3a30=[]
	d3a31=[]
	d3a32=[]
	d3a40=[]
	d3a41=[]
	d3a42=[]
	d3a50=[]
	d3a51=[]
	d3a60=[]
	d3a61=[]
	d3a62=[]
	d3a63=[]
	d3a70=[]
	d3a71=[]
	d3a72=[]
	d3a73=[]
	d3a81=[]
	d3a82=[]
	d3a90=[]
	d3a91=[]
	d3a100=[]
	d3a101=[]
	d3a102=[]
	d3a111=[]
	d3a120=[]
	d3a121=[]
	d3a130=[]
	d3a142=[]
	d3a152=[]
	d3a160=[]
	d3a170=[]
	d3a180=[]
	d3a191=[]
	d3a200=[]
	d3a201=[]
	d3a210=[]
	d3a211=[]
	d3a212=[]
	d3a213=[]
	d3a220=[]
	d3a221=[]
	d3a222=[]
	d3a223=[]
	d3a230=[]
	d3a231=[]
	d3a240=[]
	d3a241=[]
	d3a250=[]
	d3a251=[]
	d3a260=[]
	d3a262=[]
	d3a270=[]
	d3a271=[]
	d3a280=[]
	d3a283=[]
	d3a294=[]
	d3a300=[]
	d3a310=[]
	d3a320=[]
	d3a330=[]
	d3a340=[]
	d3a350=[]
	d3a351=[]
	d4a10=[]
	d4a11=[]
	d4a12=[]
	d4a13=[]
	d4a14=[]
	d4a15=[]
	d4a16=[]
	d4a20=[]
	d4a21=[]
	d4a30=[]
	d4a31=[]
	d4a32=[]
	d4a40=[]
	d4a41=[]
	d4a42=[]
	d4a50=[]
	d4a51=[]
	d4a60=[]
	d4a61=[]
	d4a62=[]
	d4a63=[]
	d4a70=[]
	d4a71=[]
	d4a72=[]
	d4a73=[]
	d4a81=[]
	d4a82=[]
	d4a90=[]
	d4a91=[]
	d4a100=[]
	d4a101=[]
	d4a102=[]
	d4a111=[]
	d4a120=[]
	d4a121=[]
	d4a130=[]
	d4a142=[]
	d4a152=[]
	d4a160=[]
	d4a170=[]
	d4a180=[]
	d4a191=[]
	d4a200=[]
	d4a201=[]
	d4a210=[]
	d4a211=[]
	d4a212=[]
	d4a213=[]
	d4a220=[]
	d4a221=[]
	d4a222=[]
	d4a223=[]
	d4a230=[]
	d4a231=[]
	d4a240=[]
	d4a241=[]
	d4a250=[]
	d4a251=[]
	d4a260=[]
	d4a262=[]
	d4a270=[]
	d4a271=[]
	d4a280=[]
	d4a283=[]
	d4a294=[]
	d4a300=[]
	d4a310=[]
	d4a320=[]
	d4a330=[]
	d4a340=[]
	d4a350=[]
	d4a351=[]
	cd1=[]
	cd2=[]
	cd3=[]
	cd4=[]
	acc=0
	acc=24
	for i in range(0,47):
		d1a10.append(0)
		d1a11.append(0)
		d1a12.append(0)
		d1a13.append(0)
		d1a14.append(0)
		d1a15.append(0)
		d1a16.append(0)
		d1a20.append(0)
		d1a21.append(0)
		d1a30.append(0)
		d1a31.append(0)
		d1a32.append(0)
		d1a40.append(0)
		d1a41.append(0)
		d1a42.append(0)
		d1a50.append(0)
		d1a51.append(0)
		d1a60.append(0)
		d1a61.append(0)
		d1a62.append(0)
		d1a63.append(0)
		d1a70.append(0)
		d1a71.append(0)
		d1a72.append(0)
		d1a73.append(0)
		d1a81.append(0)
		d1a82.append(0)
		d1a90.append(0)
		d1a91.append(0)
		d1a100.append(0)
		d1a101.append(0)
		d1a102.append(0)
		d1a111.append(0)
		d1a120.append(0)
		d1a121.append(0)
		d1a130.append(0)
		d1a142.append(0)
		d1a152.append(0)
		d1a160.append(0)
		d1a170.append(0)
		d1a180.append(0)
		d1a191.append(0)
		d1a200.append(0)
		d1a201.append(0)
		d1a210.append(0)
		d1a211.append(0)
		d1a212.append(0)
		d1a213.append(0)
		d1a220.append(0)
		d1a221.append(0)
		d1a222.append(0)
		d1a223.append(0)
		d1a230.append(0)
		d1a231.append(0)
		d1a240.append(0)
		d1a241.append(0)
		d1a250.append(0)
		d1a251.append(0)
		d1a260.append(0)
		d1a262.append(0)
		d1a270.append(0)
		d1a271.append(0)
		d1a280.append(0)
		d1a283.append(0)
		d1a294.append(0)
		d1a300.append(0)
		d1a310.append(0)
		d1a320.append(0)
		d1a330.append(0)
		d1a340.append(0)
		d1a350.append(0)
		d1a351.append(0)
		d2a10.append(0)
		d2a11.append(0)
		d2a12.append(0)
		d2a13.append(0)
		d2a14.append(0)
		d2a15.append(0)
		d2a16.append(0)
		d2a20.append(0)
		d2a21.append(0)
		d2a30.append(0)
		d2a31.append(0)
		d2a32.append(0)
		d2a40.append(0)
		d2a41.append(0)
		d2a42.append(0)
		d2a50.append(0)
		d2a51.append(0)
		d2a60.append(0)
		d2a61.append(0)
		d2a62.append(0)
		d2a63.append(0)
		d2a70.append(0)
		d2a71.append(0)
		d2a72.append(0)
		d2a73.append(0)
		d2a81.append(0)
		d2a82.append(0)
		d2a90.append(0)
		d2a91.append(0)
		d2a100.append(0)
		d2a101.append(0)
		d2a102.append(0)
		d2a111.append(0)
		d2a120.append(0)
		d2a121.append(0)
		d2a130.append(0)
		d2a142.append(0)
		d2a152.append(0)
		d2a160.append(0)
		d2a170.append(0)
		d2a180.append(0)
		d2a191.append(0)
		d2a200.append(0)
		d2a201.append(0)
		d2a210.append(0)
		d2a211.append(0)
		d2a212.append(0)
		d2a213.append(0)
		d2a220.append(0)
		d2a221.append(0)
		d2a222.append(0)
		d2a223.append(0)
		d2a230.append(0)
		d2a231.append(0)
		d2a240.append(0)
		d2a241.append(0)
		d2a250.append(0)
		d2a251.append(0)
		d2a260.append(0)
		d2a262.append(0)
		d2a270.append(0)
		d2a271.append(0)
		d2a280.append(0)
		d2a283.append(0)
		d2a294.append(0)
		d2a300.append(0)
		d2a310.append(0)
		d2a320.append(0)
		d2a330.append(0)
		d2a340.append(0)
		d2a350.append(0)
		d2a351.append(0)
		d3a10.append(0)
		d3a11.append(0)
		d3a12.append(0)
		d3a13.append(0)
		d3a14.append(0)
		d3a15.append(0)
		d3a16.append(0)
		d3a20.append(0)
		d3a21.append(0)
		d3a30.append(0)
		d3a31.append(0)
		d3a32.append(0)
		d3a40.append(0)
		d3a41.append(0)
		d3a42.append(0)
		d3a50.append(0)
		d3a51.append(0)
		d3a60.append(0)
		d3a61.append(0)
		d3a62.append(0)
		d3a63.append(0)
		d3a70.append(0)
		d3a71.append(0)
		d3a72.append(0)
		d3a73.append(0)
		d3a81.append(0)
		d3a82.append(0)
		d3a90.append(0)
		d3a91.append(0)
		d3a100.append(0)
		d3a101.append(0)
		d3a102.append(0)
		d3a111.append(0)
		d3a120.append(0)
		d3a121.append(0)
		d3a130.append(0)
		d3a142.append(0)
		d3a152.append(0)
		d3a160.append(0)
		d3a170.append(0)
		d3a180.append(0)
		d3a191.append(0)
		d3a200.append(0)
		d3a201.append(0)
		d3a210.append(0)
		d3a211.append(0)
		d3a212.append(0)
		d3a213.append(0)
		d3a220.append(0)
		d3a221.append(0)
		d3a222.append(0)
		d3a223.append(0)
		d3a230.append(0)
		d3a231.append(0)
		d3a240.append(0)
		d3a241.append(0)
		d3a250.append(0)
		d3a251.append(0)
		d3a260.append(0)
		d3a262.append(0)
		d3a270.append(0)
		d3a271.append(0)
		d3a280.append(0)
		d3a283.append(0)
		d3a294.append(0)
		d3a300.append(0)
		d3a310.append(0)
		d3a320.append(0)
		d3a330.append(0)
		d3a340.append(0)
		d3a350.append(0)
		d3a351.append(0)
		d4a10.append(0)
		d4a11.append(0)
		d4a12.append(0)
		d4a13.append(0)
		d4a14.append(0)
		d4a15.append(0)
		d4a16.append(0)
		d4a20.append(0)
		d4a21.append(0)
		d4a30.append(0)
		d4a31.append(0)
		d4a32.append(0)
		d4a40.append(0)
		d4a41.append(0)
		d4a42.append(0)
		d4a50.append(0)
		d4a51.append(0)
		d4a60.append(0)
		d4a61.append(0)
		d4a62.append(0)
		d4a63.append(0)
		d4a70.append(0)
		d4a71.append(0)
		d4a72.append(0)
		d4a73.append(0)
		d4a81.append(0)
		d4a82.append(0)
		d4a90.append(0)
		d4a91.append(0)
		d4a100.append(0)
		d4a101.append(0)
		d4a102.append(0)
		d4a111.append(0)
		d4a120.append(0)
		d4a121.append(0)
		d4a130.append(0)
		d4a142.append(0)
		d4a152.append(0)
		d4a160.append(0)
		d4a170.append(0)
		d4a180.append(0)
		d4a191.append(0)
		d4a200.append(0)
		d4a201.append(0)
		d4a210.append(0)
		d4a211.append(0)
		d4a212.append(0)
		d4a213.append(0)
		d4a220.append(0)
		d4a221.append(0)
		d4a222.append(0)
		d4a223.append(0)
		d4a230.append(0)
		d4a231.append(0)
		d4a240.append(0)
		d4a241.append(0)
		d4a250.append(0)
		d4a251.append(0)
		d4a260.append(0)
		d4a262.append(0)
		d4a270.append(0)
		d4a271.append(0)
		d4a280.append(0)
		d4a283.append(0)
		d4a294.append(0)
		d4a300.append(0)
		d4a310.append(0)
		d4a320.append(0)
		d4a330.append(0)
		d4a340.append(0)
		d4a350.append(0)
		d4a351.append(0)
		cd1.append(0)
		cd2.append(0)
		cd3.append(0)
		cd4.append(0)
	for j in range(0,47):
		for i in range(0,47):
			if (i!=j):
				if (cl[i]=='D1'):
					if (a1[i]=='0'):
						d1a10[j]+=1
					elif (a1[i]=='1'):
						d1a11[j]+=1
					elif (a1[i]=='2'):
						d1a12[j]+=1
					elif (a1[i]=='3'):
						d1a13[j]+=1
					elif (a1[i]=='4'):
						d1a14[j]+=1
					elif (a1[i]=='5'):
						d1a15[j]+=1
					else:
						d1a16[j]+=1
					if (a2[i]=='0'):
						d1a20[j]+=1
					else:
						d1a21[j]+=1
					if (a3[i]=='0'):
						d1a30[j]+=1
					elif (a3[i]=='1'):
						d1a31[j]+=1
					else:
						d1a32[j]+=1
					if (a4[i]=='0'):
						d1a40[j]+=1
					elif (a4[i]=='1'):
						d1a41[j]+=1
					else:
						d1a42[j]+=1
					if (a5[i]=='0'):
						d1a50[j]+=1
					else:
						d1a51[j]+=1
					if (a6[i]=='0'):
						d1a60[j]+=1
					elif (a6[i]=='1'):
						d1a61[j]+=1
					elif (a6[i]=='2'):
						d1a62[j]+=1
					else:
						d1a63[j]+=1
					if (a7[i]=='0'):
						d1a70[j]+=1
					elif (a7[i]=='1'):
						d1a71[j]+=1
					elif (a7[i]=='2'):
						d1a72[j]+=1
					else:
						d1a73[j]+=1
					if (a8[i]=='1'):
						d1a81[j]+=1
					else:
						d1a82[j]+=1
					if (a9[i]=='0'):
						d1a90[j]+=1
					else:
						d1a91[j]+=1
					if (a10[i]=='0'):
						d1a100[j]+=1
					elif (a10[i]=='1'):
						d1a101[j]+=1
					else:
						d1a102[j]+=1
					d1a111[j]+=1
					if (a12[i]=='0'):
						d1a120[j]+=1
					else:
						d1a121[j]+=1
					d1a130[j]+=1
					d1a142[j]+=1
					d1a152[j]+=1
					d1a160[j]+=1						
					d1a170[j]+=1
					d1a180[j]+=1	
					d1a191[j]+=1
					if (a20[i]=='0'):
						d1a200[j]+=1
					else:
						d1a201[j]+=1
					if (a21[i]=='0'):
						d1a210[j]+=1
					elif (a21[i]=='1'):
						d1a211[j]+=1
					elif (a21[i]=='2'):
						d1a212[j]+=1
					else:
						d1a213[j]+=1
					if (a22[i]=='0'):
						d1a220[j]+=1
					elif (a22[i]=='1'):
						d1a221[j]+=1
					elif (a22[i]=='2'):
						d1a222[j]+=1
					else:	
						d1a223[j]+=1
					if (a23[i]=='0'):
						d1a230[j]+=1
					else:
						d1a231[j]+=1
					if (a24[i]=='0'):
						d1a240[j]+=1
					else:
						d1a241[j]+=1
					if (a25[i]=='0'):
						d1a250[j]+=1
					else:
						d1a251[j]+=1
					if (a26[i]=='0'):
						d1a260[j]+=1
					else:
						d1a262[j]+=1
					if (a27[i]=='0'):
						d1a270[j]+=1
					else:
						d1a271[j]+=1
					if (a28[i]=='0'):
						d1a280[j]+=1
					else:
						d1a283[j]+=1
					d1a294[j]+=1
					d1a300[j]+=1
					d1a310[j]+=1
					d1a320[j]+=1
					d1a330[j]+=1
					d1a340[j]+=1
					if (a35[i]=='0'):
						d1a350[j]+=1
					else:	
						d1a351[j]+=1
					cd1[j]+=1	
				elif (cl[i]=='D2'):
					if (a1[i]=='0'):
						d2a10[j]+=1
					elif (a1[i]=='1'):
						d2a11[j]+=1
					elif (a1[i]=='2'):
						d2a12[j]+=1
					elif (a1[i]=='3'):
						d2a13[j]+=1
					elif (a1[i]=='4'):
						d2a14[j]+=1
					elif (a1[i]=='5'):
						d2a15[j]+=1
					else:
						d2a16[j]+=1
					if (a2[i]=='0'):
						d2a20[j]+=1
					else:
						d2a21[j]+=1
					if (a3[i]=='0'):
						d2a30[j]+=1
					elif (a3[i]=='1'):
						d2a31[j]+=1
					else:
						d2a32[j]+=1
					if (a4[i]=='0'):
						d2a40[j]+=1
					elif (a4[i]=='1'):
						d2a41[j]+=1
					else:
						d2a42[j]+=1
					if (a5[i]=='0'):
						d2a50[j]+=1
					else:
						d2a51[j]+=1
					if (a6[i]=='0'):
						d2a60[j]+=1
					elif (a6[i]=='1'):
						d2a61[j]+=1
					elif (a6[i]=='2'):
						d2a62[j]+=1
					else:
						d2a63[j]+=1
					if (a7[i]=='0'):
						d2a70[j]+=1
					elif (a7[i]=='1'):
						d2a71[j]+=1
					elif (a7[i]=='2'):
						d2a72[j]+=1
					else:
						d2a73[j]+=1
					if (a8[i]=='1'):
						d2a81[j]+=1
					else:
						d2a82[j]+=1
					if (a9[i]=='0'):
						d2a90[j]+=1
					else:
						d2a91[j]+=1
					if (a10[i]=='0'):
						d2a100[j]+=1
					elif (a10[i]=='1'):
						d2a101[j]+=1
					else:
						d2a102[j]+=1
					d2a111[j]+=1
					if (a2[i]=='0'):
						d2a120[j]+=1
					else:
						d2a121[j]+=1
					d2a130[j]+=1
					d2a142[j]+=1
					d2a152[j]+=1
					d2a160[j]+=1						
					d2a170[j]+=1
					d2a180[j]+=1	
					d2a191[j]+=1
					if (a20[i]=='0'):
						d2a200[j]+=1
					else:
						d2a201[j]+=1
					if (a21[i]=='0'):
						d2a210[j]+=1
					elif (a21[i]=='1'):
						d2a211[j]+=1
					elif (a21[i]=='2'):
						d2a212[j]+=1
					else:
						d2a213[j]+=1
					if (a22[i]=='0'):
						d2a220[j]+=1
					elif (a22[i]=='1'):
						d2a221[j]+=1
					elif (a22[i]=='2'):
						d2a222[j]+=1
					else:	
						d2a223[j]+=1
					if (a23[i]=='0'):
						d2a230[j]+=1
					else:
						d2a231[j]+=1
					if (a24[i]=='0'):
						d2a240[j]+=1
					else:
						d2a241[j]+=1
					if (a25[i]=='0'):
						d2a250[j]+=1
					else:
						d2a251[j]+=1
					if (a26[i]=='0'):
						d2a260[j]+=1
					else:
						d2a262[j]+=1
					if (a27[i]=='0'):
						d2a270[j]+=1
					else:
						d2a271[j]+=1
					if (a28[i]=='0'):
						d2a280[j]+=1
					else:
						d2a283[j]+=1
					d2a294[j]+=1
					d2a300[j]+=1
					d2a310[j]+=1
					d2a320[j]+=1
					d2a330[j]+=1
					d2a340[j]+=1
					if (a35[i]=='0'):
						d2a350[j]+=1
					else:	
						d2a351[j]+=1
					cd2[j]+=1
				elif (cl[i]=='D3'):
					if (a1[i]=='0'):
						d3a10[j]+=1
					elif (a1[i]=='1'):
						d3a11[j]+=1
					elif (a1[i]=='2'):
						d3a12[j]+=1
					elif (a1[i]=='3'):
						d3a13[j]+=1
					elif (a1[i]=='4'):
						d3a14[j]+=1
					elif (a1[i]=='5'):
						d3a15[j]+=1
					else:
						d3a16[j]+=1
					if (a2[i]=='0'):
						d3a20[j]+=1
					else:
						d3a21[j]+=1
					if (a3[i]=='0'):
						d3a30[j]+=1
					elif (a3[i]=='1'):
						d3a31[j]+=1
					else:
						d3a32[j]+=1
					if (a4[i]=='0'):
						d3a40[j]+=1
					elif (a4[i]=='1'):
						d3a41[j]+=1
					else:
						d3a42[j]+=1
					if (a5[i]=='0'):
						d3a50[j]+=1
					else:
						d3a51[j]+=1
					if (a6[i]=='0'):
						d3a60[j]+=1
					elif (a6[i]=='1'):
						d3a61[j]+=1
					elif (a6[i]=='2'):
						d3a62[j]+=1
					else:
						d3a63[j]+=1
					if (a7[i]=='0'):
						d3a70[j]+=1
					elif (a7[i]=='1'):
						d3a71[j]+=1
					elif (a7[i]=='2'):
						d3a72[j]+=1
					else:
						d3a73[j]+=1
					if (a8[i]=='1'):
						d3a81[j]+=1
					else:
						d3a82[j]+=1
					if (a9[i]=='0'):
						d3a90[j]+=1
					else:
						d3a91[j]+=1
					if (a10[i]=='0'):
						d3a100[j]+=1
					elif (a10[i]=='1'):
						d3a101[j]+=1
					else:
						d3a102[j]+=1
					d3a111[j]+=1
					if (a12[i]=='0'):
						d3a120[j]+=1
					else:
						d3a121[j]+=1
					d3a130[j]+=1
					d3a142[j]+=1
					d3a152[j]+=1
					d3a160[j]+=1						
					d3a170[j]+=1
					d3a180[j]+=1	
					d3a191[j]+=1
					if (a20[i]=='0'):
						d3a200[j]+=1
					else:
						d3a201[j]+=1
					if (a21[i]=='0'):
						d3a210[j]+=1
					elif (a21[i]=='1'):
						d3a211[j]+=1
					elif (a21[i]=='2'):
						d3a212[j]+=1
					else:
						d3a213[j]+=1
					if (a22[i]=='0'):
						d3a220[j]+=1
					elif (a22[i]=='1'):
						d3a221[j]+=1
					elif (a22[i]=='2'):
						d3a222[j]+=1
					else:	
						d3a223[j]+=1
					if (a23[i]=='0'):
						d3a230[j]+=1
					else:
						d3a231[j]+=1
					if (a24[i]=='0'):
						d3a240[j]+=1
					else:
						d3a241[j]+=1
					if (a25[i]=='0'):
						d3a250[j]+=1
					else:
						d3a251[j]+=1
					if (a26[i]=='0'):
						d3a260[j]+=1
					else:
						d3a262[j]+=1
					if (a27[i]=='0'):
						d3a270[j]+=1
					else:
						d3a271[j]+=1
					if (a28[i]=='0'):
						d3a280[j]+=1
					else:
						d3a283[j]+=1
					d3a294[j]+=1
					d3a300[j]+=1
					d3a310[j]+=1
					d3a320[j]+=1
					d3a330[j]+=1
					d3a340[j]+=1
					if (a35[i]=='0'):
						d3a350[j]+=1
					else:	
						d3a351[j]+=1
					cd3[j]+=1
				else:
					if (a1[i]=='0'):
						d4a10[j]+=1
					elif (a1[i]=='1'):
						d4a11[j]+=1
					elif (a1[i]=='2'):
						d4a12[j]+=1
					elif (a1[i]=='3'):
						d4a13[j]+=1
					elif (a1[i]=='4'):
						d4a14[j]+=1
					elif (a1[i]=='5'):
						d4a15[j]+=1
					else:
						d4a16[j]+=1
					if (a2[i]=='0'):
						d4a20[j]+=1
					else:
						d4a21[j]+=1
					if (a3[i]=='0'):
						d4a30[j]+=1
					elif (a3[i]=='1'):
						d4a31[j]+=1
					else:
						d4a32[j]+=1
					if (a4[i]=='0'):
						d4a40[j]+=1
					elif (a4[i]=='1'):
						d4a41[j]+=1
					else:
						d4a42[j]+=1
					if (a5[i]=='0'):
						d4a50[j]+=1
					else:
						d4a51[j]+=1
					if (a6[i]=='0'):
						d4a60[j]+=1
					elif (a6[i]=='1'):
						d4a61[j]+=1
					elif (a6[i]=='2'):
						d4a62[j]+=1
					else:
						d4a63[j]+=1
					if (a7[i]=='0'):
						d4a70[j]+=1
					elif (a7[i]=='1'):
						d4a71[j]+=1
					elif (a7[i]=='2'):
						d4a72[j]+=1
					else:
						d4a73[j]+=1
					if (a8[i]=='1'):
						d4a81[j]+=1
					else:
						d4a82[j]+=1
					if (a9[i]=='0'):
						d4a90[j]+=1
					else:
						d4a91[j]+=1
					if (a10[i]=='0'):
						d4a100[j]+=1
					elif (a10[i]=='1'):
						d4a101[j]+=1
					else:
						d4a102[j]+=1
					d4a111[j]+=1
					if (a12[i]=='0'):
						d4a120[j]+=1
					else:
						d4a121[j]+=1
					d4a130[j]+=1
					d1a142[j]+=1
					d4a152[j]+=1
					d4a160[j]+=1					
					d4a170[j]+=1
					d4a180[j]+=1	
					d4a191[j]+=1
					if (a20[i]=='0'):
						d4a200[j]+=1
					else:
						d4a201[j]+=1
					if (a21[i]=='0'):
						d4a210[j]+=1
					elif (a21[i]=='1'):
						d4a211[j]+=1
					elif (a21[i]=='2'):
						d4a212[j]+=1
					else:
						d4a213[j]+=1
					if (a22[i]=='0'):
						d4a220[j]+=1
					elif (a22[i]=='1'):
						d4a221[j]+=1
					elif (a22[i]=='2'):
						d4a222[j]+=1
					else:	
						d4a223[j]+=1
					if (a23[i]=='0'):
						d4a230[j]+=1
					else:
						d4a231[j]+=1
					if (a24[i]=='0'):
						d4a240[j]+=1
					else:
						d4a241[j]+=1
					if (a25[i]=='0'):
						d4a250[j]+=1
					else:
						d4a251[j]+=1
					if (a26[i]=='0'):
						d4a260[j]+=1
					else:
						d4a262[j]+=1
					if (a27[i]=='0'):
						d4a270[j]+=1
					else:
						d4a271[j]+=1
					if (a28[i]=='0'):
						d4a280[j]+=1
					else:
						d4a283[j]+=1
					d4a294[j]+=1
					d4a300[j]+=1
					d4a310[j]+=1
					d4a320[j]+=1
					d4a330[j]+=1
					d4a340[j]+=1
					if (a35[i]=='0'):
						d4a350[j]+=1
					else:	
						d4a351[j]+=1
					cd4[j]+=1	
		pd1a10=d1a10[j]/cd1[j]
		pd1a11=d1a11[j]/cd1[j]
		pd1a12=d1a12[j]/cd1[j]
		pd1a13=d1a13[j]/cd1[j]
		pd1a14=d1a14[j]/cd1[j]
		pd1a15=d1a15[j]/cd1[j]							
		pd1a16=d1a16[j]/cd1[j]
		pd2a10=d2a10[j]/cd2[j]
		pd2a11=d2a11[j]/cd2[j]
		pd2a12=d2a12[j]/cd2[j]
		pd2a13=d2a13[j]/cd2[j]
		pd2a14=d2a14[j]/cd2[j]
		pd2a15=d2a15[j]/cd2[j]							
		pd2a16=d2a16[j]/cd2[j]
		pd3a10=d3a10[j]/cd3[j]
		pd3a11=d3a11[j]/cd3[j]
		pd3a12=d3a12[j]/cd3[j]
		pd3a13=d3a13[j]/cd3[j]
		pd3a14=d3a14[j]/cd3[j]
		pd3a15=d3a15[j]/cd3[j]							
		pd3a16=d3a16[j]/cd3[j]
		pd4a10=d4a10[j]/cd4[j]
		pd4a11=d4a11[j]/cd4[j]
		pd4a12=d4a12[j]/cd4[j]
		pd4a13=d4a13[j]/cd4[j]
		pd4a14=d4a14[j]/cd4[j]
		pd4a15=d4a15[j]/cd4[j]
		pd4a16=d4a16[j]/cd4[j]
		pd1a20=d1a20[j]/cd1[j]
		pd1a21=d1a21[j]/cd1[j]
		pd2a20=d2a20[j]/cd2[j]
		pd2a21=d2a21[j]/cd2[j]
		pd3a20=d3a20[j]/cd3[j]
		pd3a21=d3a21[j]/cd3[j]
		pd4a20=d4a20[j]/cd4[j]
		pd4a21=d4a21[j]/cd4[j]
		pd1a30=d1a30[j]/cd1[j]
		pd1a31=d1a31[j]/cd1[j]
		pd1a32=d1a32[j]/cd1[j]
		pd2a30=d2a30[j]/cd2[j]
		pd2a31=d2a31[j]/cd2[j]
		pd2a32=d2a32[j]/cd2[j]
		pd3a30=d3a30[j]/cd3[j]
		pd3a31=d3a31[j]/cd3[j]
		pd3a32=d3a32[j]/cd3[j]
		pd4a30=d4a30[j]/cd4[j]
		pd4a31=d4a31[j]/cd4[j]
		pd4a32=d4a32[j]/cd4[j]
		pd1a40=d1a40[j]/cd1[j]
		pd1a41=d1a41[j]/cd1[j]
		pd1a42=d1a42[j]/cd1[j]
		pd2a40=d2a40[j]/cd2[j]
		pd2a41=d2a41[j]/cd2[j]
		pd2a42=d2a42[j]/cd2[j]
		pd3a40=d3a40[j]/cd3[j]
		pd3a41=d3a41[j]/cd3[j]
		pd3a42=d3a42[j]/cd3[j]
		pd4a40=d4a40[j]/cd4[j]
		pd4a41=d4a41[j]/cd4[j]
		pd4a42=d4a42[j]/cd4[j]
		pd1a50=d1a50[j]/cd1[j]
		pd1a51=d1a51[j]/cd1[j]
		pd2a50=d2a50[j]/cd2[j]
		pd2a51=d2a51[j]/cd2[j]
		pd3a50=d3a50[j]/cd3[j]
		pd3a51=d3a51[j]/cd3[j]
		pd4a50=d4a50[j]/cd4[j]
		pd4a51=d4a51[j]/cd4[j]
		pd1a60=d1a60[j]/cd1[j]
		pd1a61=d1a61[j]/cd1[j]
		pd1a62=d1a62[j]/cd1[j]
		pd1a63=d1a63[j]/cd1[j]
		pd2a60=d2a60[j]/cd2[j]
		pd2a61=d2a61[j]/cd2[j]
		pd2a62=d2a62[j]/cd2[j]
		pd2a63=d2a63[j]/cd2[j]
		pd3a60=d3a60[j]/cd3[j]
		pd3a61=d3a61[j]/cd3[j]
		pd3a62=d3a62[j]/cd3[j]
		pd3a63=d3a63[j]/cd3[j]
		pd4a60=d4a60[j]/cd4[j]
		pd4a61=d4a61[j]/cd4[j]
		pd4a62=d4a62[j]/cd4[j]
		pd4a63=d4a63[j]/cd4[j]
		pd1a70=d1a70[j]/cd1[j]
		pd1a71=d1a71[j]/cd1[j]
		pd1a72=d1a72[j]/cd1[j]
		pd1a73=d1a73[j]/cd1[j]
		pd2a70=d2a70[j]/cd2[j]
		pd2a71=d2a71[j]/cd2[j]
		pd2a72=d2a72[j]/cd2[j]
		pd2a73=d2a73[j]/cd2[j]
		pd3a70=d3a70[j]/cd3[j]
		pd3a71=d3a71[j]/cd3[j]
		pd3a72=d3a72[j]/cd3[j]
		pd3a73=d3a73[j]/cd3[j]
		pd4a70=d4a70[j]/cd4[j]
		pd4a71=d4a71[j]/cd4[j]
		pd4a72=d4a72[j]/cd4[j]
		pd4a73=d4a73[j]/cd4[j]
		pd1a81=d1a81[j]/cd1[j]
		pd1a82=d1a82[j]/cd1[j]
		pd2a81=d2a81[j]/cd2[j]
		pd2a82=d2a82[j]/cd2[j]
		pd3a81=d3a81[j]/cd3[j]
		pd3a82=d3a82[j]/cd3[j]
		pd4a81=d4a81[j]/cd4[j]
		pd4a82=d4a82[j]/cd4[j]
		pd1a90=d1a90[j]/cd1[j]
		pd1a91=d1a91[j]/cd1[j]
		pd2a90=d2a90[j]/cd2[j]
		pd2a91=d2a91[j]/cd2[j]
		pd3a90=d3a90[j]/cd3[j]
		pd3a91=d3a91[j]/cd3[j]
		pd4a90=d4a90[j]/cd4[j]
		pd4a91=d4a91[j]/cd4[j]
		pd1a100=d1a100[j]/cd1[j]
		pd1a101=d1a101[j]/cd1[j]
		pd1a102=d1a102[j]/cd1[j]
		pd2a100=d1a100[j]/cd2[j]
		pd2a101=d1a101[j]/cd2[j]
		pd2a102=d1a102[j]/cd2[j]
		pd3a100=d1a100[j]/cd3[j]
		pd3a101=d1a101[j]/cd3[j]
		pd3a102=d1a102[j]/cd3[j]
		pd4a100=d4a100[j]/cd4[j]
		pd4a101=d4a101[j]/cd4[j]
		pd4a102=d4a102[j]/cd4[j]
		pd1a111=d1a111[j]/cd1[j]
		pd2a111=d2a111[j]/cd2[j]
		pd3a111=d3a111[j]/cd3[j]
		pd4a111=d4a111[j]/cd4[j]
		pd1a120=d1a120[j]/cd1[j]
		pd1a121=d1a121[j]/cd1[j]
		pd2a120=d2a120[j]/cd2[j]
		pd2a121=d2a121[j]/cd2[j]
		pd3a120=d3a120[j]/cd3[j]
		pd3a121=d3a121[j]/cd3[j]
		pd4a120=d4a120[j]/cd4[j]
		pd4a121=d4a121[j]/cd4[j]
		pd1a130=d1a130[j]/cd1[j]
		pd2a130=d2a130[j]/cd2[j]
		pd3a130=d3a130[j]/cd3[j]
		pd4a130=d4a130[j]/cd4[j]
		pd1a142=d1a142[j]/cd1[j]
		pd2a142=d2a142[j]/cd2[j]
		pd3a142=d3a142[j]/cd3[j]
		pd4a142=d4a142[j]/cd4[j]
		pd1a152=d1a152[j]/cd1[j]
		pd2a152=d2a152[j]/cd2[j]
		pd3a152=d3a152[j]/cd3[j]
		pd4a152=d4a152[j]/cd4[j]
		pd1a160=d1a160[j]/cd1[j]
		pd2a160=d2a160[j]/cd2[j]
		pd3a160=d3a160[j]/cd3[j]
		pd4a160=d4a160[j]/cd4[j]
		pd1a170=d1a170[j]/cd1[j]
		pd2a170=d2a170[j]/cd2[j]
		pd3a170=d3a170[j]/cd3[j]
		pd4a170=d4a170[j]/cd4[j]
		pd1a180=d1a180[j]/cd1[j]
		pd2a180=d2a180[j]/cd2[j]
		pd3a180=d3a180[j]/cd3[j]
		pd4a180=d4a180[j]/cd4[j]
		pd1a191=d1a191[j]/cd1[j]
		pd2a191=d2a191[j]/cd2[j]
		pd3a191=d3a191[j]/cd3[j]
		pd4a191=d4a191[j]/cd4[j]
		pd1a200=d1a200[j]/cd1[j]
		pd1a201=d1a201[j]/cd1[j]
		pd2a200=d2a200[j]/cd2[j]
		pd2a201=d2a201[j]/cd2[j]
		pd3a200=d3a200[j]/cd3[j]
		pd3a201=d3a201[j]/cd3[j]
		pd4a200=d4a200[j]/cd4[j]
		pd4a201=d4a201[j]/cd4[j]
		pd1a210=d1a210[j]/cd1[j]
		pd1a211=d1a211[j]/cd1[j]
		pd1a212=d1a212[j]/cd1[j]
		pd1a213=d1a213[j]/cd1[j]
		pd2a210=d2a210[j]/cd2[j]
		pd2a211=d2a211[j]/cd2[j]
		pd2a212=d2a212[j]/cd2[j]
		pd2a213=d2a213[j]/cd2[j]
		pd3a210=d3a210[j]/cd3[j]
		pd3a211=d3a211[j]/cd3[j]
		pd3a212=d3a212[j]/cd3[j]
		pd3a213=d3a213[j]/cd3[j]
		pd4a210=d4a210[j]/cd4[j]
		pd4a211=d4a211[j]/cd4[j]
		pd4a212=d4a212[j]/cd4[j]
		pd4a213=d4a213[j]/cd4[j]
		pd1a220=d1a220[j]/cd1[j]
		pd1a221=d1a221[j]/cd1[j]
		pd1a222=d1a222[j]/cd1[j]
		pd1a223=d1a223[j]/cd1[j]
		pd2a220=d2a220[j]/cd2[j]
		pd2a221=d2a221[j]/cd2[j]
		pd2a222=d2a222[j]/cd2[j]
		pd2a223=d2a223[j]/cd2[j]
		pd3a220=d3a220[j]/cd3[j]
		pd3a221=d3a221[j]/cd3[j]
		pd3a222=d3a222[j]/cd3[j]
		pd3a223=d3a223[j]/cd3[j]
		pd4a220=d4a220[j]/cd4[j]
		pd4a221=d4a221[j]/cd4[j]
		pd4a222=d4a222[j]/cd4[j]
		pd4a223=d4a223[j]/cd4[j]
		pd1a230=d1a230[j]/cd1[j]
		pd1a231=d1a231[j]/cd1[j]
		pd2a230=d2a230[j]/cd2[j]
		pd2a231=d2a231[j]/cd2[j]
		pd3a230=d3a230[j]/cd3[j]
		pd3a231=d3a231[j]/cd3[j]
		pd4a230=d4a230[j]/cd4[j]
		pd4a231=d4a231[j]/cd4[j]
		pd1a240=d1a240[j]/cd1[j]
		pd1a241=d1a241[j]/cd1[j]
		pd2a240=d2a240[j]/cd2[j]
		pd2a241=d2a241[j]/cd2[j]
		pd3a240=d3a240[j]/cd3[j]
		pd3a241=d3a241[j]/cd3[j]
		pd4a240=d4a240[j]/cd4[j]
		pd4a241=d4a241[j]/cd4[j]
		pd1a250=d1a250[j]/cd1[j]
		pd1a251=d1a251[j]/cd1[j]
		pd2a250=d2a250[j]/cd2[j]
		pd2a251=d2a251[j]/cd2[j]
		pd3a250=d3a250[j]/cd3[j]
		pd3a251=d3a251[j]/cd3[j]
		pd4a250=d4a250[j]/cd4[j]
		pd4a251=d4a251[j]/cd4[j]
		pd1a260=d1a260[j]/cd1[j]
		pd1a262=d1a262[j]/cd1[j]
		pd2a260=d2a260[j]/cd2[j]
		pd2a262=d2a262[j]/cd2[j]
		pd3a260=d3a260[j]/cd3[j]
		pd3a262=d3a262[j]/cd3[j]
		pd4a260=d4a260[j]/cd4[j]
		pd4a262=d4a262[j]/cd4[j]
		pd1a270=d1a270[j]/cd1[j]
		pd1a271=d1a271[j]/cd1[j]
		pd2a270=d2a270[j]/cd2[j]
		pd2a271=d2a271[j]/cd2[j]
		pd3a270=d3a270[j]/cd3[j]
		pd3a271=d3a271[j]/cd3[j]
		pd4a270=d4a270[j]/cd4[j]
		pd4a271=d4a271[j]/cd4[j]
		pd1a280=d1a280[j]/cd1[j]
		pd1a283=d1a283[j]/cd1[j]
		pd2a280=d2a280[j]/cd2[j]
		pd2a283=d2a283[j]/cd2[j]
		pd3a280=d3a280[j]/cd3[j]
		pd3a283=d3a283[j]/cd3[j]
		pd4a280=d4a280[j]/cd4[j]
		pd4a283=d4a283[j]/cd4[j]
		pd1a294=d1a294[j]/cd1[j]
		pd2a294=d2a294[j]/cd2[j]
		pd3a294=d3a294[j]/cd3[j]
		pd4a294=d4a294[j]/cd4[j]
		pd1a300=d1a300[j]/cd1[j]
		pd2a300=d2a300[j]/cd2[j]
		pd3a300=d3a300[j]/cd3[j]
		pd4a300=d4a300[j]/cd4[j]
		pd1a310=d1a310[j]/cd1[j]
		pd2a310=d2a310[j]/cd2[j]
		pd3a310=d3a310[j]/cd3[j]
		pd4a310=d4a310[j]/cd4[j]
		pd1a320=d1a320[j]/cd1[j]
		pd2a320=d2a320[j]/cd2[j]
		pd3a320=d3a320[j]/cd3[j]
		pd4a320=d4a320[j]/cd4[j]
		pd1a330=d1a330[j]/cd1[j]
		pd2a330=d2a330[j]/cd2[j]
		pd3a330=d3a330[j]/cd3[j]
		pd4a330=d4a330[j]/cd4[j]
		pd1a340=d1a340[j]/cd1[j]
		pd2a340=d2a340[j]/cd2[j]
		pd3a340=d3a340[j]/cd3[j]
		pd4a340=d4a340[j]/cd4[j]
		pd1a350=d1a350[j]/cd1[j]
		pd1a351=d1a351[j]/cd1[j]
		pd2a350=d2a350[j]/cd2[j]
		pd2a351=d2a351[j]/cd2[j]
		pd3a350=d3a350[j]/cd3[j]
		pd3a351=d3a351[j]/cd3[j]
		pd4a350=d4a350[j]/cd4[j]
		pd4a351=d4a351[j]/cd4[j]
		d1t1=0
		d1t2=0
		d1t3=0
		d1t4=0
		d1t5=0
		d1t6=0
		d1t7=0
		d1t8=0
		d1t9=0
		d1t10=0
		d1t11=0
		d1t12=0
		d1t13=0
		d1t14=0
		d1t15=0
		d1t16=0
		d1t17=0
		d1t18=0
		d1t19=0
		d1t20=0
		d1t21=0
		d1t22=0
		d1t23=0
		d1t24=0
		d1t25=0
		d1t26=0
		d1t27=0
		d1t28=0
		d1t29=0
		d1t30=0
		d1t31=0
		d1t32=0
		d1t33=0
		d1t34=0
		d1t35=0
		d2t1=0
		d2t2=0
		d2t3=0
		d2t4=0
		d2t5=0
		d2t6=0
		d2t7=0
		d2t8=0
		d2t9=0
		d2t10=0
		d2t11=0
		d2t12=0
		d2t13=0
		d2t14=0
		d2t15=0
		d2t16=0
		d2t17=0
		d2t18=0
		d2t19=0
		d2t20=0
		d2t21=0
		d2t22=0
		d2t23=0
		d2t24=0
		d2t25=0
		d2t26=0
		d2t27=0
		d2t28=0
		d2t29=0
		d2t30=0
		d2t31=0
		d2t32=0
		d2t33=0
		d2t34=0
		d2t35=0
		d3t1=0
		d3t2=0
		d3t3=0
		d3t4=0
		d3t5=0
		d3t6=0
		d3t7=0
		d3t8=0
		d3t9=0
		d3t10=0
		d3t11=0
		d3t12=0
		d3t13=0
		d3t14=0
		d3t15=0
		d3t16=0
		d3t17=0
		d3t18=0
		d3t19=0
		d3t20=0
		d3t21=0
		d3t22=0
		d3t23=0
		d3t24=0
		d3t25=0
		d3t26=0
		d3t27=0
		d3t28=0
		d3t29=0
		d3t30=0
		d3t31=0
		d3t32=0
		d3t33=0
		d3t34=0
		d3t35=0
		d4t1=0
		d4t2=0
		d4t3=0
		d4t4=0
		d4t5=0
		d4t6=0
		d4t7=0
		d4t8=0
		d4t9=0
		d4t10=0
		d4t11=0
		d4t12=0
		d4t13=0
		d4t14=0
		d4t15=0
		d4t16=0
		d4t17=0
		d4t18=0
		d4t19=0
		d4t20=0
		d4t21=0
		d4t22=0
		d4t23=0
		d4t24=0
		d4t25=0
		d4t26=0
		d4t27=0
		d4t28=0
		d4t29=0
		d4t30=0
		d4t31=0
		d4t32=0
		d4t33=0
		d4t34=0
		d4t35=0
		pd1=cd1[j]/46
		pd2=cd2[j]/46
		pd3=cd3[j]/46
		pd4=cd4[j]/46
		if (a1[j]=='0'):
			d1t1=pd1a10
			d2t1=pd2a10
			d3t1=pd3a10
			d4t1=pd4a10
		elif (a1[j]=='1'):
			d1t1=pd1a11
			d2t1=pd2a11
			d3t1=pd3a11
			d4t1=pd4a11	
		elif (a1[j]=='2'):
			d1t1=pd1a12
			d2t1=pd2a12
			d3t1=pd3a12
			d4t1=pd4a12
		elif (a1[j]=='3'):
			d1t1=pd1a13
			d2t1=pd2a13
			d3t1=pd3a13
			d4t1=pd4a13		
		elif (a1[j]=='4'):
			d1t1=pd1a14
			d2t1=pd2a14
			d3t1=pd3a14
			d4t1=pd4a14	
		elif (a1[j]=='5'):
			d1t1=pd1a15
			d2t1=pd2a15
			d3t1=pd3a15
			d4t1=pd4a15	
		else:
			d1t1=pd1a16
			d2t1=pd2a16
			d3t1=pd3a16
			d4t1=pd4a16
		if (a2[j]=='0'):
			d1t2=pd1a20
			d2t2=pd2a20
			d3t2=pd3a20
			d4t2=pd4a20		
		else:
			d1t2=pd1a21
			d2t2=pd2a21
			d3t2=pd3a21
			d4t2=pd4a21	
		if (a3[j]=='0'):
			d1t3=pd1a30
			d2t3=pd2a30
			d3t3=pd3a30
			d4t3=pd4a30
		elif (a3[j]=='1'):
			d1t3=pd1a31
			d2t3=pd2a31
			d3t3=pd3a31
			d4t3=pd4a31
		else:
			d1t3=pd1a32
			d2t3=pd2a32
			d3t3=pd3a32
			d4t3=pd4a32	
		if (a4[j]=='0'):
			d1t4=pd1a40
			d2t4=pd2a40
			d3t4=pd3a40
			d4t4=pd4a40
		elif (a4[j]=='1'):
			d1t4=pd1a41
			d2t4=pd2a41
			d3t4=pd3a41
			d4t4=pd4a41
		else:
			d1t4=pd1a42
			d2t4=pd2a42
			d3t4=pd3a42
			d4t4=pd4a42
		if (a5[i]=='0'):
			d1t5=pd1a50
			d2t5=pd2a50
			d3t5=pd3a50
			d4t5=pd4a50
		else:
			d1t5=pd1a51
			d2t5=pd2a51
			d3t5=pd3a51
			d4t5=pd4a51	
		if (a6[j]=='0'):
			d1t6=pd1a60
			d2t6=pd2a60
			d3t6=pd3a60
			d4t6=pd4a60
		elif (a6[j]=='1'):
			d1t6=pd1a61
			d2t6=pd2a61
			d3t6=pd3a61
			d4t6=pd4a61	
		elif (a6[j]=='2'):
			d1t6=pd1a62
			d2t6=pd2a62
			d3t6=pd3a62
			d4t6=pd4a62
		else:
			d1t6=pd1a63
			d2t6=pd2a63
			d3t6=pd3a63
			d4t6=pd4a63
		if (a7[j]=='0'):
			d1t7=pd1a70
			d2t7=pd2a70
			d3t7=pd3a70
			d4t7=pd4a70
		elif (a7[j]=='1'):
			d1t7=pd1a71
			d2t7=pd2a71
			d3t7=pd3a71
			d4t7=pd4a71	
		elif (a7[j]=='2'):
			d1t7=pd1a72
			d2t7=pd2a72
			d3t7=pd3a72
			d4t7=pd4a72
		else:
			d1t7=pd1a73
			d2t7=pd2a73
			d3t7=pd3a73
			d4t7=pd4a73
		if (a8[i]=='0'):
			d1t8=pd1a80
			d2t8=pd2a80
			d3t8=pd3a80
			d4t8=pd4a80
		else:
			d1t8=pd1a81
			d2t8=pd2a81
			d3t8=pd3a81
			d4t8=pd4a81
		if (a9[i]=='0'):
			d1t9=pd1a90
			d2t9=pd2a90
			d3t9=pd3a90
			d4t9=pd4a90
		else:
			d1t9=pd1a91
			d2t9=pd2a91
			d3t9=pd3a91
			d4t9=pd4a91
		if (a10[j]=='0'):
			d1t10=pd1a100
			d2t10=pd2a100
			d3t10=pd3a100
			d4t10=pd4a100
		elif (a3[j]=='1'):
			d1t10=pd1a101
			d2t10=pd2a101
			d3t10=pd3a101
			d4t10=pd4a101
		else:
			d1t10=pd1a102
			d2t10=pd2a102
			d3t10=pd3a102
			d4t10=pd4a102
		d1t11=pd1a111
		d2t11=pd2a111
		d3t11=pd3a111
		d4t11=pd4a111
		if (a12[i]=='0'):
			d1t12=pd1a120
			d2t12=pd2a120
			d3t12=pd3a120
			d4t12=pd4a120
		else:
			d1t12=pd1a121
			d2t12=pd2a121
			d3t12=pd3a121
			d4t12=pd4a121
		d1t13=pd1a130
		d2t13=pd2a130
		d3t13=pd3a130
		d4t13=pd4a130
		d1t14=pd1a142
		d2t14=pd2a142
		d3t14=pd3a142
		d4t14=pd4a142
		d1t15=pd1a152
		d2t15=pd2a152
		d3t15=pd3a152
		d4t15=pd4a152
		d1t16=pd1a160
		d2t16=pd2a160
		d3t16=pd3a160
		d4t16=pd4a160
		d1t17=pd1a170
		d2t17=pd2a170
		d3t17=pd3a170
		d4t17=pd4a170
		d1t18=pd1a180
		d2t18=pd2a180
		d3t18=pd3a180
		d4t18=pd4a180
		d1t19=pd1a191
		d2t19=pd2a191
		d3t19=pd3a191
		d4t19=pd4a191
		if (a20[i]=='0'):
			d1t20=pd1a200
			d2t20=pd2a200
			d3t20=pd3a200
			d4t20=pd4a200
		else:
			d1t20=pd1a201
			d2t20=pd2a201
			d3t20=pd3a201
			d4t20=pd4a201
		if (a21[j]=='0'):
			d1t21=pd1a210
			d2t21=pd2a210
			d3t21=pd3a210
			d4t21=pd4a210
		elif (a21[j]=='1'):
			d1t21=pd1a211
			d2t21=pd2a211
			d3t21=pd3a211
			d4t21=pd4a211	
		elif (a21[j]=='2'):
			d1t21=pd1a212
			d2t21=pd2a212
			d3t21=pd3a212
			d4t21=pd4a212
		else:
			d1t21=pd1a213
			d2t21=pd2a213
			d3t21=pd3a213
			d4t21=pd4a213
		if (a22[j]=='0'):
			d1t22=pd1a220
			d2t22=pd2a220
			d3t22=pd3a220
			d4t22=pd4a220
		elif (a22[j]=='1'):
			d1t22=pd1a221
			d2t22=pd2a221
			d3t22=pd3a221
			d4t22=pd4a221	
		elif (a22[j]=='2'):
			d1t22=pd1a222
			d2t22=pd2a222
			d3t22=pd3a222
			d4t22=pd4a222
		else:
			d1t22=pd1a223
			d2t22=pd2a223
			d3t22=pd3a223
			d4t22=pd4a223	
		if (a23[i]=='0'):
			d1t23=pd1a230
			d2t23=pd2a230
			d3t23=pd3a230
			d4t23=pd4a230
		else:
			d1t23=pd1a231
			d2t23=pd2a231
			d3t23=pd3a231
			d4t23=pd4a231	
		if (a24[i]=='0'):
			d1t24=pd1a240
			d2t24=pd2a240
			d3t24=pd3a240
			d4t24=pd4a240
		else:
			d1t24=pd1a241
			d2t24=pd2a241
			d3t24=pd3a241
			d4t24=pd4a241	
		if (a25[i]=='0'):
			d1t25=pd1a250
			d2t25=pd2a250
			d3t25=pd3a250
			d4t25=pd4a250
		else:
			d1t25=pd1a2518			
			d2t25=pd2a251
			d3t25=p33a251
			d4t25=p34a251	
		if (a26[i]=='0'):
			d1t26=pd1a260
			d2t26=pd2a260
			d3t26=pd3a260
			d4t26=pd4a260
		else:
			d1t26=pd1a262
			d2t26=pd2a262
			d3t26=pd3a262
			d4t26=pd4a262	
		if (a27[i]=='0'):
			d1t27=pd1a270
			d2t27=pd2a270
			d3t27=pd3a270
			d4t27=pd4a270
		else:
			d1t27=pd1a271
			d2t27=pd2a271
			d3t27=pd3a271
			d4t27=pd4a271
		if (a28[i]=='0'):
			d1t28=pd1a280
			d2t28=pd2a280
			d3t28=pd3a280
			d4t28=pd4a280
		else:
			d1t28=pd1a283
			d2t28=pd2a283
			d3t28=pd3a283
			d4t28=pd4a283	
		d1t29=pd1a294
		d2t29=pd2a294
		d3t29=pd3a294
		d4t29=pd4a294
		d1t30=pd1a300
		d2t30=pd2a300
		d3t30=pd3a300
		d4t30=pd4a300
		d1t31=pd1a310
		d2t31=pd2a310
		d3t31=pd3a310
		d4t31=pd4a310
		d1t32=pd1a320
		d2t32=pd2a320
		d3t32=pd3a320
		d4t32=pd4a320
		d1t33=pd1a330
		d2t33=pd2a330
		d3t33=pd3a330
		d4t33=pd4a330
		d1t34=pd1a340
		d2t34=pd2a340
		d3t34=pd3a340
		d4t34=pd4a340
		if (a35[i]=='0'):
			d1t35=pd1a350
			d2t35=pd2a350
			d3t35=pd3a350
			d4t35=pd4a350
		else:
			d1t35=pd1a351
			d2t35=pd2a351
			d3t35=pd3a351
			d4t35=pd4a351
		prpd1=pd1*d1t1*d1t2*d1t3*d1t4*d1t5*d1t6*d1t7*d1t8*d1t9*d1t10*d1t11*d1t12*d1t13*d1t14*d1t15*d1t16*d1t17*d1t18*d1t19*d1t20*d1t21*d1t22*d1t23*d1t24*d1t25*d1t26*d1t27*d1t28*d1t29*d1t30*d1t31*d1t32*d1t33*d1t34*d1t35
		prpd2=pd2*d2t1*d2t2*d2t3*d2t4*d2t5*d2t6*d2t7*d2t8*d2t9*d2t10*d2t11*d2t12*d2t13*d2t14*d2t15*d2t16*d2t17*d2t18*d2t19*d2t20*d2t21*d2t22*d2t23*d2t24*d2t25*d2t26*d2t27*d2t28*d2t29*d2t30*d2t31*d2t32*d2t33*d2t34*d2t35
		prpd3=pd3*d3t1*d3t2*d3t3*d3t4*d3t5*d3t6*d3t7*d3t8*d3t9*d3t10*d3t11*d3t12*d3t13*d3t14*d3t15*d3t16*d3t17*d3t18*d3t19*d3t20*d3t21*d3t22*d3t23*d3t24*d3t25*d3t26*d3t27*d3t28*d3t29*d3t30*d3t31*d3t32*d3t33*d3t34*d3t35
		prpd4=pd4*d4t1*d4t2*d4t3*d4t4*d4t5*d4t6*d4t7*d4t8*d4t9*d4t10*d4t11*d4t12*d4t13*d4t14*d4t15*d4t16*d4t17*d4t18*d4t19*d4t20*d4t21*d4t22*d4t23*d4t24*d4t25*d4t26*d4t27*d4t28*d4t29*d4t30*d4t31*d4t32*d4t33*d4t34*d4t35
		if (prpd1>prpd2):
			if (prpd1>prpd3):
				if (prpd1>prpd4):
					if (cl[j]=='D1'):
						acc+=1
				else:
					if (cl[j]=='D4'):
						acc+=1
			else:
				if (prpd3>prpd4):
					if (cl[j]=='D3'):
						acc+=1
				else:
					if (cl[j]=='D4'):
						acc+=1
		else:
			if (prpd2>prpd3):
				if (prpd2>prpd4):
					if (cl[j]=='D2'):
						acc+=1
				else:
					if (cl[j]=='D4'):
						acc+=1
			else:
				if (prpd3>prpd4):
					if (cl[j]=='D3'):
						acc+=1
				else:
					if (cl[j]=='D4'):
						acc+=1
	print(acc)						
	act=(acc/47)*100
	print(act)