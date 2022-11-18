import pytest
from account import *


class Test:
    def setup_method(self):
        self.p1 = Account('001-John')
        self.p2 = Account('002-Jane')

    def teardown_method(self):
        del self.p1
        del self.p2

    def test_init(self):
        assert self.p1.get_name() == '001-John'
        assert self.p2.get_name() == '002-Jane'

        assert self.p1.get_balance() == 0
        assert self.p2.get_balance() == 0

    def test_deposit(self):
        self.p1.deposit(5)
        assert self.p1.get_balance() == 5

        self.p2.deposit(5)
        assert self.p2.get_balance() == 5

        self.p1.deposit(-5)
        assert self.p1.get_balance() == 5

        self.p2.deposit(-5)
        assert self.p2.get_balance() == 5

        self.p1.deposit(0)
        assert self.p1.get_balance() == 5

        self.p2.deposit(0)
        assert self.p2.get_balance() == 5

        assert self.p1.deposit(1) is True
        assert self.p1.deposit(-1) is False

    def test_withdraw(self):

        assert self.p1.get_balance() == 0
        assert self.p2.get_balance() == 0

        self.p1.withdraw(5)
        self.p2.withdraw(5)
        assert self.p1.get_balance() == 0
        assert self.p2.get_balance() == 0

        self.p1.withdraw(0)
        self.p2.withdraw(0)
        assert self.p1.get_balance() == 0
        assert self.p2.get_balance() == 0

        self.p1.withdraw(-5)
        self.p2.withdraw(-5)
        assert self.p1.get_balance() == 0
        assert self.p2.get_balance() == 0

        self.p1.deposit(5)
        self.p2.deposit(5)

        self.p1.withdraw(5)
        assert self.p1.get_balance() == 0

        self.p2.withdraw(4)
        assert self.p2.get_balance() == 1

        assert self.p1.withdraw(1) is True
        assert self.p1.withdraw(-1) is False
        assert self.p1.withdraw(11) is False

