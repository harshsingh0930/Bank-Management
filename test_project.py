from project import get_name, get_num, get_email, get_crn
import re


def test_get_name():
    assert not re.match(r"^[A-Za-z]+( [A-Za-z]+)? [A-Za-z]+$","elo")
    assert re.match(r"^[A-Za-z]+( [A-Za-z]+)? [A-Za-z]+$","hello world")
    assert re.match(r"^[A-Za-z]+( [A-Za-z]+)? [A-Za-z]+$","Hello world man")
    assert not re.match(r"^[A-Za-z]+( [A-Za-z]+)? [A-Za-z]+$","Hello world man you")

def test_get_num():
    assert re.match(r"^[0-9]{10}$","9891876123")
    assert not re.match(r"^[0-9]{10}$","1233456643455")
    assert not re.match(r"^[0-9]{10}$","harsh")

def test_get_email():
    assert not re.match(r"^\w+(\.\w+)?@\w+\.\w+(\.\w+)?$","hoee")
    assert re.match(r"^\w+(\.\w+)?@\w+\.\w+(\.\w+)?$","user.name@gmail.com")
    assert re.match(r"^\w+(\.\w+)?@\w+\.\w+(\.\w+)?$","user.name@ugc.ac.in")

def test_get_crn():
    crn = get_crn()
    assert 1000 <= crn <= 9999
