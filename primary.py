def chartFromNothing():
	import dataGather
	import json
	#bitcoinName = "XBTC"
	#currency = "GBP"
	#amount = "40"
	time=1 #time in days
	#data = json.loads(dataGather.get(bitcoinName,currency,amount))
	data = json.load(open("historicalBitcoinData.json"))
	import cleaner
	cleanedData = cleaner.use(data)
	print(cleanedData)
	import prediction
	expectation = prediction.flux(data,time)
	import chartMaker
	#chart = chartMaker.makeChart(data, expectation)
	chart = chartMaker.makeChart(cleanedData)
		#cleanedData 
	#Do something to print the chart
	#FANCY IOS MAGIC GOES HERE
if __name__ == "__main__":
	chartFromNothing()
