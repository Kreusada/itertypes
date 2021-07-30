"""
Iterators in Python aren't a matter of type but of protocol.  A large
and changing number of builtin types implement *some* flavor of
iterator. This private library explores into some of the iterable
types.
"""

from typing import Any, Iterable, Iterator

__version__ = "1.1.4"

StringIteratorType = type(iter(""))
TupleIteratorType = type(iter((1,)))
ListIteratorType = type(iter([]))
SetIteratorType = type(iter({1,}))
FrozensetIteratorType = type(iter(frozenset()))  # same as set
DictIteratorType = type(iter({}))  # same as dict.keys()
DictKeyIteratorType = type(iter({}.keys()))
DictItemIteratorType = type(iter({}.items()))
DictValueIteratorType = type(iter({}.values()))
RangeIteratorType = type(iter(range(0)))
LongRangeIteratorType = type(iter(range(1 << 1000)))

BytearrayIteratorType = type(iter(bytearray()))
ByteIteratorType = type(iter(bytes()))
ListReversedIteratorType = type(iter(reversed([])))

ZipIteratorType = type(iter(zip()))
MapIteratorType = type(iter(map([],[])))


def isiterable(object: Any) -> bool:
    """Returns True or False based on whether the given object is iterable.

    Parameters
    ----------
    object: Any
        The object to see if it's iterable.

    Returns
    -------
    bool
        Whether the given object is iterable.
    """
    try:
        iter(object)
    except TypeError:
        return False
    else:
        return True


def isstringiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a string iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a string iterator.

    Returns
    -------
    bool
        Whether the given object is a string iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, StringIteratorType)


def istupleiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a tuple iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a tuple iterator.

    Returns
    -------
    bool
        Whether the given object is a tuple iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, TupleIteratorType)


def islistiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a list iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a list iterator.

    Returns
    -------
    bool
        Whether the given object is a list iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, TupleIteratorType)


def issetiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a set iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a set iterator.

    Returns
    -------
    bool
        Whether the given object is a set iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, SetIteratorType)


def isfrozensetiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a frozenset iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a frozenset iterator.

    Returns
    -------
    bool
        Whether the given object is a frozenset iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, FrozensetIteratorType)


def isdictiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a dict iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a dict iterator.

    Returns
    -------
    bool
        Whether the given object is a dict iterator.
    """
    return isdictkeyiterator(object)


def isdictkeyiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a dict key iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a dict key iterator.

    Returns
    -------
    bool
        Whether the given object is a dict key iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, DictKeyIteratorType)


def isdictitemiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a dict item iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a dict item iterator.

    Returns
    -------
    bool
        Whether the given object is a dict item iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, DictItemIteratorType)


def isdictvalueiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a dict value iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a dict value iterator.

    Returns
    -------
    bool
        Whether the given object is a dict value iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, DictValueIteratorType)


def israngeiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a range iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a range iterator.

    Returns
    -------
    bool
        Whether the given object is a range iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, RangeIteratorType)


def islongrangeiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a long range iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a long range iterator.

    Returns
    -------
    bool
        Whether the given object is a long range iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, LongRangeIteratorType)


def isbytearrayiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a bytearray iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a bytearray iterator.

    Returns
    -------
    bool
        Whether the given object is a bytearray iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, BytearrayIteratorType)


def isbytesiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a bytes iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a bytes iterator.

    Returns
    -------
    bool
        Whether the given object is a bytes iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, ByteIteratorType)


def islistreversediterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a reversed list iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a reversed list iterator.

    Returns
    -------
    bool
        Whether the given object is a reversed list iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, ListReversedIteratorType)


def iszipiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a zip iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a zip iterator.

    Returns
    -------
    bool
        Whether the given object is a zip iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, ZipIteratorType)


def ismapiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a map iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a map iterator.

    Returns
    -------
    bool
        Whether the given object is a map iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, MapIteratorType)

def filter_array(iterable: Iterable[Any], *types) -> Iterable[Any]:
    """Return the iterable with only the select types inside.

    Parameters
    ----------
    iterable : Iterable[Any]
        The iterable to filter.
    types: tuple
        The types to filter for.

    Returns
    -------
    list
        The filtered iterable.
    """
    return list(filter(lambda x: type(x) in types, iterable))


def filter_iterable(iterable: Iterable[Any]) -> Iterable[Iterable[Any]]:
    """Returns only iterables from an iterable.

    Parameters
    ----------
    iterable : Iterable[Any]
        The iterable to filter.

    Returns
    -------
    list
        The filtered iterable.
    """
    return list(filter(lambda x: isiterable(x), iterable))


def filter_noniterable(iterable: Iterable[Any]) -> Iterable[Any]:
    """Returns only non-iterables from an iterable.

    Parameters
    ----------
    iterable : Iterable[Any]
        The iterable to filter.

    Returns
    -------
    list
        The filtered iterable.
    """
    return list(filter(lambda x: not isiterable(x), iterable))


def filter_type(iterable: Iterable[Any], types: Iterable[type]) -> Iterable[Any]:
    """Filter certain types from an iterable.

    Parameters
    ----------
    iterable : Iterable[Any]
        The iterable to filter.
    types : Iterable[Any]
        The types to filter from the iterable.

    Returns
    -------
    list
        A list of filtered types from the iterable.
    """
    return list(filter(lambda x: type(x) in types, iterable))


def filter_remove_type(iterable: Iterable[Any], types: Iterable[type]) -> Iterable[Any]:
    """Filter certain types out of an iterable.

    Parameters
    ----------
    iterable : Iterable[Any]
        The iterable to filter.
    types : Iterable[Any]
        The types to filter out of the iterable.

    Returns
    -------
    list
        A list of filtered types from the iterable.
    """
    return list(filter(lambda x: type(x) not in types, iterable))
