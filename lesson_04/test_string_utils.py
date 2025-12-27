import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("Volk", "Volk"),
    (" Volk", "Volk"),
    ("     Volk", "Volk"),
    ("  Volk  ", "Volk  ")
    ])
def test_trim_pos(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    (" ", ""),
    ("         ", ""),
    ])
def test_trim_neg(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "y", True),
    ("100%", "%", True)
 ])
def test_contains_pos(string, symbol, expected):
    utils = StringUtils()
    assert utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "s", False),
    ("SkyPro", "U", False),
    ("  ", "U", False)
    ])
def test_contains_neg(string, symbol, expected):
    utils = StringUtils()
    assert utils.contains(string, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Тест", "с", "Тет"),
    ("12345", "3", "1245"),
])
def test_delete_symbol_positive(string, symbol, expected):
    utils = StringUtils()
    result = utils.delete_symbol(string, symbol)
    assert result == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "x", "SkyPro"),
    ("", "a", ""),
    ("aaaa", "a", ""),
    ("ababa", "aba", "ba")
  ])
def test_delete_symbol_negative(string, symbol, expected):
    utils = StringUtils()
    result = utils.delete_symbol(string, symbol)
    assert result == expected
