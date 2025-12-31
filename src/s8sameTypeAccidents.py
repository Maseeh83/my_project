# file name: s8sameTypeAccidents.py

def getSameTypeAccidents(accidents, keyword):
	"""This function takes a list of accidents and a keyword and returns a list of accidents caused by
	an accident type that contains the keyword."""

	sameTypeAccidents = []
	for acc in accidents:
		if keyword.upper() in acc[7].upper():
			sameTypeAccidents.append(acc)

	return sameTypeAccidents
