import Surajsinh as name_point

def test_length_greater_than_one():
    assert len(name_point.hi_my_name_is()) > 1

def test_output_is_alphabetic():
    assert name_point.hi_my_name_is().isalpha()

def test_output_is_equal_to_name():
    assert name_point.hi_my_name_is() == "SURAJSINH"

def test_output_is_in_uppercase():
    assert name_point.hi_my_name_is().isupper()

def test_output_is_alphanumeric():
    assert name_point.hi_my_name_is().isalnum()

def test_output_has_correct_length():
    assert len(name_point.hi_my_name_is()) == 9

def test_output_starts_with_specific_letter():
    assert name_point.hi_my_name_is().startswith("S")

def test_output_ends_with_specific_letter():
    assert name_point.hi_my_name_is().endswith("H")

def test_output_is_not_empty():
    assert name_point.hi_my_name_is() != ""

