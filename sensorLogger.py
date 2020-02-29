import grovepi
from time import sleep
from math import isnan

dht_sensor_port = 4
dht_sensor_type = 0
light_sensor = 1

grovepi.pinMode(light_sensor, "INPUT")

while True:
	try:
        # get the temperature and Humidity from the DHT sensor
		[ temp,hum ] = grovepi.dht(dht_sensor_port, dht_sensor_type)
		print("temp =", temp, "C\thumidity =", hum,"%")

		if isnan(temp) is True or isnan(hum) is True or isnan(light) is True:
			raise TypeError('NAN error')

        writeRecordsToDB( temp, hum, light)

	except (IOError, TypeError) as e:
		print(str(e))
        	break
	
	except KeyboardInterrupt as e:
		print(str(e))
		break

    #set the recording interval to 10 mins

	sleep(600)
