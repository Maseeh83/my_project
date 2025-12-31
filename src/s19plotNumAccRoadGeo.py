# file name: s19plotNumAccRoadGeo.py

import matplotlib.pyplot as plt
import numpy as np

def plotNumAccRoadGeo(roadGeos, numAccEachRoadGeo):
	"""Displays the number of accidents related to each road type (road geometry)."""

	# Total number of accidents
	totalAccNums = 0
	for numAcc in numAccEachRoadGeo:
		totalAccNums += numAcc

	width = 0.5
	y_pos = np.arange(len(roadGeos))

	plt.figure(figsize=(9, 5))
	plt.subplots_adjust(left=0.25) # To move the graph to the left
	plt.grid(color='grey', linestyle='--', linewidth=1, axis='x', alpha=0.7)

	ax = plt.subplot(111)
	ax.barh(y_pos, np.array(numAccEachRoadGeo)/totalAccNums*100, color='firebrick', alpha=0.8)
	ax.set_yticks(y_pos)
	ax.set_yticklabels(roadGeos)
	ax.set_xlabel('Percentage (%)', fontweight='bold', fontsize=12)
	ax.set_ylabel('Road Geometry', fontweight='bold', fontsize=12)
	ax.set_title('Percentage of Accidents based on Road Geometries', fontweight='bold', fontsize=14)

	plt.show()
