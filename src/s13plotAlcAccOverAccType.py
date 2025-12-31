# file name: s13plotAlcAccOverAccType.py

import matplotlib.pyplot as plt
import numpy as np

def plotAlcAccOverAccType(accTypes, numAccEachType):
	"""Plots a pie chart that displays the proportion of alcohol-related accidents in each accident type category."""

	y = np.array(numAccEachType)

	plt.figure(figsize=(10, 6))
	plt.pie(y, labels = accTypes, startangle = 35, textprops={'color': 'darkblue', 'fontsize': 11})
	plt.title("Accident types involving Alcohol", fontweight='bold', fontsize=14)
	plt.show()
