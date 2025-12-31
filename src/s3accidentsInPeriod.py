# file name: s3accidentsInPeriod.py

from datetime import datetime
import wx

def accidentsInfoInATimePeriod (accidents, startDate, endDate):
    """To find the list of accidents that happened between startDate and endDate."""

    from operator import itemgetter

    # To inform user when startDate or endDate fields are empty.
    if startDate == '' or endDate == '':
        wx.MessageBox('Please enter valid dates between 1/7/2013 and 21/3/2019.')
        return [], None, None

    else:
        try:
            firstDate = datetime.strptime('1/7/2013', '%d/%m/%Y').date()
            lastDate = datetime.strptime('21/3/2019', '%d/%m/%Y').date()
            accidents = sorted(accidents, key=itemgetter(4), reverse=False)
            startDate = datetime.strptime(startDate, '%d/%m/%Y').date()
            endDate = datetime.strptime(endDate, '%d/%m/%Y').date()


            if startDate < firstDate and firstDate <= endDate <= lastDate:
                startDate = firstDate
            elif startDate < firstDate and endDate > lastDate:
                startDate = firstDate
                endDate = lastDate
            elif firstDate <= startDate <= lastDate and endDate > lastDate:
                endDate = lastDate
            elif (startDate < firstDate and endDate < firstDate) or (startDate > lastDate and endDate > lastDate):
                wx.MessageBox('Invalid dates: The dates must be between 1/7/2013 and 21/3/2019.')
                return [], None, None
            else:
                if startDate > endDate:
                    wx.MessageBox('Your End Date is less than Start Date!')
                    return [], None, None

            accidentsInPeriod = []
            for acc in accidents:
                if startDate <= acc[4] <= endDate:
                    accidentsInPeriod.append(acc)
            return accidentsInPeriod, startDate, endDate

        except ValueError:
            wx.MessageBox("Invalid date format: Please enter the date in the format DD/MM/YYYY.")
            return [], None, None
