def to_roman(number):
    roman_map = [
        (10,"X"),
        (9,"IX"),
        (5,"V"),
        (4,"IV"),
        (1,"I"),
    ]
    result = ""
    for value, symbol in roman_map:
        while number >= value:
            result += symbol
            number -= value
    return result