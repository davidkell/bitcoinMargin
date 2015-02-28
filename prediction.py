import numpy as np
def getClosingPrices(data):
	return [i['PX_LAST'] for i in data]
class Model: 
	"""A single mathematical model of the past data.

	To initiate a model, give a list pvals. pvals should be the 
	probability of a given result, for every possible result 
		(over sensible values of bitcoin based on recent years.)
	pvals must sum to a value between .99 and 1.01 
		(small error margin included to account for floating points.)
	Alternatively, instead of providing the p-values explicitly, one
	may instead 
	"""
	def __init__(self, time_difference, pvals=[],func=lambda:(0)):
		try:
			assert sum(pvals) >.99
			assert sum(pvals) <  1.01
			self.pvals = pvals
			self.discrete = 1
		except:
			self.func = func
			self.discrete = 0

	def p(self,val):
		if self.discrete:
			return self.pvals[val]
		return self.func(val)
	def confidence_value_below(self, confidence):
		if self.discrete:
			pass
		pass
class Distribution:
	"""A distribution is anything that will return sensible values.

	Distribution itself is an extremely thin class: the main utility is
	found in the subclasses, which provide greater specificity."""
	pass
class Continious_Distribution(Distribution):
	def __init__(self, f,data):
		NineNine,NineFive,SevenFive,Fifty=f(data)
		self.NineNine = NineNine
		self.NineFive = NineFive
		self.SevenFive = SevenFive
		self.Fifty = Fifty
		pass
class List_Distribution(Distribution):
	def __init__(self, time_difference, pvals, vals):
		assert sum(pvals) >.99
		assert sum(pvals) <  1.01
		self.pvals = pvals
		assert type(time_difference) == type(1)
		self.td = time_difference
		assert len(pvals)==len(vals)
		self.vals = vals
	def get_confidence_value_below(self, confidence):
		summing = 0
		for i in range(len(pvals)):
			if summing < confidence:
				summing+=pvals[i]
			else:
				break
		return i
def trainModels(models, data_subset):
	pass
def make_models(data_subset):
	dumbStDev = Continious_Distribution(stDevApproach,data)
	return dumbStDev
	#Look at data in different resolutions.
	#Check out weekend effects, check out 
	#Consider other bloomberg
def stDevApproach(data_subset):
	cp = getClosingPrices(data_subset)
	arr = np.array(cp)
	stdev = np.std(arr)
	mean = getClosingPrices(data_subset)[-1]
		#Gets closing price on most recent date.
	Fifty = mean
	SevenFive = mean + stdev*.675
	NineFive = mean + stdev*1.644
	NineNine = mean + stdev*2.33
	return NineNine,NineFive,SevenFive,Fifty

def test_continious_distribution(f,data):
	NineNineOvers = 0
	NineFiveOvers = 0
	SevenFiveOvers= 0
	FiftyOvers    = 0
	for i in range(200):
		c = Continious_Distribution(f,data[-i-1:])
		if c.NineNine < data[-i]:
			NineNineOvers+=1
		if c.NineNine < data[-i]:
			NineNineOvers+=1
		if c.NineNine < data[-i]:
			NineNineOvers+=1
		if c.NineNine < data[-i]:
			NineNineOvers+=1
	print("NineNineOvers"+str(NineNineOvers)+"Expected:"+"2")
	print("NineFiveOvers"+str(NineFivevers)+"Expected:"+"10")
	print("SevenFivevers"+str(SevenFiveOvers)+"Expected:"+"50")
	print("FiftyOvers"+str(FiftyOvers)+"Expected:"+"100")
test_continious_distribution(stDevApproach)