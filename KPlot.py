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

class frame:
	def init(self):
		self.clear(verbose = False)
	def clear(self , verbose = True):
		if verbose: print "ClearingFrame"
		self.inputFile = None
		self.note = ""
		self.cols = [] # list 
		self.rows = []
		self.data = {}
		self.pointSpecPoints = []
		self.methods = {}
		self.nonNumerics = False
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
		firstRow = piviot[0] + (1 if colNames else 0)
		firstCol = piviot[1] + (1 if rowNames else 0)
		lastRow = lastRow if lastRow else len(raw)
		lastCol = lastCol if lastCol else len(raw[piviot[0]])
		self.rows = [raw[n][piviot[1]] for n in range(piviot[0]+1,lastRow)] if rowNames else range(0,(len(raw)-piviot[0]))
		self.cols = raw[piviot[0]][piviot[1]+1:] if colNames else range(0,len(raw[piviot[0]])-piviot[1])
		self.data = {}
		for n,k in enumerate(range(firstRow,lastRow)):
			try:
				self.data[self.rows[n]] = {}
				for n2,k2 in enumerate(range(firstCol,lastCol)):
					try:
						self.data[self.rows[n]][self.cols[n2]] = float(raw[k][k2])
					except ValueError:
						print "Cell["+str(n)+":"+str(k)+"]["+str(n2)+":"+str(k2)+"]"+" contains a non-numeric value ="+str(raw[k][k2])
						if(raw[k][k2] in ["None","","nan"]):
							self.data[self.rows[n]][self.cols[n2]] = None
						else:	
							self.data[self.rows[n]][self.cols[n2]] = raw[k][k2]
						self.nonNumerics = True
			except IndexError:
				try:
					del self.data[self.rows[n]]
				except IndexError:
					temp = "salty"
				self.rows = self.rows[:len(self.data)]
				print "an index error occured -\\_('_')_/- \n this may be the end of your file at "+("row" if rowNames else "line")+" "+str(n)+"\n!  @  "+target+"  @  !"
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
	def csv():
		print("Todo")

def testIO():
	kframe = frame()
	kframe.addNote("Test Driven development makes for higher quality, more usable products.")
	kframe.loadFromCsv("./testData/basicTestData.csv")
	print(kframe.pretty())
	kframe.clear()
	kframe.loadFromCsv("./testData/basicTestData.csv",rowNames=True, colNames=True)
	print(kframe.pretty())
#testIO()



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
	print("placeHolder")




def hexidecimalDiget(n,deHex = False):
	if(n<0):
		print "negitive values not supported by call to hexidecimalDiget("+str(n)+")"
		return None
	elif(n < 10):
		return str(n)
	elif(n < 15):
		return ["a","b","c","d","e","f"][n-10]
	elif(n in ["a","b","c","d","e","f"]):
		if deHex:
			return ["a","b","c","d","e","f"].index(n)
		return n
	else:
		print "call to hexidecimalDiget("+str(n)+") not supported!"
		return None

def colorFormHexArray(arr):
	if len(arr)!=3 and len(arr)!=6:
		print "invalid length for color on call to colorFormHexArray("+str(arr)+")"
		return None
	elif None in arr:
		print "cannot make color from None arguments in "+str(arr)
		return None
	else:
		ret = "#"
		for k in arr:
			if(type(k) == list):
				for k2 in k:
					ret+=hexidecimalDiget(k)
			else:
				ret+=hexidecimalDiget(k)
		return ret

def arrayFromColor(c):
	c = c.replace("#","")
	col = []
	for n,k in enumerate(c):
		if(len(c) == 3):
			col.append([hexidecimalDiget(k,deHex = True)])
		elif(len(c) == 6):
			col.append([hexidecimalDiget(c[(n+1)*2-2],deHex = True),hexidecimalDiget(c[(n+1)*2-2],deHex = True)])
	return(col)

def intFromHexPair(hp):
	ret = 0
	for n,k in enumerate(hp):
		digBase = 16**(len(hp)-n-1)
		ret+=digBase*hexidecimalDiget(hp[0],deHex = True)
	return ret

def hexPairFromInt(I,minDigits = 1,maxDigits = 256):
	if I<0:
		print "negitive numbers not supported by hexPairFromInt"
	k= 0
	while(16**(k+1) <= I):
		k+=1
	if k < minDigits:
		k = minDigits
	if k > minDigits:
		print("maxDigitsExceeded")
	ret = []
	while k>=0:
		dig = 16**k
		ret.append(hexidecimalDiget(int(I)%(dig)))
		I-=dig
		k-=1
	return ret

def specColor(start,end,bottom,top):
	start = arrayFromColor(start)
	end = arrayFromColor(end)
	def ret(v):
		if( v<start or c>end ):
			print("value out of range "+str([start,end]))
			return('#aa0000') #eyo <- error red
		else:
			starts = [intFromHexPair(k) for k in start]
			ends = [intFromHexPair(hp) for k in end]
			normalized = (v-bottom)/(top-bottom)
			return colorFormHexArray([hexPairFromInt(int((starts[n]-ends[n])*normalized),minDigits = 1,maxDigits = 256) for n,k in enumerate(starts)])
	return ret

def testColors(): #Todo
	test1 = specColor('#000000','#eeeeee',0,500)
	

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
	

import os
import warnings

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

def ex1():
	a = range(0,20)
	b = [k/10. for k in a]
	c,d = investOnRatios(b,10.,1.)
	e =[k*10 for k in range(8,12)]
	mlSurf(c,"basic","% Return","Investment","Gross",xticks=[k*10 for k in a],yticks=d)
#ex1()

def ex2():
	a = range(80,110)
	b = [k/100. for k in a]
	c,d = investOnRatios(b,10.,1.)
	e =[k*10 for k in range(8,12)]
	mlSurf(c,"basic","% Return","Investment","Gross",xticks=a,yticks=d)
#ex2()

def ex3():
	a = range(99,102)
	b = [k/100. for k in a]
	c,d = investOnRatios(b,10.,1.)
	e =[k*10 for k in range(8,12)]
	mlSurf(c,"basic","% Return","Investment","Gross",xticks=a,yticks=d)
#ex3()



def cap():
	a = range(-10,10)
	cpc = 2
	ret = []
	r =[k/10. for k in range(0,10)]
	for k in r:
		ret.append([(1.5**k2)*k-cpc*k2 for k2 in a])
	mlSurf(ret,"cvsp","Complexity","Time Invested","Productivity",xticks=a,yticks=r)
#cap()

import make as kl #klearner
import geoTools as gt  #back and for for longitude latitude to XYZ tools

def geoKlTest():
	f = frame()
	f.loadFromCsv("./testData/geoTestData.csv",rowNames=True, colNames=True)
	arr = f.toArray()
	print f.pretty()
	for n,k in enumerate(f.rows):
		for n2,k2 in enumerate(f.cols):
			if(arr[n][n2] == None):
				print(k+":"+k2+":"+str(round(kl.kfp(arr,n,n2),2)))
	xyz = gt.cordToEuc(arr[0][0],arr[0][1])
	print arr[0][0],arr[0][1],xyz
	euc = gt.eucToCord(xyz[0],xyz[1],xyz[2])
	print xyz,euc
geoKlTest()










