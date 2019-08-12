import roman


def test_roman_2006():
    assert roman.roman_to_decimal('MMVI') == 2006


def test_roman_1944():
    assert roman.roman_to_decimal('MCMXLIV') == 1944
