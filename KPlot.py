# coding: utf-8
"""
 __  _  ____   ___   _     ______ 
|  |/ ]|    \ /   \ | |   |      |<- krewn.github.io/KPlot
|  ' / |  o  )     || |   |      |
|    \ |   _/|  O  || |___|_|  |_|
|     ||  |  |     ||     | |  |  
|  .  ||  |  |     ||     | |  |  
|__|\_||__|   \___/ |_____| |__|  Kevin Nelson -> kpie314@gmail.com
                                  
"""



def paddedPrint(s,l):
    if(type(s) == float):
        s = round(s,3)
    return(str(s)+(" "*(l-len(str(s))) if len(str(s))<= l else "#"))

def redPrint(s,l):
    if(type(s) == float):
        s = round(s,3)
    CSI="\x1B["
    return(CSI+"31;40m" + str(s) + CSI + "0m"+(" "*(l-len(str(s))) if len(str(s))<= l else "#"))

def where(vector,condition):
	return([n for n,k in enumerate(vector) if eval(condition)])

import xlrd
import csv
def sheetAsArray(name,index,opFile):
	with xlrd.open_workbook(name) as wb:
	    sh = wb.sheet_by_index(index)  # or wb.sheet_by_name('name_of_the_sheet_here')
	    with open(opFile, 'wb') as f:
		ret = ""
		for r in range(sh.nrows):
			for k in unicode(sh.row_values(r)):
				ret+=c.writerow(k)+","
			ret = ret[:-1]
			ret+="\n"
		ret = ret[:-1]
		f.write(ret)

import os
def explode(inputFile):
	try:
		os.mkdir(inputFile+".folder")
	except OSError:
		chill = None
	with xlrd.open_workbook(inputFile) as wb:
		for k in range(0,wb.nsheets):
			sh = wb.sheet_by_index(k) # or wb.sheet_by_name('name_of_the_sheet_here')
			with open(inputFile+".folder"+"/sheet"+str(k)+".csv", 'wb') as f:
				ret = ""
				for r in range(sh.nrows):
					for col in sh.row_values(r):
						try:
							ret+=str(col)+","
						except UnicodeEncodeError:
							ret+=","
					ret = ret[:-1]
					ret+="\n"
				ret = ret[:-1]
				f.write(ret)


