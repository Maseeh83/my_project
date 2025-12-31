# file name: s2accDateConv.py

from datetime import datetime

def accidentDateTypeConverter(accidents):
    """This function converts the type of 'ACCIDENT_DATE' value from string to datetime.date"""

    accidentsList = []
    for acc in accidents:
        acc = list(acc)
        acc[4] = datetime.strptime(acc[4], '%d/%m/%Y').date()
        accidentsList.append(acc)

    return accidentsList
