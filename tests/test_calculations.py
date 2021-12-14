from app.calculations import add, substract, multiply, divide, BankAccount
import pytest

'''@pytest.mark.parametrize("a, b, result", [
    (2,7,9),
    (3,7,10),
    (12,7,19)
])

def test_add(a,b,result):
    assert add(a,b,) == result

def test_substract():
    assert substract(5,3) == 2

def test_multiply():
    assert multiply(5,5) == 25

def test_divide():
    assert divide(20,5) == 4'''

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("deposited, withdrawn, total", [
    (200,100,100),
    (1000,200,800)
])
def test_bank_transactions(zero_bank_account,deposited, withdrawn, total):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrawn)
    assert zero_bank_account.balance == total


def test_bank_account(bank_account):
    assert bank_account.balance == 50

def test_default(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_insufficient_funds(bank_account):
    with pytest.raises(Exception):
        bank_account.withdraw(200)

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70
    
