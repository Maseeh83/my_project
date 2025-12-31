# file name: s12numAlcAccsEachType.py

def numOfAlcAccidentsEachType(accidents, accTypes):
	"""This function counts the number of alcohol related accidents based on accident types."""

	numOfAlcAccEachType = [0] * len(accTypes)
	for acc in accidents:
		for i in range(len(accTypes)):
			if acc[7] == accTypes[i] and acc[45] == "Yes":
				numOfAlcAccEachType[i] += 1

	return numOfAlcAccEachType
