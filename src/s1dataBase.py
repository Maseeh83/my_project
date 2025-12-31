# file name: s1dataBase.py

from os.path import isfile
import sqlite3
import csv

def dataBase():
	"""To create a database from file 'Crash Statistics Victoria.csv' using sqlite script,
	fetch all data from the database and return all the accidents in a list."""

	path = 'data/Crash Statistics Victoria.csv'
	if not isfile("CrashStatisticsVictoria.db"):
		connection = sqlite3.connect("CrashStatisticsVictoria.db")
		cursor = connection.cursor()
		sql_command = """CREATE TABLE IF NOT EXISTS crash (
					OBJECTID, ACCIDENT_NO, ABS_CODE, ACCIDENT_STATUS, ACCIDENT_DATE, ACCIDENT_TIME,	ALCOHOLTIME, 
					ACCIDENT_TYPE, DAY_OF_WEEK,	DCA_CODE, HIT_RUN_FLAG, LIGHT_CONDITION, POLICE_ATTEND, ROAD_GEOMETRY,
					SEVERITY, SPEED_ZONE, RUN_OFFROAD, NODE_ID, LONGITUDE, LATITUDE, NODE_TYPE, LGA_NAME, REGION_NAME,
					VICGRID_X, VICGRID_Y, TOTAL_PERSONS, INJ_OR_FATAL, FATALITY, SERIOUSINJURY, OTHERINJURY, NONINJURED,
					MALES, FEMALES, BICYCLIST, PASSENGER, DRIVER, PEDESTRIAN, PILLION, MOTORIST, UNKNOWN, PED_CYCLIST_5_12,
					PED_CYCLIST_13_18, OLD_PEDESTRIAN, OLD_DRIVER, YOUNG_DRIVER, ALCOHOL_RELATED, UNLICENCSED, NO_OF_VEHICLES,
					HEAVYVEHICLE, PASSENGERVEHICLE, MOTORCYCLE, PUBLICVEHICLE, DEG_URBAN_NAME, DEG_URBAN_ALL, LGA_NAME_ALL,
					REGION_NAME_ALL, SRNS, SRNS_ALL, RMA, RMA_ALL, DIVIDED, DIVIDED_ALL, STAT_DIV_NAME);"""
		cursor.execute(sql_command)

		with open(path) as csvfile:
			table = csv.reader(csvfile)
			next(table, None)  # skip the headers
			for p in table:
				format_str = """INSERT OR IGNORE INTO crash (OBJECTID, ACCIDENT_NO, ABS_CODE, ACCIDENT_STATUS, ACCIDENT_DATE, 
							ACCIDENT_TIME, ALCOHOLTIME, ACCIDENT_TYPE, DAY_OF_WEEK, DCA_CODE, HIT_RUN_FLAG,	LIGHT_CONDITION, 
							POLICE_ATTEND, ROAD_GEOMETRY, SEVERITY, SPEED_ZONE, RUN_OFFROAD, NODE_ID, LONGITUDE, LATITUDE, 
							NODE_TYPE, LGA_NAME, REGION_NAME, VICGRID_X, VICGRID_Y, TOTAL_PERSONS, INJ_OR_FATAL, FATALITY, 
							SERIOUSINJURY, OTHERINJURY, NONINJURED,	MALES, FEMALES, BICYCLIST, PASSENGER, DRIVER, PEDESTRIAN, 
							PILLION, MOTORIST, UNKNOWN, PED_CYCLIST_5_12, PED_CYCLIST_13_18, OLD_PEDESTRIAN, OLD_DRIVER, 
							YOUNG_DRIVER, ALCOHOL_RELATED, UNLICENCSED, NO_OF_VEHICLES,	HEAVYVEHICLE, PASSENGERVEHICLE,	
							MOTORCYCLE, PUBLICVEHICLE, DEG_URBAN_NAME, DEG_URBAN_ALL, LGA_NAME_ALL, REGION_NAME_ALL, SRNS, 
							SRNS_ALL, RMA, RMA_ALL, DIVIDED, DIVIDED_ALL, STAT_DIV_NAME)
							 
							VALUES ("{id}", "{accNo}", "{absCode}", "{accStatus}", "{accDate}", "{accTime}", "{alcTime}",
							"{accType}", "{day}", "{dcaCode}", "{hrFlag}", "{light}", "{police}", "{roadGeo}", "{severity}",
							"{speedZone}", "{offroad}", "{nodeID}", "{longitude}", "{latitude}", "{nodeType}", "{LGA}", 
							"{region}", "{vicgX}", "{vicgY}", "{tPersons}", "{injOrFatal}", "{fatality}", "{seriousInj}", 
							"{otherInj}", "{nonInj}", "{males}", "{females}", "{bicyclist}", "{passenger}", "{driver}", 
							"{pedestrian}", "{pillion}", "{motorist}", "{unknown}", "{pedCyc5}", "{pedCyc13}", "{oldPed}", 
							"{oldDrv}", "{youngDrv}", "{alcRelated}", "{unlicencsed}", "{numOfVehicles}", "{heavyVeh}", 
							"{passengerVeh}", "{motorcycle}", "{publicVeh}", "{degUrbanName}", "{degUrbanAll}", "{LGAAll}", 
							"{regionAll}", "{srns}", "{srnsAll}", "{rma}", "{rmaAll}", "{divided}", "{dividedAll}", 
							"{statDivName}");"""

				sql_command = format_str.format(id=p[0], accNo=p[1], absCode=p[2], accStatus=p[3], accDate=p[4],
												accTime=p[5], alcTime=p[6], accType=p[7], day=p[8], dcaCode=p[9], hrFlag=p[10],
												light=p[11], police=p[12], roadGeo=p[13], severity=p[14], speedZone=p[15],
												offroad=p[16], nodeID=p[17], longitude=p[18], latitude=p[19], nodeType=p[20],
												LGA=p[21], region=p[22], vicgX=p[23], vicgY=p[24], tPersons=p[25],
												injOrFatal=p[26], fatality=p[27], seriousInj=p[28], otherInj=p[29],
												nonInj=p[30], males=p[31], females=p[32], bicyclist=p[33], passenger=p[34],
												driver=p[35], pedestrian=p[36], pillion=p[37], motorist=p[38], unknown=p[39],
												pedCyc5=p[40], pedCyc13=p[41], oldPed=p[42], oldDrv=p[43], youngDrv=p[44],
												alcRelated=p[45], unlicencsed=p[46], numOfVehicles=p[47], heavyVeh=p[48],
												passengerVeh=p[49], motorcycle=p[50], publicVeh=p[51], degUrbanName=p[52],
												degUrbanAll=p[53], LGAAll=p[54], regionAll=p[55], srns=p[56], srnsAll=p[57],
												rma=p[58], rmaAll=p[59], divided=p[60], dividedAll=p[61], statDivName=p[62])

				cursor.execute(sql_command)
		connection.commit()
		connection.close()

	connection = sqlite3.connect("CrashStatisticsVictoria.db")
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM crash")
	orgAccidents = cursor.fetchall()
	columnNames = [i[0] for i in cursor.description]
	connection.close()

	return orgAccidents, columnNames
