import json

import unittest

from hello_world import app

class testcalci(unittest.testcase):

    def test_addition(self):
        self.assertequal(app.add(5,4),9)
        self.assertequal(app.add(-5,5),0)
        self.assertequal(app.add(-2,-2),-4)

    def test_subtract(self):
        self.assertequal(app.sub(5,4),1)
        self.assertequal(app.sub(-5,5),-10)
        self.assertequal(app.sub(-2,-2),0)

    def test_multiplicat(self):
        self.assertequal(app.mul(5,4),20)
        self.assertequal(app.mul(-5,5),-25)
        self.assertequal(app.mul(-5,-5),25)

if__name__=='__main__':
    unittest.main()

