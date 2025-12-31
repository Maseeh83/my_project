# file name: s15numAlcAccsSeverities.py

def numOfAlcAccidentsSeverities(accidents, accSeverities):
	"""This function calculates the total number of accidents and the number of alcohol-related accidents
	based on the severity category."""

	numOfAccEachSeverity = [0] * len(accSeverities)
	numOfAlcAccEachSeverity = [0] * len(accSeverities)

	for acc in accidents:
		for i in range(len(accSeverities)):
			if acc[14] == accSeverities[i]:
				numOfAccEachSeverity[i] += 1
				if acc[45] == "Yes":
					numOfAlcAccEachSeverity[i] += 1

	return numOfAccEachSeverity, numOfAlcAccEachSeverity
