# file name: s20accSpeedZones.py

def accSpeedZones(accidents):
	"""Returns all unique speed zones available in the data set."""

	speedZones = set()
	for acc in accidents:
		speedZones.add(acc[15])
	speedZones = sorted(list(speedZones))

	return speedZones
