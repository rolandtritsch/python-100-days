import d082.morsecode as morse

def test_convert():
    assert morse.convert("hello") == ".... . .-.. .-.. ---"
    assert morse.convert("world") == ".-- --- .-. .-.. -.."
    assert morse.convert("python") == ".--. -.-- - .... --- -."
    assert morse.convert("SOS") == "... --- ..."
    assert morse.convert("SOS") == morse.convert("sos")
    assert morse.convert("") == ""
    assert morse.convert(" ") == ""