class frame:
	inputFile = None
	note = ""
	cols = []
	rows = []
	data = {}
	pointSpecPoints = []
	methods = {}
	nonNumerics = False
	def init(self):
		self.clear(verbose = False)
	def clear(self , verbose = True):
		if verbose: print "ClearingFrame"
		self.inputFile = None
		self.note = ""
		self.cols = []
		self.rows = []
		self.data = {}
		self.pointSpecPoints = []
		self.methods = {}
		self.nonNumerics = False
	def getRows(self):
		return(self.rows)
	def getCols(self): 
		return(self.cols)
	def add(self, row,column,value=None):
		if not(row in self.rows):
			self.rows.append(row)
			self.data[row] = {}
		if not(column in self.cols):
			self.cols.append(column)
		self.data[row][column] = value
	def add2dDict(self,d):
		for k in d:
			for k2 in d[k]:
				self.add(k,k2,d[k][k2])
	def getRow(self,r):
		return [self.data[r][k] for k in self.cols]
	def getCol(self,c):
		return [self.data[k][c] for k in self.rows]
	def toArray(self,headers = False):
		ret = []
		for n,k in enumerate(self.rows):
			ret.append([])
			for k2 in self.cols:
				ret[n].append(self.data[k][k2])
		if headers:
			return(ret,self.rows,self.cols)
		return(ret)
	def flat(self):
		for k in self.rows:
			for k in self.cols:
				ret.append((self.data[k][k2],(k,k2)))
	def deSelectColumns(self):
		self.colSelector = [False]*len(columns)
	def selectColumns(self):
		self.colSelector = [True]*len(columns)
	def deSelectRows(self):
		self.rowSelector = [False]*len(columns)
	def selectRows(self):
		self.rowSelector = [True]*len(columns)
	def toggleRow(self,n):
		if(type(n)==int):
			self.rowSelector[n] = False if self.rowSelector[n] else True
		else:
			for k in where(this.rows,"k == "+str(n)):
				self.rowSelector[k] = False if self.rowSelector[k] else True
	def toggleCol(self,n):
		if(type(n)==int):
			self.colSelector[n] = False if self.colSelector[n] else True
		else:
			for k in where(this.rows,"k == "+str(n)):
				self.colSelector[k] = False if self.colSelector[k] else True
	def selectMethod(self,m):
		if( (m in self.Methods) == False):
			print(m+" is not a method")
		else:
			self.methods[m] = False if self.rowSelector[k] else True
	def addValue(row,col,val):
		if(not (r in rows)):
			self.rows.append(r)
			self.data[row]={}
		self.data[row][col] = val
	def loadFromCsv(self, target, rowNames=False, colNames=False, piviot=[0,0], rowDelim="\n", colDelim=",", lastRow=False, lastCol=False):
		self.inputFile = target
		o = open(target)
		raw = [k.split(colDelim) for k in o.read().split(rowDelim)]
		if len(raw[len(raw)-1])==1 and raw[len(raw)-1] == "":
			raw = raw[:len(raw)-1]
		#print len(raw)
		firstRow = piviot[0] + (1 if colNames else 0)
		firstCol = piviot[1] + (1 if rowNames else 0)
		lastRow = lastRow if lastRow else len(raw)
		lastCol = lastCol if lastCol else len(raw[piviot[0]])
		self.rows = [raw[n][piviot[1]] for n in range(piviot[0]+1,lastRow)] if rowNames else range(0,(len(raw)-piviot[0]))
		self.cols = raw[piviot[0]][piviot[1]+1:] if colNames else range(0,len(raw[piviot[0]])-piviot[1])
		#print self.rows
		self.data = {}
		TotalRows = lastRow - firstRow
		for n,k in enumerate(range(firstRow,lastRow+(1 if (colNames == True and rowNames == False) else 0))):
			#print str(n)+"/"+str(TotalRows) ,"\r",
			if colNames == True and rowNames == False:
				self.data[self.rows[n]] = {k:v for k,v in zip(self.cols,raw[n][piviot[1]+1:])}
			else:
				try:
					self.data[self.rows[n]] = {}
					for n2,k2 in enumerate(range(firstCol,lastCol)):
						try:
							self.data[self.rows[n]][self.cols[n2]] = float(raw[k][k2])
						except ValueError:
							#print "Cell["+str(n)+":"+str(k)+"]["+str(n2)+":"+str(k2)+"]"+" contains a non-numeric value ="+str(raw[k][k2])
							if(raw[k][k2] in ["None","","nan"]):
								self.data[self.rows[n]][self.cols[n2]] = None
							else:	
								self.data[self.rows[n]][self.cols[n2]] = raw[k][k2]
							self.nonNumerics = True
						#print self.data[self.rows[n]][self.cols[n2]]
				except IndexError:
					try:
						del self.data[self.rows[n]]
					except IndexError:
						temp = "salty"
					self.rows = self.rows[:len(self.data)]
					#print "an index error occured -\\_('_')_/- \n this may be the end of your file at "+("row" if rowNames else "line")+" "+str(n)+"\n!  @  "+target+"  @  !"
					#print target
	def addNote(self, n):		
		try:
			temp = self.note
		except AttributeError:
			self.note = ""
		self.note = ("\n" if len(self.note) > 0 else "")+n
	def pretty(self):
		out = ""
		out += "File:\t"+self.inputFile+"\n" if self.inputFile!=None else ""
		if hasattr(self, "note"):
			out += "Note:\t"+self.note +"\n"
		out+=paddedPrint("",15)
		for k in self.cols:
		    out+=paddedPrint(k,15)
		for k in self.rows:
		    out+="\n"+paddedPrint(k,15)
		    for k2 in self.cols:
			try:
		        	out+=paddedPrint(str(self.data[k][k2]),15)
			except KeyError:
				out+=redPrint(str(""),15)
		return("\n\n"+out+"\n\n")
	def csv(self, rowdelim = "\n", coldelim = "\t"):
		top = ""
		if len(self.rows) > 0:
			top+=coldelim
		for k in self.rows:
			top+=str(k)+coldelim
		if len(self.cols) > 0:
			top = top[:-len(coldelim)]
		if len(top)>0:
			top+="\n"
		body = ""
		for k in self.rows:
			body+=str(k)+coldelim
			for k2 in self.cols:
				try:
					body+=str(self.data[k2][k])+coldelim
				except KeyError:
					body+=coldelim
			top = top[:-len(coldelim)]
			body+=rowdelim
		return(top+body)

