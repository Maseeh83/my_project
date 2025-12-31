# file name: s11accidentTypes.py

def accidentTypes(accidents):
	"""Returns all unique accident types available in the data set."""

	accTypes = set()
	for acc in accidents:
		accTypes.add(acc[7])
	accTypes = sorted(list(accTypes))

	return accTypes
