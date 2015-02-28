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
	def __init__(self, pvals=[],func=lambda:(0)):
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

def make_models(data_subset):
	pass
def trainModels(models, data_subset):
	pass
