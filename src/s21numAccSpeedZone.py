# file name: s21numAccSpeedZone.py

def numAccInSpeedZones(accidents, accSeverities):
	"""Categorises the number of accidents happened in each speed zone based on the accident severity."""

	numAccSeveritySpeedZone = []
	numAccSeverity30kph = [0] * len(accSeverities)
	numAccSeverity40kph = [0] * len(accSeverities)
	numAccSeverity50kph = [0] * len(accSeverities)
	numAccSeverity60kph = [0] * len(accSeverities)
	numAccSeverity70kph = [0] * len(accSeverities)
	numAccSeverity75kph = [0] * len(accSeverities)
	numAccSeverity80kph = [0] * len(accSeverities)
	numAccSeverity90kph = [0] * len(accSeverities)
	numAccSeverity100kph = [0] * len(accSeverities)
	numAccSeverity110kph = [0] * len(accSeverities)
	numAccSeverityCampGround = [0] * len(accSeverities)
	numAccSeverityNotKnown = [0] * len(accSeverities)
	numAccSeverityOther = [0] * len(accSeverities)

	for acc in accidents:
		for i in range(len(accSeverities)):
			if acc[14] == accSeverities[i] and ''.join(acc[15].split()) == '30km/hr':
				numAccSeverity30kph[i] += 1
			elif acc[14] == accSeverities[i] and ''.join(acc[15].split()) == '40km/hr':
				numAccSeverity40kph[i] += 1
			elif acc[14] == accSeverities[i] and ''.join(acc[15].split()) == '50km/hr':
				numAccSeverity50kph[i] += 1
			elif acc[14] == accSeverities[i] and ''.join(acc[15].split()) == '60km/hr':
				numAccSeverity60kph[i] += 1
			elif acc[14] == accSeverities[i] and ''.join(acc[15].split()) == '70km/hr':
				numAccSeverity70kph[i] += 1
			elif acc[14] == accSeverities[i] and ''.join(acc[15].split()) == '75km/hr':
				numAccSeverity75kph[i] += 1
			elif acc[14] == accSeverities[i] and ''.join(acc[15].split()) == '80km/hr':
				numAccSeverity80kph[i] += 1
			elif acc[14] == accSeverities[i] and ''.join(acc[15].split()) == '90km/hr':
				numAccSeverity90kph[i] += 1
			elif acc[14] == accSeverities[i] and ''.join(acc[15].split()) == '100km/hr':
				numAccSeverity100kph[i] += 1
			elif acc[14] == accSeverities[i] and ''.join(acc[15].split()) == '110km/hr':
				numAccSeverity110kph[i] += 1
			elif acc[14] == accSeverities[i] and acc[15] == 'Camping grounds or off road':
				numAccSeverityCampGround[i] += 1
			elif acc[14] == accSeverities[i] and acc[15] == 'Not known':
				numAccSeverityNotKnown[i] += 1
			elif acc[14] == accSeverities[i] and acc[15] == 'Other speed limit':
				numAccSeverityOther[i] += 1

	numAccSeveritySpeedZone.extend([numAccSeverity30kph, numAccSeverity40kph, numAccSeverity50kph,
									numAccSeverity60kph, numAccSeverity70kph, numAccSeverity75kph,
									numAccSeverity80kph, numAccSeverity90kph, numAccSeverity100kph,
									numAccSeverity110kph, numAccSeverityCampGround, numAccSeverityNotKnown,
									numAccSeverityOther])

	return numAccSeveritySpeedZone
