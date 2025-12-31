# file name: s5numOfDays.py

def numOfDays(fDate, lDate):
	"""This function calculates the number of days between two dates."""

	numberOfDays = (lDate - fDate).days + 1
	return numberOfDays
