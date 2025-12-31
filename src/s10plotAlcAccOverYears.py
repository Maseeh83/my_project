# file name: s10plotAlcAccOverYears.py

import matplotlib.pyplot as plt
import numpy as np

def plotNumAccOverYears(totalAccidents, alcRelatedAccidents):
	"""plots Alcohol and non-alcohol related accidents using bar graph."""

	noAlcRelatedAccidents = np.array(totalAccidents) - np.array(alcRelatedAccidents)
	years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019])
	width = 0.35

	plt.figure(figsize=(10, 5))
	plt.bar(np.arange(len(years)), noAlcRelatedAccidents, width, label='Non-Alcohol-Related',
			color='navy', alpha=0.7)
	plt.bar(np.arange(len(years)) + width, np.array(alcRelatedAccidents), width, label='Alcohol-Related',
			color='maroon', alpha=0.7)
	plt.ylabel('Number of Accidents', fontweight='bold', fontsize=12)
	plt.title('Number of Alcohol-related and Non-alcohol-related Accidents \n From 01/07/2013 To 21/03/2019',
			  fontweight='bold', fontsize=14)
	plt.xticks(np.arange(len(years)) + width / 2, [i for i in years], fontsize=12)
	plt.legend(loc='best')
	plt.show()
