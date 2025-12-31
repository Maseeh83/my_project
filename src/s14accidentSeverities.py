# file name: s14accidentSeverities.py

def accidentSeverities(accidents):
	"""Returns all unique accident severities available in the data set."""

	accSeverity = set()
	for acc in accidents:
		accSeverity.add(acc[14])
	accSeverity = sorted(list(accSeverity))

	return accSeverity
