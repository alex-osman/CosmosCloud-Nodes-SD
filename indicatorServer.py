#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from indicatorFunctions import changeColor, changeStyle, isPi

PORT_NUMBER = 8081
style = "off"
colors = [0, 0, 0]



# This handles HTTP Requests
class myHandler(BaseHTTPRequestHandler):
    # GET Requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Remove the leading '/'
        self.path = self.path[1:]

        # /{style}
        # /{r}/{g}/{b}
        # /{style}/{r}/{g}/{b}
        args = self.path.split('/')
        if len(args) == 1:
            changeStyle(args[0])
        elif len(args) == 3:
            changeColor([int(args[0]), int(args[1]), int(args[2])])
        elif len(args) == 4:
            changeStyle(args[0])
            changeColor([int(args[1]), int(args[2]), int(args[3])])
        else:
            print("Unknown path")

        self.wfile.write("{\n\tstyle: '" + style + "',\n\trgb: [" +
                         ', '.join(map(str, colors)) + "]\n}\n")
        # self.wfile.write(rgb.brightness)
        return


try:
    # Create web server and define the request handler
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ', PORT_NUMBER)
    if isPi:
        gpio = SmartHome.Gpio()
        rgb = SmartHome.rgb([26, 19, 13])
    server.serve_forever()


except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
