import unittest
from account import *


class MyTestCase(unittest.TestCase):
    delta_value = 0.001

    def setUp(self):
        self.p1 = Account('001-John')
        self.p2 = Account('002-Jane')

    def tearDown(self):
        del self.p1
        del self.p2

    def test_init(self):
        self.assertAlmostEqual(self.p1.get_name(), '001-John')
        self.assertAlmostEqual(self.p2.get_name(), '002-Jane')

        self.assertAlmostEqual(self.p1.get_balance(), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.get_balance(), 0, delta=self.delta_value)

    def test_deposit(self):
        self.p1.deposit(5)
        self.assertAlmostEqual(self.p1.get_balance(), 5, delta=self.delta_value)

        self.p2.deposit(5)
        self.assertAlmostEqual(self.p2.get_balance(), 5, delta=self.delta_value)

        self.p1.deposit(-5)
        self.assertAlmostEqual(self.p1.get_balance(), 5, delta=self.delta_value)

        self.p2.deposit(-5)
        self.assertAlmostEqual(self.p2.get_balance(), 5, delta=self.delta_value)

        self.p1.deposit(0)
        self.assertAlmostEqual(self.p1.get_balance(), 5, delta=self.delta_value)

        self.p2.deposit(0)
        self.assertAlmostEqual(self.p2.get_balance(), 5, delta=self.delta_value)

        self.assertTrue(self.p1.deposit(1))
        self.assertFalse(self.p1.deposit(-1))

    def test_withdraw(self):
        self.assertAlmostEqual(self.p1.get_balance(), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.get_balance(), 0, delta=self.delta_value)

        self.assertAlmostEqual(self.p1.withdraw(5), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.withdraw(5), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p1.withdraw(0), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.withdraw(0), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p1.withdraw(-5), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.withdraw(-5), 0, delta=self.delta_value)

        self.p1.deposit(5)
        self.p2.deposit(5)

        self.assertAlmostEqual(self.p1.withdraw(5), 0, delta=self.delta_value)
        self.assertAlmostEqual(self.p2.withdraw(4), 1, delta=self.delta_value)

        self.assertTrue(self.p1.withdraw(1))
        self.assertFalse(self.p1.withdraw(-1))
        self.assertFalse(self.p1.withdraw(11))


if __name__ == '__main__':
    unittest.main()
