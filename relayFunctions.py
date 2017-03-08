#!/usr/bin/python


# Set pi to false when Pi is unavailable
isPi = False

if isPi is True:
    import SmartHome

    gpio = SmartHome.Gpio()
    relay = SmartHome.Relay([17, 27])


# various Relay functions
def relayOn(channel=None):
    if isPi is False:
        print("On: " + str(channel))
        result = ("On: " + str(channel))

    else:
        if channel == 1:
            result = relay.turnOn(1)
        elif channel == 0:
            result = relay.turnOn(0)
        else:
            result = relay.turnOn()
    return result


def relayOff(channel=None):
    if isPi is False:
        print("Off: " + str(channel))
        result = ("Off: " + str(channel))
    else:
        if channel == 1:
            result = relay.turnOff(1)

        elif channel == 0:
            result = relay.turnOff(0)
        else:
            result = relay.turnOff()
    return result


def relayToggle(channel=None):
    if isPi is False:
        print("toggle: " + str(channel))
        result = ("toggle: " + str(channel))
    else:
        if channel == 1:
            result = relay.toggle(1)
        elif channel == 0:
            result = relay.toggle(0)
        else:
            result = relay.toggle()

    return result
