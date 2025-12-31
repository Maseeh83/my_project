# file name: s6avgAccidentsEachHour.py

import numpy as np

def avgNumOfAccidentsEachHour(accidents, numOfDays):
	"""This function calculates the average number of accidents each hour a day."""

	# A list that will contain the number of accidents each hour a day in order started from 12am.
	accidentsEachHour = [0] * 24

	for acc in accidents:
		if acc[5] == 0:
			accidentsEachHour[0] += 1
		elif acc[5] == 1:
			accidentsEachHour[1] += 1
		elif acc[5] == 2:
			accidentsEachHour[2] += 1
		elif acc[5] == 3:
			accidentsEachHour[3] += 1
		elif acc[5] == 4:
			accidentsEachHour[4] += 1
		elif acc[5] == 5:
			accidentsEachHour[5] += 1
		elif acc[5] == 6:
			accidentsEachHour[6] += 1
		elif acc[5] == 7:
			accidentsEachHour[7] += 1
		elif acc[5] == 8:
			accidentsEachHour[8] += 1
		elif acc[5] == 9:
			accidentsEachHour[9] += 1
		elif acc[5] == 10:
			accidentsEachHour[10] += 1
		elif acc[5] == 11:
			accidentsEachHour[11] += 1
		elif acc[5] == 12:
			accidentsEachHour[12] += 1
		elif acc[5] == 13:
			accidentsEachHour[13] += 1
		elif acc[5] == 14:
			accidentsEachHour[14] += 1
		elif acc[5] == 15:
			accidentsEachHour[15] += 1
		elif acc[5] == 16:
			accidentsEachHour[16] += 1
		elif acc[5] == 17:
			accidentsEachHour[17] += 1
		elif acc[5] == 18:
			accidentsEachHour[18] += 1
		elif acc[5] == 19:
			accidentsEachHour[19] += 1
		elif acc[5] == 20:
			accidentsEachHour[20] += 1
		elif acc[5] == 21:
			accidentsEachHour[21] += 1
		elif acc[5] == 22:
			accidentsEachHour[22] += 1
		else:
			accidentsEachHour[23] += 1

	accidentsEachHour.append(0)  # to add '12:00 AM' to the end of plot x-axis.

	# A list contains the average number of accidents each hour a day.
	avgNumOfAccInEachHour = np.array(accidentsEachHour) / numOfDays
	return avgNumOfAccInEachHour
