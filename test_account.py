import pytest
from account import *


p1 = Account('001-John')
p2 = Account('002-Jane')


#assert self.p1.get_balance() == approx(20.5, abs=0.001)
def test_init():
    assert p1.get_name() == '001-John'
    assert p2.get_name() == '002-Jane'

    assert p1.get_balance() == pytest.approx(0, abs=0.001)
    assert p2.get_balance() == pytest.approx(0, abs=0.001)


def test_deposit():
    p1.deposit(5)
    assert p1.get_balance() == pytest.approx(5, abs=0.001)

    p2.deposit(5)
    assert p2.get_balance() == pytest.approx(5, abs=0.001)

    p1.deposit(-5)
    assert p1.get_balance() == pytest.approx(5, abs=0.001)

    p2.deposit(-5)
    assert p2.get_balance() == pytest.approx(5, abs=0.001)

    p1.deposit(0)
    assert p1.get_balance() == pytest.approx(5, abs=0.001)

    p2.deposit(0)
    assert p2.get_balance() == pytest.approx(5, abs=0.001)

    assert p1.deposit(1) is True
    assert p1.deposit(-1) is False


def test_withdraw():
    assert p1.get_balance() == pytest.approx(0, abs=0.001)
    assert p2.get_balance() == pytest.approx(0, abs=0.001)

    p1.withdraw(5)
    p2.withdraw(5)
    assert p1.get_balance() == pytest.approx(0, abs=0.001)
    assert p2.get_balance() == pytest.approx(0, abs=0.001)

    p1.withdraw(0)
    p2.withdraw(0)
    assert p1.get_balance() == pytest.approx(0, abs=0.001)
    assert p2.get_balance() == pytest.approx(0, abs=0.001)

    p1.withdraw(-5)
    p2.withdraw(-5)
    assert p1.get_balance() == pytest.approx(0, abs=0.001)
    assert p2.get_balance() == pytest.approx(0, abs=0.001)

    p1.deposit(5)
    p2.deposit(5)

    p1.withdraw(5)
    assert p1.get_balance() == pytest.approx(5, abs=0.001)

    p2.withdraw(4)
    assert p2.get_balance() == pytest.approx(1, abs=0.001)

    assert p1.withdraw(1) is True
    assert p1.withdraw(-1) is False
    assert p1.withdraw(11) is False