def testCSV():
	kframe = frame()
	kframe.addNote("Test Driven development makes for higher quality, more usable products.")
	kframe.loadFromCsv("./testData/basicTestData.csv")
	print(kframe.pretty())
	kframe.clear()
	kframe.loadFromCsv("./testData/basicTestData.csv",rowNames=True, colNames=True)
	print(kframe.pretty())

#testCSV()
import make as kl #klearner
def klTest():
	f = frame()
	f.loadFromCsv("./testData/geoTestData.csv",rowNames=True, colNames=True)
	arr = f.toArray()
	print f.pretty()
	for n,k in enumerate(f.rows):
		for n2,k2 in enumerate(f.cols):
			if(arr[n][n2] == None):
				print(k+":"+k2+":"+str(round(kl.kfp(arr,n,n2),2)))
#klTest()
import geoTools as gt  #back and for for longitude latitude to XYZ tools
def geoTest():
	f = frame()
	f.loadFromCsv("./testData/geoTestData.csv",rowNames=True, colNames=True)
	arr = f.toArray()
	xyz = gt.cordToEuc(arr[0][0],arr[0][1])
	print arr[0][0],arr[0][1],xyz
	euc = gt.eucToCord(xyz[0],xyz[1],xyz[2])
	print xyz,euc
#geoTest()

import analysisTools as at
# TODO write tests and more clustering methods.

