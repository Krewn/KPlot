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
	
