from ex import ValueExpectedException


def test_value_expected_exception():
    # См. вывод в консоли
    try:
        raise ValueExpectedException("True", "False", src=test_value_expected_exception.__name__)
    except ValueExpectedException as ex:
        print()
        print(ex.message)
    assert True
