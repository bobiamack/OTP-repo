from otp import *

def test_generatePad():
    assert generatePad("hello!") > 6

def test_encrypt():
    assert encrypt("QWERTYUIOP", "Rally Day!") == "Hwpcr Bug!"

def test_decipher():
    assert decipher("QWERTYUIOP", "Hwpcr Bug!") == "Rally Day!"
