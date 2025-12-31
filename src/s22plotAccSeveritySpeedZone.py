# file name: s22plotAccSeveritySpeedZone.py

import matplotlib.pyplot as plt
import numpy as np

def plotNumAccSeveritySpeedZone(numAccSeveritySpeedZone, accSeverities):
	"""Plots the number of accidents based on their severities and speed-zones."""

	width = 0.06  # width of bar
	plt.figure(figsize=(11, 5.5))

	# Position of the bar on X axis
	barPos = np.arange(len(numAccSeveritySpeedZone[0]))

	plt.bar(barPos-5*width, numAccSeveritySpeedZone[0], color='brown', width=width,
			edgecolor='grey', label='30km/hr')
	plt.bar(barPos-4*width, numAccSeveritySpeedZone[1], color='g', width=width,
			edgecolor='grey', label='40km/hr')
	plt.bar(barPos-3*width, numAccSeveritySpeedZone[2], color='b', width=width,
			edgecolor='grey', label='50km/hr')
	plt.bar(barPos-2*width, numAccSeveritySpeedZone[3], color='r', width=width,
			edgecolor='grey', label='60km/hr')
	plt.bar(barPos-width, numAccSeveritySpeedZone[4], color='m', width=width,
			edgecolor='grey', label='70km/hr')
	plt.bar(barPos, numAccSeveritySpeedZone[5], color='y', width=width,
			edgecolor='grey', label='75km/hr')
	plt.bar(barPos+width, numAccSeveritySpeedZone[6], color='gray', width=width,
			edgecolor='grey', label='80km/hr')
	plt.bar(barPos+2*width, numAccSeveritySpeedZone[7], color='lime', width=width,
			edgecolor='grey', label='90km/hr')
	plt.bar(barPos+3*width, numAccSeveritySpeedZone[8], color='tab:blue', width=width,
			edgecolor='grey', label='100km/hr')
	plt.bar(barPos+4*width, numAccSeveritySpeedZone[9], color='blueviolet', width=width,
			edgecolor='grey', label='110km/hr')
	plt.bar(barPos+5* width, numAccSeveritySpeedZone[10], color='tab:brown', width=width,
			edgecolor='grey', label='Camping grounds or off road')
	plt.bar(barPos+6*width, numAccSeveritySpeedZone[11], color='tab:pink', width=width,
			edgecolor='grey', label='Not known')
	plt.bar(barPos+7* width, numAccSeveritySpeedZone[12], color='tab:gray', width=width,
			edgecolor='grey', label='Other speed limit')

	plt.ylabel('Number of Accidents', fontweight='bold', fontsize=15)
	plt.title('Number of Accidents based on their Severities and Speed-zones \n From 1/7/2013 To 21/3/2019',
			  fontweight='bold', fontsize=14)
	plt.xticks([r + width for r in range(len(numAccSeveritySpeedZone[0]))], [i for i in accSeverities]
			   , fontsize=12)
	plt.legend(loc='upper left', title='Speed Zones')
	plt.show()
