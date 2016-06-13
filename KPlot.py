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
testFont()

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
		out = "File:\t"+self.inputFile+"\n"
		out += "Note:\t"+self.note+"\n"
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

def testIO():
	kframe = frame()
	kframe.addNote("Test Driven development makes for higher quality, more usable products.")
	kframe.loadFromCsv("testData.csv")
	print(kframe.pretty())
	kframe.clear()
	kframe.loadFromCsv("testData.csv",rowNames=True, colNames=True)
	print(kframe.pretty())
testIO()



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
