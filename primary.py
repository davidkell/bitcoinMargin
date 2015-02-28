def chartFromNothing():
	import dataGather
	bitcoinName = "XBTC"
	currency = "GBP"
	amount = "40"
	time="1"#time in days
	data = dataGather.get(bitcoinName,currency,amount,time)
	import prediction
	expectation = prediction.flux(data)
	import chartMaker
	chart = chartMaker.makeChart(data, expectation)
	#Do something to print the chart
	#FANCY IOS MAGIC GOES HERE
if __name__ = "__main__":
	chartFromNothing()
