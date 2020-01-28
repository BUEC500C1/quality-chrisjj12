import arab_conv

def test_answer():
    assert arab_conv.conv(3) == "III"
    assert arab_conv.conv(4178) == "MMMMCLXXVIII"
    assert arab_conv.conv(25) == "XXV"
    assert arab_conv.conv(2384) == "MMCCCLXXXIV"
    assert arab_conv.conv(4999) == "MMMMCMXCIX"
    assert arab_conv.conv(-3) == "Number is not valid"
    assert arab_conv.conv(5000) == "Number is not valid"
    assert arab_conv.conv(100) == "C"
    assert arab_conv.conv("a") == "Number is not valid"

