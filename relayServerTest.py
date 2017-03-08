import unittest

from relayFunctions import relayOn, relayOff, relayToggle


class MyTestCase(unittest.TestCase):
    def test_relayOn(self):
        self.assertEqual(relayOn(0), "On: 0")
        self.assertEqual(relayOn(1), "On: 1")
        self.assertEqual(relayOn(), "On: None")

    def test_relayOff(self):
        self.assertEqual(relayOff(0), "Off: 0")
        self.assertEqual(relayOff(1), "Off: 1")
        self.assertEqual(relayOff(), "Off: None")

    def test_relayToggle(self):
        self.assertEqual(relayToggle(0), "toggle: 0")
        self.assertEqual(relayToggle(1), "toggle: 1")
        self.assertEqual(relayToggle(), "toggle: None")


if __name__ == '__main__':
    unittest.main()
