# file name: VictoriaRoadApp.py

import wx

from src.s1dataBase import dataBase
from src.s2accDateConv import accidentDateTypeConverter
from src.s3accidentsInPeriod import accidentsInfoInATimePeriod
from src.s4accTimeHour import accidentTimeHour
from src.s5numOfDays import numOfDays
from src.s6avgAccidentsEachHour import avgNumOfAccidentsEachHour
from src.s7plotAccInEachHour import plotAvgNumOfAccInHour
from src.s8sameTypeAccidents import getSameTypeAccidents
from src.s9numOfAccsEachYear import numOfAccidentsEachYear
from src.s10plotAlcAccOverYears import plotNumAccOverYears
from src.s11accidentTypes import accidentTypes
from src.s12numAlcAccsEachType import numOfAlcAccidentsEachType
from src.s13plotAlcAccOverAccType import plotAlcAccOverAccType
from src.s14accidentSeverities import accidentSeverities
from src.s15numAlcAccsSeverities import numOfAlcAccidentsSeverities
from src.s16plotAlcAccEachSeverity import plotNumAccSeverity
from src.s17roadGeometry import roadGeometry
from src.s18numAccRoadGeo import numAccRoadGeo
from src.s19plotNumAccRoadGeo import plotNumAccRoadGeo
from src.s20accSpeedZones import accSpeedZones
from src.s21numAccSpeedZone import numAccInSpeedZones
from src.s22plotAccSeveritySpeedZone import plotNumAccSeveritySpeedZone

# Global variables
orgAccidents = []
userStartDate = ''
userEndDate = ''

