#!/usr/bin/python

import subprocess
import time
import shlex
import os
import urllib2
import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

# Dedicated port
DISCOVERY_PORT = os.getenv('DISCOVERY_PORT', '4200')
print(DISCOVERY_PORT)


def parseModules(jsonModules):
    print(jsonModules)
    modules = json.loads(jsonModules)
    print(modules)
    for module in modules:
        print("Starting ", module['type'])
        subprocess.Popen(["python", module['type'] + "Server.py"])


# Sends a request to the server
def requestModules(coreserver):
    try:
        url = "http://" + coreserver + ":" + DISCOVERY_PORT + "/api/connect"
        jsonModules = urllib2.urlopen(url).read()
        # No modules yet, wait for settings
        if jsonModules != "wait":
            parseModules(jsonModules)
            startServer()
        else:
            time.sleep(5)
            requestModules(coreserver)
    except:
        time.sleep(5)
        requestModules(coreserver)


# Basic handler that will start modules
class myHandler(BaseHTTPRequestHandler):
    # GET Requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Start modules according to the core server's request
        print(self.path)

        # Respond to core server
        self.wfile.write("Modules started")
        return


# Function to start the server after connection with
# core server has been established
def startServer():
    try:
        # Create web server and define the request handler
        server = HTTPServer(("", int(DISCOVERY_PORT)), myHandler)
        print("Started httpserver on port", DISCOVERY_PORT)
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down...")
        server.socket.close()


# Returns a list of all visible machines
def getHosts():
    try:
        # get arp list, remove incompletes, remove everything so only IP
        cmd = "arp -a | grep -v incomplete | sed 's/^.*(//g' | sed 's/).*//g'"
        return shlex.split(subprocess.check_output(cmd, shell=True))
    except:
        print("Error finding Cosmos Cloud")


def netcat(host):
    cmd = "nc -zv -w 2 " + host + " " + DISCOVERY_PORT
    try:
        return subprocess.check_output(cmd,
                                       stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError:
        pass
    except:
        print("Unknown Error")
        raise


# SCRIPT ###
cloudFile = "coreserver"
if os.path.isfile(cloudFile):
    f = open(cloudFile, 'r')
    coreserver = f.read()
    print(coreserver)
    f.close()
    requestModules(coreserver)
else:
    hostFound = False
    while not hostFound:
        print("Looking for Cloud...")
        # Get list of hosts from `arp` with valid IPs
        hosts = getHosts()
        print(hosts)

        # Check each host for DISCOVERY_PORT
        for host in hosts:
            try:
                print(host)
                # Netcat the host and check for success
                if not hostFound and (netcat(host).find("succeeded!") != -1
                                      or netcat(host).find("open") != -1):
                    # TODO: Check that this is not a random server
                    hostFound = True
                    print("The Cloud is located at %s" % (host))

                    # Write IP to file
                    f = open(cloudFile, 'w')
                    f.write(host)
                    f.close()
                    requestModules(host)
            except AttributeError:
                # No return from netcat
                pass
            else:
                pass
            time.sleep(2)
            # Requires `arp` command and `nc` command
