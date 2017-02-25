#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
from time import time

#Set pi to false when Pi is unavailable
isPi = False

#Import the smarthome module when if Pi is on
if isPi is True:
	import SmartHome

PORT_NUMBER = 8080


#This handles HTTP Requests
class myHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		print self.path
		relay.toggle(0)
		relay.toggle(1)
		self.wfile.write("{status:\"" + relay.status() + "\"")

	#GET Requests
	def do_GET(self):

		#various Relay functions

		#turns On the 2 outlets based on the channel # and if the pi is on
		def relayOn(channel=None):
			if isPi is False:
				print("On: " + str(channel))
			else:
				if channel == 1:
					relay.turnOn(1)
				elif channel == 0:
					relay.turnOn(0)
				else:
					relay.turnOn()

		#turns off the 2 outlets based on the channel # and if the pi is on
		def relayOff(channel=None):
			if isPi is False:
				print("Off: " + str(channel))
			else:
				if channel == 1:
					relay.turnOff(1)

				elif channel == 0:
					relay.turnOff(0)
				else:
					relay.turnOff()

		#toggles the 2 outlets based on the channel # and if the pi is on
		def relayToggle(channel = None):
		   if isPi is False:
		       print("toggle: " + str(channel))
		   else:
		       if channel == 1:
		           relay.toggle(1)
		       elif channel == 0:
		           relay.toggle(0)
		       else:
		           relay.toggle()


		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		print "Looking at ", self.path


		#sample path: /toggle/1 or /on/1
		var1 = self.path.split("/")[1] #get the first value from the path after the first slash
		var2 = self.path.split("/")[2] #get the second value from the path after the second slash


		if (var1 == "on"):
			try:
				if (var2 == "0"):
					relayOn(0)
				else:
					relayOn(1)
			except:
				relayOn(0)
				relayOn(1)
		elif (var1 == "off"):
			try:

				if (var2  == "0"):
					relayOff(0)
				elif (var2  == "1"):
					relayOff(1)
			except:
					relayOff(0)
					relayOff(1)

		elif (var1 == "toggle"):
			try:
				if (var2 == "0"):
					relayToggle(0)
				elif (var2  == "1"):
					relayToggle(1)
			except:
				relayToggle(0)
				relayToggle(1)
		else:
			print "none"

		if isPi is False:
			self.wfile.write("Pi is False!")
		else:
			self.wfile.write("Relay Status: " + relay.status())
		return

try:
	#Create web server and define the request handler
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER

	if isPi is True: #if Pi is on then call the Gpio and Relay functions
		gpio = SmartHome.Gpio()
		relay = SmartHome.Relay([17, 27])

	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
