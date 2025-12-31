# file name: s7plotAccInEachHour.py

import matplotlib.pyplot as plt
import numpy as np

def plotAvgNumOfAccInHour(avgNumOfAccEachHour, startDate, endDate):
	"""Plots the average number of accidents each hour a day in a period of time."""

	hours = ['12:00 AM', '', '', '3:00 AM', '', '', '6:00 AM', '', '', '9:00 AM', '', '', '12:00 PM',
			 '', '', '3:00 PM', '', '', '6:00 PM', '', '', '9:00 PM', '', '', '12:00 AM']
	width = 0.5 # set width of bar

	plt.figure(figsize=(10, 5))
	plt.bar(np.arange(len(hours)) + width, avgNumOfAccEachHour, width=width, color='royalblue',
			edgecolor='darkblue', alpha=0.7)
	plt.grid(color='grey', linestyle='--', linewidth=1, axis='y', alpha=0.7)
	plt.ylabel('Average number of Accidents', fontweight='bold', fontsize=12)
	plt.title(f'Average number of Accidents each Hour a day \n From {startDate} To {endDate}',
			  fontweight='bold', fontsize=14)

	ax = plt.subplot(111)
	# Hide the right and top spines
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)

	plt.xticks(np.arange(len(hours)), [i for i in hours], rotation=-10)
	plt.show()
