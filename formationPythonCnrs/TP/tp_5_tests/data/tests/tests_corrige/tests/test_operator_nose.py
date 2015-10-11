import calculatrice.operateur as op
from nose.tools import assert_equals
from nose.plugins.attrib import attr

class testOpNose:
    @classmethod
    def setUpClass(self):
        self.a = 4
        self.b = 5

    @attr(op="addOrSous")
    def testAdd(self):
        assert_equals(op.addition(self.a, self.b), 9.)

    @attr(op="addOrSous")
    def testSous(self):
        assert_equals(op.soustraction(self.a, self.b), -1.)

    @attr(op="multOrDiv")
    def testMult(self):
        assert_equals(op.multiplication(self.a, self.b), 20.)

    @attr(op="multOrDiv")
    def testDiv(self):
        assert_equals(op.division(self.a, self.b), .8)
