# file name: s16plotAlcAccEachSeverity.py

import matplotlib.pyplot as plt
import numpy as np

def plotNumAccSeverity(numAccSeverity, numAlcAccSeverity, accSeverities):
	"""Plots the percentage of alcohol and non-alcohol related accidents based on severity."""

	alcAccPercentage = np.array(numAlcAccSeverity)/np.array(numAccSeverity)*100
	nonAlcAccPercentage = (np.array(numAccSeverity) - np.array(numAlcAccSeverity))/np.array(numAccSeverity)*100
	width = 0.3

	plt.figure(figsize=(9, 5))
	plt.bar(np.arange(len(accSeverities)), nonAlcAccPercentage, width, label='Non-Alcohol-Related',
			color='navy', alpha=0.7)
	plt.bar(np.arange(len(accSeverities)) + width, alcAccPercentage, width, label='Alcohol-Related',
			color='maroon', alpha=0.7)
	plt.ylabel('Percentage of Accidents', fontweight='bold', fontsize=12)
	plt.title('Percentage of Alcohol and Non-alcohol related Accidents \n in each Accident Severity category',
			  fontweight='bold', fontsize=14)
	plt.xticks(np.arange(len(accSeverities)) + width / 2, accSeverities, fontsize=11, rotation=-10)
	plt.legend(loc='best')
	plt.show()
