import itertypes


def test_is_string_iterator_type(object):
    assert isinstance(object, itertypes.StringIteratorType)


def test_isiterable(object):
    assert itertypes.isiterable(object)


def test_isdictiterator(object):
    """dict iteration resolves to dict_keyiterator"""
    assert itertypes.isdictiterator(object)
    assert itertypes.isdictkeyiterator(object)


def test_filter_noniterable(iterable):
    return itertypes.filter_noniterable(iterable)


def test_filter_iterable(iterable):
    return itertypes.filter_iterable(iterable)


def test_filter_array(*types):
    tests = [
        True,
        False,
        0,
        1,
        "str",
        bytes(1),
        lambda: None,
    ]
    return itertypes.filter_array(tests, *types)
