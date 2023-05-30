import pytest
from calculette import Calculette, Error

@pytest.fixture
def cal():
    return Calculette()


def test_add(cal):
	cal.add(400,600)
	assert cal.res == 1000

def test_div(cal):
	cal.divide(1,10)
	assert cal.res == 0.1

def test_div(cal):
	cal.add(1,1)
	assert cal.res == 3

def test_raise(cal):
	with pytest.raises(Error):
		cal.divide(1,0)
