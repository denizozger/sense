import requests
import time
import datetime
import os
import calendar

from sense_hat import SenseHat

url = os.getenv('HOME_API_URL', 'http://localhost:5000/readings') + '/readings'
readings = dict()
response = None
sense = SenseHat()

while True: 
	temperature = round(sense.get_temperature(), 1)
	pressure = round(sense.get_pressure(), 1)
	humidity = round(sense.get_humidity(), 1)

	readings = dict(temperature=temperature,
					pressure=pressure,
					humidity=humidity,
					time=int(time.time()))

	response = requests.post(url, data=readings, allow_redirects=True)
	print(response.content, readings)

	time.sleep(1)

