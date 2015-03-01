import json
import csv

import cleaner
import prediction
import dataGather
#import chartMaker
def exportCSV():
	#a = json.loads(dataGather.get(bitcoinName,currency,amount))
	dct = json.load(open("historicalBitcoinData.json"))
	cleaned = cleaner.use(dct)
	cp = prediction.getClosingPrices(cleaned)
	times = prediction.getClosingTimes(cleaned)
	with open("output.csv","wb") as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow([str(fa) for fa in cp])
		writer.writerow([str(gb) for gb in times])
def chartFromNothing():
	#bitcoinName = "XBTC"
	#currency = "GBP"
	#amount = "40"
	time=1 #time in days
	#data = json.loads(dataGather.get(bitcoinName,currency,amount))
	data = json.load(open("historicalBitcoinData.json"))
	cleanedData = cleaner.use(data)
	print(cleanedData)
	expectation = prediction.flux(data,time)
	#chart = chartMaker.makeChart(data, expectation)
	chart = chartMaker.makeChart(cleanedData)
		#cleanedData 
	#Do something to print the chart
	#FANCY IOS MAGIC GOES HERE
if __name__ == "__main__":
	chartFromNothing()


