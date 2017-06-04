import unittest

from indicatorFunctions import changeColor, changeStyle

colors = [0, 0, 0]
style = "off"


class MyTestCase(unittest.TestCase):
    def test_changeColor(self):
        self.assertEqual(changeColor(colors), colors)

    def test_changeStyle(self):
        self.assertEqual(changeStyle(style), style)


if __name__ == '__main__':
    unittest.main()
