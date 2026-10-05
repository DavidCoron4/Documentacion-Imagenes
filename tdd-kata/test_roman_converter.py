import pytest
from roman_converter import to_roman

@pytest.mark.parametrize(
    "number, exepcted",
    [
        (1,"I"),
        (2,"II"),
        (3,"III"),
        (4,"IV"),
        (5,"V"),
        (6,"VI"),
        (9,"IX"),
        (10,"X"),
    ],
)
def test_to_roman_conversion(number, exepcted):
    assert to_roman(number) == exepcted