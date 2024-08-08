## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

## 2. Design the Function Signature

def age_checker():
    parameter: string YYYY-MM-DD
    return a string saying either: - "Acess granted" if 16 or older
                                   - "Access denied" if younger than 16 

    side effects: return age when access denied and required aged (16)

## 3. Create Examples as Tests

```python
# EXAMPLE

"""
if user date is 16 or older print access granted
"""
check_age("2000-01-01") => "Access granted"

"""
if user date is younger than 16 print access denied and age of the user plus required age
"""
check_age("2020-01-01") => "Access denied yur age is ... required age is 16"

"""
if user enter wrong input format raise an error "wrong format need input date as YYYY-MM-DD"
"""
extract_uppercase("06-01-2000") => "wrong format need input date as YYYY-MM-DD"

```

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
