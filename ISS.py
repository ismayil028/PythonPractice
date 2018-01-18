import json
import turtle
import urllib.request
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read().decode('utf8'))
people = result['people']
for p in people:
	print(p['name'] + ' in ' +p['craft'])

print('People in Space: ' , result['number'])

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read().decode('utf8'))

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']

print('Latitude: ' , lat)
print('Longitude: ' , lon)

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180, -90 , 180 , 90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(float(90))

iss.penup()
iss.goto(float(lon),float(lat))

lat = 29.5502
lon = -95.097

location = turtle.Turtle()

location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api/open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read().decode('utf8'))

over = result[response][1]['risetime']

style = ('Arial',6, 'bold')
location.write(time.ctime(over) , font=style)