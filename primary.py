def chartFromNothing():
	import dataGather
	bitcoinName = "XBTC"
	currency = "GBP"
	amount = "40"
	time="1"#time in days
	import json
	#data = json.loads(dataGather.get(bitcoinName,currency,amount,time))
	data = json.load(open("historicalBitcoinData.json"))
	import cleaner
	cleanedData = cleaner.use(data)
	print(cleanedData)
	import prediction
	expectation = prediction.flux(data)
	import chartMaker
	#chart = chartMaker.makeChart(data, expectation)
	chart = chartMaker.makeChart(cleanedData)
	#Do something to print the chart
	#FANCY IOS MAGIC GOES HERE
if __name__ == "__main__":
	chartFromNothing()