import Image, ImageDraw
#Characters are fixed font drawn on a 2x4 grid where y = 3 is the text line bottm.
characters = {'1':[[(0,1),(1,0),(1,3)],[(0,3),(2,3)]],'2':[[(0,1),(1,0),(2,1),(0,3),(2,3)]],'3':[[(0,1),(1,0),(2,1),(1,1.5),(2,2),(1,3),(0,2)]],'4':[[(0,0),(0,1.5),(2,1.5)],[(2,0),(2,3)]],'5':[[(2,0),(0,0),(0,1,),(1,1),(2,1.75),(2,2.25),(1,3),(0,3)]],'6':[[(1,0),(0,1),(0,3),(2,3),(2,2),(0,2)]],'7':[[(0,0),(2,0),(1,3)]],'8':[[(0,0),(2,0),(2,1),(1.5,1.5),(2,2.5),(2,3),(0,3),(0,2),(0.5,1.5),(0,0.5),(0,0)],[(0.5,1.5),(1.5,1.5)]],'9':[[(0,3),(2,2),(2,0),(0,0),(0,1),(2,1)]],'0':[[(0,0),(0,3),(2,3),(2,0),(0,0),(2,3)]],'a':[[(1.5,3),(1.5,1),(0,1),(0,3),(1.5,3),(2,3)]],'b':[[(0,0),(0,3),(2,3),(2,2),(0,2)]],'c':[[(2,1),(1,1),(0,1.5),(0,2.5),(1,3),(2,3)]],'d':[[(2,0),(2,3),(0,3),(0,2),(2,2)]],'e':[[(2,3),(0,3),(0,1),(2,1),(2,2),(0,2)]],'f':[[(1,3),(1,0),(2,0)],[(0,1.5),(2,1.5)]],'g':[[(2,3),(0,3),(0,1),(2,1),(2,4),(1,4)]],'h':[[(0,3),(0,0)],[(0,2),(2,2),(2,3)]],'i':[[(1,3),(1,1.5)],[(0.75,1.25),(1.25,0.75)]],'j':[[(0,4),(1,4),(1,1.5)],[(0.75,1.25),(1.25,0.75)]],'k':[[(0,3),(0,0)],[(0,2),(1,1)],[(0,2),(2,3)]],'l':[[(1,3),(1,0)]],'m':[[(0,3),(0,1),(2,1),(2,3)],[(1,1),(1,3)]],'n':[[(0,3),(0,1),(2,1),(2,3)]],'o':[[(0,1),(2,1),(2,3),(0,3),(0,1)]],'p':[[(0,4),(0,1),(2,1),(2,3),(0,3)]],'q':[[(2,4),(2,1),(0,1),(0,3),(2,3)]],'r':[[(0,3),(0,1)],[(0,1.5),(1,1),(2,1)]],'s':[[(2,1),(0,1),(0,2),(2,2),(2,3),(0,3),]],'t':[[(1,0),(1,3)],[(0,1.5),(2,1.5)]],'u':[[(0,1),(0,3),(2,3),(2,1)]],'v':[[(0,1),(1,3),(2,1)]],'w':[[(0,1),(0,3),(1,2),(2,3),(2,1)]],'x':[[(0,1),(2,3)],[(0,3),(2,1)]],'y':[[(0,1),(0,3),(2,3)],[(2,1),(2,4),(1,4)]],'z':[[(0,1),(2,1),(0,3),(2,3)]],'A':[[(0,3),(1,0),(2,3)],[(0,1.5),(2,1.5)]],'B':[[(0,3),(0,0),(1.5,0),(1.5,1.5)],[(0,3),(2,3),(2,1.5),(0,1.5)]],'C':[[(2,0),(0,0),(0,3),(2,3)]],'D':[[(0,0),(0,3),(1.5,3),(2,2.5),(2,0.5),(1.5,0),(0,0)]],'E':[[(2,0),(0,0),(0,3),(2,3)],[(0,1.5),(1,1.5)]],'F':[[(0,3),(0,0),(2,0)],[(0,1.5),(1,1.5)]],'G':[[(2,0.5),(2,0),(0,0),(0,3),(2,3),(2,1.5),(1,1.5)]],'H':[[(0,0),(0,3)],[(0,1.5),(2,1.5)],[(2,0),(2,3)]],'I':[[(0,0),(2,0)],[(1,0),(1,3)],[(0,3),(2,3)]],'J':[[(0,0),(2,0)],[(1,0),(1,3),(0,2)]],'K':[[(0,0),(0,3)],[(2,0),(0,1.5),(2,3)]],'L':[[(0,0),(0,3),(2,3)]],'M':[[(0,3),(0,0),(1,1),(2,0),(2,3)]],'N':[[(0,3),(0,0),(2,3),(2,0)]],'O':[[(0,0),(0,3),(2,3),(2,0),(0,0)]],'P':[[(0,3),(0,0),(2,0),(2,1.5),(0,1.5)]],'Q':[[(2,3),(2,0),(0,0),(0,3),(2,3),(1,2)]],'R':[[(0,3),(0,0),(2,0),(2,1),(0,1.5),(2,3)]],'S':[[(2,0),(0,0),(0,1),(2,2),(2,3),(0,3)]],'T':[[(0,0),(2,0)],[(1,3),(1,0)]],'U':[[(0,0),(0,3),(2,3),(2,0)]],'V':[[(0,0),(1,3),(2,0)]],'W':[[(0,0),(0,3),(1,2),(2,3),(2,0)]],'X':[[(0,0),(2,3)],[(0,3),(2,0)]],'Y':[[(0,0),(1,1),(2,0)],[(1,1),(1,3)]],'Z':[[(0,0),(2,0),(0,3),(2,3)]]}

def tupleSum(a,b):
	return tuple([sum(k) for k in zip(a,b)])

def scale(vector,scaler):
	return tuple([scaler*k for k in vector])

def drawLine(start, end, img, relativeLocation = (0,0) ,size = 1):
	draw = ImageDraw.Draw(img)
	draw.line( tupleSum(relativeLocation,scale(start,size))+tupleSum(relativeLocation,scale(end,size)), fill=128)
	del draw

def drawLetter(letter,scale,img,relativeLocation,size = 1):
	global characters
	try:
		lines = characters[letter]
	except IndexError:
		print letter+" is not supported: to add suport for this letter make an entery in the characters variable."
	for k in lines:
		for k2 in range(1,len(k)):
			drawLine(k[k2-1], k[k2], img, relativeLocation, size)

def drawText(text,img,relativeLocation,size = 1):
	step = size*3
	place = list(relativeLocation)
	for k in text:
		drawLetter(k, scale, img, place, size)
	 	place[0] += step

def testFont():
	im = Image.new("RGB", (900, 512), "white")
	numbers = "1234567890"
	lowerCase = "abcdefghijklmnopqrstuvwxyz"
	upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	drawText(upperCase,im,(5,5),15)
	drawText(lowerCase,im,(5,50),15)
	drawText(numbers,im,(5,100),15)
	im.show()
#testFont()
def get(data,key,defaultVaule = False):#defaultsFalse
	return(data[key] if key in data else defaultVaule)

