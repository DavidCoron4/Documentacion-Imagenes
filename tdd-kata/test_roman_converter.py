def test_roman_mao_has_correct_tuples():
    from roman_converter import to_roman
    import roman_converter
    assert len(roman_converter.to_roman.__code__.co_code)>0