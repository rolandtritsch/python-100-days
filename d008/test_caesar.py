import d008.caesar as caesar


def test_chr2idx():
    assert caesar.chr2idx("a") == 0
    assert caesar.chr2idx("z") == 25


def test_idx2chr():
    assert caesar.idx2chr(0) == "a"
    assert caesar.idx2chr(25) == "z"


def test_shift():
    assert caesar.shift(0, 1) == 1
    assert caesar.shift(len(caesar.ALPHABET) - 1, 1) == 0
    assert caesar.shift(1, -1) == 0
    assert caesar.shift(0, -1) == len(caesar.ALPHABET) - 1


def test_encode():
    assert caesar.encode("abc", 1) == "bcd"
    assert caesar.encode("xyz", 2) == "zAB"
    assert caesar.encode("ABC", 3) == "DEF"
    assert caesar.encode("XYZ", 4) == "123"


def test_decode():
    assert caesar.decode("bcd", 1) == "abc"
    assert caesar.decode("zAB", 2) == "xyz"
    assert caesar.decode("DEF", 3) == "ABC"
    assert caesar.decode("123", 4) == "XYZ"

    text = "Hello, World!"
    assert caesar.decode(caesar.encode(text, 256), 256) == text
    assert caesar.decode(caesar.encode(text, 1024), 1024) == text
