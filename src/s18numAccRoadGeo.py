# file name: s18numAccRoadGeo.py

def numAccRoadGeo(accidents, roadGeos):
	"""Calculates the number of accidents for each road geometry available in the data set."""

	numOfAccEachRoadGeo = [0] * len(roadGeos)
	for acc in accidents:
		for i in range(len(roadGeos)):
			if acc[13] == roadGeos[i]:
				numOfAccEachRoadGeo[i] += 1

	return numOfAccEachRoadGeo
