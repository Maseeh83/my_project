# file name: s4accTimeHour.py

def accidentTimeHour(accidents):
	"""This function replaces the values of sixth column (ACCIDENT_TIME) with their Hours as integer."""

	for accident in accidents:
		accident[5] = int(accident[5][:2])

	return accidents