class grapher():
	def __init__(self):
		self.clear()
	def clear(self, verbose = False):
		self.dataFrame = frame()
	def setFrame(f):
		self.dataFrame = f
	def setData(self,data):
		self.data = data
	def graph(self,args):
		xticks = get( args,"xticks" )
		yticks = get( args,"yticks" )
		xtickLables = get( args,"xtickLables",defaultVaule = True )
		ytickLables = get( args,"ytickLables",defaultVaule = True )
		graphType = get( args,"graphType",defaultVaule = "line" )
		outPut = get( args,"outPut" )
		plot = get( args,"plot",defaultVaule = self.data.keys() )
		by = get( args,"plot",defaultVaule = self.data.keys() )
		if(graphType == "bar"):
			print("placeHolder")
		elif(graphType == "line"):
			print("placeHolder")
		elif(graphType == "pie"):
			print("placeHolder")
		elif(graphType == "heatMap"):
			print("placeHolder")
	
def gifPlot(grapher,graphs):
	print("placeHolder") # Todo

def investOnRatios(ratio,investment,step):
	I = 0
	ret = []
	invs = []
	while(I<investment):
		temp = [I*k-I for k in ratio]
		ret.append(temp)
		invs.append(I)
		I+=step
	return(ret,invs)

def toMatLabArray(varName,arr):
	ret = varName+"="
	if type(arr) == list:
		ret +="["
		for k in arr:
			if type(k) == list:
				for k2 in k:
					ret+=str(k2)+","
				ret+=";"
			else:
				ret+=str(k)+","
		ret += "]"
	else:
		ret += str(arr)+";"
	return(ret)

def curlyList(l):
	return str([str(k) for k in l]).replace("[","{").replace("]","}")

def mlStepper(l):
	s = "["
	s+=str(min(l))+":"
	s+=str(float(max(l)-min(l))/float(len(l)))+":"
	s+=str(max(l))+"]"
	return(s)

def durp7(l):
	step = (float(max(l))-float(min(l)))/6.
	r = float(min(l))
	ret = [""]
	for k in range(0,7):
		ret.append(round(r,1))
		r+=step
	return(ret)

def boy(x,y,xname="xName",yname="yName"):
	return(toMatLabArray(xname,x),toMatLabArray(yname,y))

def mlSurf(arr,opFile,xlabel = "x", ylabel = "y" , title = "title", xticks = None , yticks = None):
	varstr = toMatLabArray("InvestmentReturns",arr)
	f = open(opFile+".m","w")
	graphstr = varstr+";\n"
	if xticks != None and yticks != None:
		xs,ys = boy(xticks,yticks)
		graphstr += xs+";\n"
		graphstr += ys+";\n"
		graphstr +="surf("+xs.split("=")[0]+","+ys.split("=")[0]+","+varstr.split("=")[0]+");\n"
	else:
		graphstr +="surf("+varstr.split("=")[0]+");\n"
	graphstr +='view(0,90); shading interp;colorbar;\n'
	graphstr +='xlabel("'+xlabel+'");ylabel("'+ylabel+'");\n'
	graphstr +='title("'+title+'");\n'
	graphstr +='axis("tight");\n'
	f.write(graphstr)
	f.close()
	f = open(opFile+".sh","w")
	f.write("octave --persist "+opFile+".m")
	f.close()
	os.system("chmod +x "+opFile+".sh")
	os.system("./"+opFile+".sh")

def mlSurfTest1():
	a = range(99,102)
	b = [k/100. for k in a]
	c,d = investOnRatios(b,10.,1.)
	e =[k*10 for k in range(8,12)]
	mlSurf(c,"basic","% Return","Investment","Gross",xticks=a,yticks=d)
#mlSurfTest1()

def  mlSurfTest2():
	a = range(-10,10)
	cpc = 2
	ret = []
	r =[k/10. for k in range(0,10)]
	for k in r:
		ret.append([(1.5**k2)*k-cpc*k2 for k2 in a])
	mlSurf(ret,"cvsp","Complexity","Time Invested","Productivity",xticks=a,yticks=r)
#mlSurfTest2()

def gridToPixles(tmin,tmax,ymin,ymax,w,h,t,y):
	retT = ((t-tmin)/(tmax-tmin))*w
	retY = ((ymax-y)/(ymax-ymin))*h
	return((retT,retY))





