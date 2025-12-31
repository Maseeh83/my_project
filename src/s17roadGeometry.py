# file name: s17roadGeometry.py

def roadGeometry(accidents):
	"""Returns all unique road geometries available in the data set."""

	roadGeos = set()
	for acc in accidents:
		roadGeos.add(acc[13])
	roadGeos = sorted(list(roadGeos))

	return roadGeos
