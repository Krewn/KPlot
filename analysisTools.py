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
	return([1 if k>avg else 0 for k in v])


