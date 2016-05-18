from ds18b20 import DS18B20
from time import sleep
from oauth2client.service_account import ServiceAccountCredentials
import gspread, datetime

scope = ['https://spreadsheet.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('TempWithDoc-7e9e14ed4d4e.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("TempWithDoc").sheet1

def main():
	sensor = DS18B20()
	while True:
		time = datetime.now().strftime('%Y/%M/%d %H:%M:%S')
		temp = sensor.get_temperatures([DS18B20.DEGREES_C, DS18B20.DEGREES_F, DS18B20.KELVIN])

		row = 0
		for values in wks.col_values(1):  ## loop count row
    				row = row + 1
			addRow = [time, temp[0], temp[2], temp[1]] 
			wks.resize(row)
			wks.append_row(addRow)
			sleep(10)





if __main__ == "__main__":
	main()