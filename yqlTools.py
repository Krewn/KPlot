import urllib

def histoQuote(tag,startDate,endDate):
	filehandle = urllib.urlopen("https://query.yahooapis.com/v1/public/yql?q=SELECT%20*%20FROM%20yahoo.finance.historicaldata%20WHERE%20symbol%3D%22"+tag+"%22%20and%20startDate%3D%22"+startDate+"%22%20and%20endDate%3D%22"+endDate+"%22&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=")
	d = eval(filehandle.read())
	attrs = ['High','Volume','Low','Close','Symbol','Open','Adj_Close']
	ret = {}
	for k in d['query']['results']['quote']:
		ret[k['Date']] = {k2:k[k2] for k2 in atts}
	return(ret)
			

def ajoin(arr,delim):
	ret = ""
	for k in arr:
		ret+=str(k)+"%20"
	return(ret)

def quoteNow(tags):
	return("https://query.yahooapis.com/v1/public/yql?q=env%20'store%3A%2F%2Fdatatables.org%2Falltableswithkeys'%3B%20select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22"+ajoin(tags)+"%22)&format=json&diagnostics=true&callback=")

filehandle = urllib.urlopen("https://query.yahooapis.com/v1/public/yql?q=SELECT%20*%20FROM%20yahoo.finance.historicaldata%20WHERE%20symbol%3D%22fldm%22%20and%20startDate%3D%222014-09-11%22%20and%20endDate%3D%222015-09-11%22&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=")

filehandle2 = urllib.urlopen("https://query.yahooapis.com/v1/public/yql?q=env%20'store%3A%2F%2Fdatatables.org%2Falltableswithkeys'%3B%20select%20*%20from%20yahoo.finance.quotes%20where%20symbol%20in%20(%22YHOO%22%2C%22AAPL%22%2C%22GOOG%22%2C%22MSFT%22)&format=json&diagnostics=true&callback=")

d = eval(filehandle.read())

attrs = ['High','Volume','Low','Date','Close','Symbol','Open','Adj_Close']

print(d['query']['results']['quote'][0])
