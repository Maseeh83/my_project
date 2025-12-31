# file name: s9numOfAccsEachYear.py

def numOfAccidentsEachYear(accidents):
	"""This function calculates the total number of accidents and the number of alcohol-related accidents
	each year (from 2013 to 2019)."""

	years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019']
	numAccEachYear = [0] * 7  # Total number of accidents each year (from 2013 to 2019).
	numAlcAccEachYear = [0] * 7  # The number of Alcohol related accidents each year (from 2013 to 2019).

	for acc in accidents:
		for i in range(len(years)):
			if acc[4][-4:] == years[i]:
				numAccEachYear[i] += 1
				if acc[45] == 'Yes':
					numAlcAccEachYear[i] += 1

	return numAccEachYear, numAlcAccEachYear
