#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# Set pi to false when Pi is unavailable
isPi = False

# Import the smarthome module when if Pi is on
if isPi is True:
    import SmartHome

PORT_NUMBER = 8080


# This handles HTTP Requests
class myHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        print self.path
        relay.toggle(0)
        relay.toggle(1)
        self.wfile.write("{status:\"" + relay.status() + "\"")

        # GET Requests

    def do_GET(self):

        # various Relay functions
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

        def relayToggle(channel=None):
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

        # sample path: /toggle/1 or /on/1

        action = self.path.split("/")[1]
        channel = None
        try:
            channel = self.path.split("/")[2]
        except:
            pass

        if (action == "on"):
            if (channel == "0"):
                relayOn(0)
            elif (channel == "1"):
                relayOn(1)
            else:
                relayOn(0)
                relayOn(1)

        elif (action == "off"):
            if (channel == "0"):
                relayOff(0)
            elif (channel == "1"):
                relayOff(1)
            else:
                relayOff(0)
                relayOff(1)

        elif (action == "toggle"):
            if (channel == "0"):
                relayToggle(0)
            elif (channel == "1"):
                relayToggle(1)
            else:
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
    # Create web server and define the request handler
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port ', PORT_NUMBER

    if isPi is True:  # if Pi is on then call the Gpio and Relay functions
        gpio = SmartHome.Gpio()
        relay = SmartHome.Relay([17, 27])

    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()
