from ds18b20 import DS18B20
from time import sleep
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import gspread

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('TempWithDoc-1fffdaa0ccad.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open("tempNew").sheet1

def main():
	sensor = DS18B20()
	while True:
		time = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
		temp = sensor.get_temperatures([DS18B20.DEGREES_C, DS18B20.DEGREES_F, DS18B20.KELVIN])
                print time
                print temp[0]
		print temp[1]
		print temp[2]
		print "========"
		print "Adding row....."

		row = 0
		try:
                        for values in wks.col_values(1):  ## loop count row
                                row = row + 1
                        
                        addRow = [time, temp[0], temp[2], temp[1]] 
                        wks.resize(row)
                        wks.append_row(addRow)
                        print "Added row"
                        sleep(5)
                except:
                        print("Exit")
                        break;





if __name__ == "__main__":
	main()
