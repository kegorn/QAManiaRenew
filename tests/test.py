def test_new():
    x = 5
    assert 1 == 1


def test_new2():
    x = 5
    assert 1 == 3


def test_assert():
    print('before')
    result = False
    print('after')
    assert result, 'this test failed in'
