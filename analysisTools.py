import mdp

def pca(data, singleValueDecomp=True):
	return(mdp.pca(data,svd=singleValueDecomp))

def ica(data, precision = 'float32'):
	return(mdp.fastica(data, dtype=precision))

def BiSec(v, method = "mean"):
	if(method == "mean"):
		avg = sum(v)/float(len(v))
	if(method == "median"):
		avg = sum(sorted(v)[len(v)/2-1:len(v)/2+1 if len(v)%2 == 0 else len(v)/2:len(v)/2+1])
	if(method == "middle"):
		avg = min(v)+(max(v)-min(v))/2.
	return([1 if k>avg else 0 for k in v])

def cov(a,b,defaulValue = 0):
	aNeeds = set(b.keys()).difference(set(a.keys()))
	bNeeds = set(a.keys()).difference(set(b.keys()))
	for k in aNeeds:
		a[k] = defaultValue
	for k in bNeeds:
		b[k] = defaultValue
	keys = a.keys()
	meanA = sum([a[k] for k in keys])/float(len(keys))
	meanB = sum([b[k] for k in keys])/float(len(keys))
	ret = 0
	for k in keys:
		ret+= (a[k]-meanA)*(b[k]-meanB)
	ret/=float(len(keys))
	return(ret)

def sigma(a):
	keys = a.keys()
	meanA = sum([a[k] for k in keys])/float(len(keys))
	ret=0
	for k in keys:
		ret +=(a[k]-meanA)**2
	ret/=len(keys)
	ret**=0.5
	return(ret)

def correlation(a,b,defaulValue = 0):
	aNeeds = set(b.keys()).difference(set(a.keys()))
	bNeeds = set(a.keys()).difference(set(b.keys()))
	for k in aNeeds:
		a[k] = defaultValue
	for k in bNeeds:
		b[k] = defaultValue
	cov(a,b)/(sigma(a)*sigma(b))

def magnitude(a):
	ret =0
	for k in a:
		ret+=a[k]**2
	return ret**0.5

def dot(a,b):
	aNeeds = set(b.keys()).difference(set(a.keys()))
	bNeeds = set(a.keys()).difference(set(b.keys()))
	for k in aNeeds:
		a[k] = defaultValue
	for k in bNeeds:
		b[k] = defaultValue
	keys = a.keys()
	ret=0
	for k in keys:
		ret+=a[k]*b[k]
	return(ret)

def cos(a,b):
	return(dot(a,b)/(magnitude(a)*magnitude(b)))	

