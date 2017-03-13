# CosmosCloud-Nodes-SD

This repository contains the files to run the Cosmos Cloud Nodes.  It is intended to run on a Raspberry Pi with a relay module and LED module attached via GPIO.

Installation:

The module servers run on Python 3.

Requires [CosmosCloud_SD](https://github.com/alex-osman/CosmosCloud_SD) to communicate with.

To initialize, simply clone this repository and run startup.py.

  ```sh
  $ git clone https://github.com/alex-osman/CosmosCloud-Nodes-SD.git
  $ cd CosmosCloud-Nodes-SD
  $ nohup python startup.py &
  ```

It is recommended to add `startup.py &` to `~/.bashrc` or `/etc/rc.local` to start on boot.

Current feature list:

  * Relay Module
  * Indicator Module

### Tech:

 * [Python 3](https://www.python.org/download/releases/3.0/)
 * ARP - Address Resolution Display and Control
 * [netcat](http://nc110.sourceforge.net/)

### Todo:
  * Theatre Module