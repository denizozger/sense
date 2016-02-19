import requests
import time
import datetime

url = 'http://localhost:5000/readings'
data = dict()
response = None

while True: 
	data = dict(temperature='10', time=datetime.datetime.now())
	response = requests.post(url, data=data, allow_redirects=True)
	print(response.content)
	time.sleep(300)

