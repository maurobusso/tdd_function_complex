import pytest
from lib.check_age import *

def test_user_older_than_sixteen():
    assert check_age("1993-06-01") == "Access granted"

def test_user_youger_than_sixteen():
    assert check_age("2020-01-01") == "Access denied yur age is 4 required age is 16"

def test_input_in_wrong_format():
    with pytest.raises(ValueError) as error:
        check_age("01-01-1990")
    error_message = str(error.value)
    assert error_message == "Sorry wrong format insert dat as YYYY-MM-DD"

