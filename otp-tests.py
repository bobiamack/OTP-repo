from otp import *

def test1_generatePad():
    assert generatePad("hello") > 5

def test2_generatePad():
    assert generatePad("Hello!") > 6

def test1_encrypt():
    assert encrypt("QWERTYUIOP", "Rally Day!") == "Hwpcr Bug!"

def test2_encrypt():
    assert encrypt("QWERTYUIOP", "rALLY dAY!") == "hWPCR bUG!"

def test1_decipher():
    assert decipher("QWERTYUIOP", "Hwpcr Bug!") == "Rally Day!"

def test2_decipher():
    assert decipher("QWERTYUIOP", "hWPCR bUG!") == "rALLY dAY!"