# Main app frame
class VicRoadGui(wx.Frame):
	def __init__(self, parent, id, title):
		wx.Frame.__init__(self, parent, id, title, size=(1280, 680), style=wx.MINIMIZE_BOX|wx.SYSTEM_MENU|
					wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN)
		self.Center()
		self.initialise()

	def initialise(self):
		self.Show(True)
		global orgAccidents # Make the list of accidents global to be accessible to all the classes
		# Inform user about the loading process
		with wx.BusyInfo(wx.BusyInfoFlags().Title("<b>Please wait...</b>").Text("Loading")
             .Foreground(wx.WHITE).Background(wx.Colour(46,139,87))):
			# Create database (if not exists) and retrieve all the accidents information in the database
			orgAccidents, self.columnNames = dataBase()

		pnl = wx.Panel(self, size=(1280, 680))
		self.frame_number = 1

		# Start Date input text box
		startDateText = wx.StaticText(pnl, label="Start Date", pos=(50, 42))
		self.startDate = wx.TextCtrl(pnl, pos=(125, 40), size=(140, 25))
		self.startDate.SetHint('DD/MM/YYYY')
		font = startDateText.GetFont()
		font.PointSize += 1
		startDateText.SetFont(font)
		self.startDate.SetFont(font)


		# End Date input text box for top section
		endDateText = wx.StaticText(pnl, label="End Date", pos=(330, 42))
		self.endDate = wx.TextCtrl(pnl, pos=(400, 40), size=(140, 25))
		self.endDate.SetHint('DD/MM/YYYY')
		endDateText.SetFont(font)
		self.endDate.SetFont(font)

		# Keyword input text box for the top section
		keywordText = wx.StaticText(pnl, label="Search by Keyword in Accident Type", pos=(50, 108))
		self.keyword = wx.TextCtrl(pnl, pos=(290, 105), size=(250, 25))
		self.keyword.SetHint('e.g. object')
		keywordText.SetFont(font)
		self.keyword.SetFont(font)

		# Search button for top section
		btnSearch = wx.Button(pnl, label="Search", pos=(580, 70), size=(100, 25))
		self.Bind(wx.EVT_BUTTON, self.onSearch, btnSearch)

		# Visualize button for top section
		btnVisualise = wx.Button(pnl, label="Visualize", pos=(720, 70), size=(100, 25))
		self.Bind(wx.EVT_BUTTON, self.onVisualise, btnVisualise)

		# Vic Roads image for the top section
		image = wx.Bitmap('vic_road_updated.png')
		control = wx.StaticBitmap(pnl, -1, image)
		control.SetPosition((857, 20))

		# Display accidents information in a tabular format
		self.list_ctrl = wx.ListCtrl(pnl, pos=(10, 170), size=(1240, 450),
									 style=wx.LC_REPORT | wx.BORDER_SUNKEN | wx.LC_HRULES | wx.LC_VRULES)

		font = wx.Font(wx.FontInfo(11).Bold())  # Make the headers bold
		self.list_ctrl.SetFont(font)
		self.list_ctrl.InsertColumn(0, 'NO.')  # For extra column 'No.'
		for i in range(len(self.columnNames)):
			self.list_ctrl.InsertColumn(i + 1, self.columnNames[i])  # Insert a new column in the list control
		self.list_ctrl.SetColumnWidth(0, 45)  # Set the first column width to 45 pixels
		for i in range(len(self.columnNames)):
			self.list_ctrl.SetColumnWidth(i + 1, -2)  # Resize the column to the length of the header

	def onSearch(self, event):
		accidents = accidentDateTypeConverter(orgAccidents)
		# global userStartDate, userEndDate  # Make these two variables global
		userStartDate = ''.join(self.startDate.Value.split())
		userEndDate = ''.join(self.endDate.Value.split())
		keyword = self.keyword.Value

		# Task 1
		accInPeriod, returnedStartDate, returnedEndDate = accidentsInfoInATimePeriod(accidents, userStartDate, userEndDate)

		self.list_ctrl.DeleteAllItems()  # Delete previous search results
		if accInPeriod != [] and keyword != '':
			sameTypeAccidents = getSameTypeAccidents(accInPeriod, keyword)
			accInPeriod = sameTypeAccidents

		if accInPeriod != [] and returnedStartDate and returnedEndDate:
			# Inform user about the loading process
			with wx.BusyInfo(wx.BusyInfoFlags().Title("<b>Please wait...</b>").Text("Loading")
									 .Foreground(wx.WHITE).Background(wx.Colour(46,139,87))):
				index = 0
				for accident in accInPeriod:
					font = wx.Font(wx.FontInfo(10))
					self.list_ctrl.InsertItem(index, str(index + 1))
					self.list_ctrl.SetItemFont(index, font)
					for i in range(4):
						self.list_ctrl.SetItem(index, i+1, accident[i])
					self.list_ctrl.SetItem(index, 5, str(accident[4]))  # Convert type 'datetime.date' to 'string'
					for i in range(5, len(self.columnNames)):
						self.list_ctrl.SetItem(index, i+1, accident[i])
					index += 1

	def onVisualise(self, event):
		# Create an instance of PlotFrame class
		frame = PlotFrame(title='Plots', parent=self.GetParent())
		self.frame_number = 1
		global userStartDate, userEndDate  # Make these two variables global
		userStartDate = ''.join(self.startDate.Value.split())
		userEndDate = ''.join(self.endDate.Value.split())

# Pop up window after clicking the 'Visualize' button
class PlotFrame(wx.Frame):
	def __init__(self, title, parent=None):
		wx.Frame.__init__(self, parent=parent, title=title, size=(400, 450), style=wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.CAPTION|
					wx.CLOSE_BOX|wx.CLIP_CHILDREN)
		pnl = PlotPanel(self)
		self.Center()
		self.Show(True)

