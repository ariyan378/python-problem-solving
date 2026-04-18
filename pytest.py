# test_spellcheck.py

''' 
Import statements: 
    1. Import pytest and spellcheck modules
'''
# Import pytest for writing and running tests
import pytest

# Import spellcheck module (even if not used directly, it is required by the instruction)
import spellcheck


# String variables to be tested
alpha = "Checking the length & structure of the sentence."
beta = "This sentence should fail the test"


# Do not delete this function. You may change the value assigned to input to test different inputs to your test functions.
@pytest.fixture
def input_value():
    # Default input value for testing
    input = alpha
    return input


# First test function test_length()
def test_length(input_value):
    """ 
    Tests whether a string has fewer than 10 words and fewer than 50 chars.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string has fewer than 10 words
        2. Use an assert statement to check the given string has fewer than 50 chars

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """

    # Split the sentence into words using space as separator
    words = input_value.split()

    # Assert that the number of words is less than 10
    assert len(words) < 10

    # Assert that the total number of characters in the string is less than 50
    assert len(input_value) < 50


# Second test function test_struc()
def test_struc(input_value):
    """ 
    Tests whether a string begins with a capital letter and ends with a period.

    [IMPLEMENT ME]
        1. Use an assert statement to check the given string begins with a capital letter
        2. Use an assert statement to check the given string ends with a period ('.')

    Args:
      input_value: a function that returns a string, which can be configured
                   in the input_value() function
    """

    # Check if the first character of the string is uppercase
    assert input_value[0].isupper()

    # Check if the string ends with a period
    assert input_value.endswith(".")
    

# Run these tests with:
# python3 -m pytest test_spellcheck.py