class PlotPanel(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, size=(400, 450))

		# Calculations to draw plots

		self.totalAccidents, self.alcRelatedAccidents = numOfAccidentsEachYear(orgAccidents) # Plot B
		self.accTypes = accidentTypes(orgAccidents) # Plot C
		self.numOfAlcAccEachType = numOfAlcAccidentsEachType(orgAccidents, self.accTypes)
		self.accSeverities = accidentSeverities(orgAccidents) # Plot D
		self.numOfAccEachSeverity, self.numOfAlcAccEachSeverity = numOfAlcAccidentsSeverities(orgAccidents, self.accSeverities)
		self.roadGeos = roadGeometry(orgAccidents) # Plot E
		self.numOfAccEachRoadGeo = numAccRoadGeo(orgAccidents, self.roadGeos)
		self.speedZones = accSpeedZones(orgAccidents) # Plot F
		self.numAccSeveritySpeedZone = numAccInSpeedZones(orgAccidents, self.accSeverities)

		# Plot button
		self.frame_number = 1
		btn = wx.Button(self, label='Plot', pos=(150, 350))
		btn.Bind(wx.EVT_BUTTON, self.onPlot)

		# Radio Buttons
		self.rb1 = wx.RadioButton(self, -1, label='Average number of accidents in each hour of the day', pos=(30, 30), style=wx.RB_GROUP)
		self.rb2 = wx.RadioButton(self, -1, label='Number of Alcohol and Non-alcohol related accidents', pos=(30, 80))
		self.rb3 = wx.RadioButton(self, -1, label='Accident types involving Alcohol', pos=(30, 130))
		self.rb4 = wx.RadioButton(self, -1, label='Alcohol and Non-alcohol related accidents based on Severity', pos=(30, 180))
		self.rb5 = wx.RadioButton(self, -1, label='Percentage of accidents based on Road Geometry', pos=(30, 230))
		self.rb6 = wx.RadioButton(self, -1, label='Number of accidents versus Severity and Speed-zone', pos=(30, 280))
		self.Bind(wx.EVT_RADIOBUTTON, self.onRadiogroup1, self.rb1)
		self.Bind(wx.EVT_RADIOBUTTON, self.onRadiogroup2, self.rb2)
		self.Bind(wx.EVT_RADIOBUTTON, self.onRadiogroup3, self.rb3)
		self.Bind(wx.EVT_RADIOBUTTON, self.onRadiogroup4, self.rb4)
		self.Bind(wx.EVT_RADIOBUTTON, self.onRadiogroup5, self.rb5)
		self.Bind(wx.EVT_RADIOBUTTON, self.onRadiogroup6, self.rb6)
		self.rb = self.rb1.GetLabel()  # Set a default value for radio button

	def onRadiogroup1(self, event):
		self.rb = self.rb1.GetLabel()

	def onRadiogroup2(self, event):
		self.rb = self.rb2.GetLabel()

	def onRadiogroup3(self, event):
		self.rb = self.rb3.GetLabel()

	def onRadiogroup4(self, event):
		self.rb = self.rb4.GetLabel()

	def onRadiogroup5(self, event):
		self.rb = self.rb5.GetLabel()

	def onRadiogroup6(self, event):
		self.rb = self.rb6.GetLabel()

	def onPlot(self, event):
		if self.rb == 'Average number of accidents in each hour of the day':
			self.accidents = accidentDateTypeConverter(orgAccidents)
			self.accInPeriod, self.returnedStartDate, self.returnedEndDate = accidentsInfoInATimePeriod(self.accidents,
																										userStartDate, userEndDate)
			if self.accInPeriod != []:
				self.accidentsFin = accidentTimeHour(self.accInPeriod)  # Plot A
				self.numberOfDays = numOfDays(self.returnedStartDate, self.returnedEndDate)
				self.avgNumOfAccInHour = avgNumOfAccidentsEachHour(self.accidentsFin, self.numberOfDays)
				plotAvgNumOfAccInHour(self.avgNumOfAccInHour, self.returnedStartDate, self.returnedEndDate)

		elif self.rb == 'Number of Alcohol and Non-alcohol related accidents':
			plotNumAccOverYears(self.totalAccidents, self.alcRelatedAccidents)
		elif self.rb == 'Accident types involving Alcohol':
			plotAlcAccOverAccType(self.accTypes, self.numOfAlcAccEachType)
		elif self.rb == 'Alcohol and Non-alcohol related accidents based on Severity':
			plotNumAccSeverity(self.numOfAccEachSeverity, self.numOfAlcAccEachSeverity, self.accSeverities)
		elif self.rb == 'Percentage of accidents based on Road Geometry':
			plotNumAccRoadGeo(self.roadGeos, self.numOfAccEachRoadGeo)
		else:
			plotNumAccSeveritySpeedZone(self.numAccSeveritySpeedZone, self.accSeverities)


app = wx.App()
frame = VicRoadGui(None, -1, "Victoria Roads Data")
app.MainLoop()
