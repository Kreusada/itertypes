"""
This library has some useful types and functions used to get types of iterables.
Whilst iterable types were purposely avoided by the types library, iterables offer
unique types which could sometimes be useful to obtain.
"""

from collections import OrderedDict, defaultdict, deque
from typing import Any, Iterable, Iterator

BytearrayIteratorType         = type(iter(bytearray()))
ByteIteratorType              = type(iter(bytes()))
DefaultDictIteratorType       = type(iter(defaultdict()))
DequeIteratorType             = type(iter(deque()))
DictItemIteratorType          = type(iter({}.items()))
DictIteratorType              = type(iter({}))  # same as dict.keys()
DictKeyIteratorType           = type(iter({}.keys()))
DictReversedItemIteratorType  = type(iter(reversed({}.items())))
DictReversedIteratorType      = type(iter(reversed({})))  # same as dict.keys()
DictReversedKeyIteratorType   = type(iter(reversed({}.keys())))
DictReversedValueIteratorType = type(iter(reversed({}.values())))
DictValueIteratorType         = type(iter({}.values()))
EnumerateIteratorType         = type(iter(enumerate([])))
FrozensetIteratorType         = type(iter(frozenset()))  # same as set
ListIteratorType              = type(iter([]))
ListReversedIteratorType      = type(iter(reversed([])))
LongRangeIteratorType         = type(iter(range(1 << 1000)))
MapIteratorType               = type(iter(map([],[])))
MemoryviewIteratorType        = type(iter(memoryview(bytes())))  # generic
OrderedDictIteratorType       = type(iter(OrderedDict()))
RangeIteratorType             = type(iter(range(0)))
SetIteratorType               = type(iter({1,}))
StringIteratorType            = type(iter(""))
TupleIteratorType             = type(iter((1,)))
ZipIteratorType               = type(iter(zip()))


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


def isdictreversediterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a reversed dict iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a reversed dict iterator.

    Returns
    -------
    bool
        Whether the given object is a reversed dict iterator.
    """
    return isdictreversedkeyiterator(object)


def isdictreversedkeyiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a reversed dict key iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a reversed dict key iterator.

    Returns
    -------
    bool
        Whether the given object is a reversed dict key iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, DictReversedKeyIteratorType)


def isdictreverseditemiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a reversed dict item iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a reversed dict item iterator.

    Returns
    -------
    bool
        Whether the given object is a reversed dict item iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, DictReversedItemIteratorType)


def isdictreversedvalueiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a reversed dict value iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a reversed dict value iterator.

    Returns
    -------
    bool
        Whether the given object is a reversed dict value iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, DictReversedValueIteratorType)


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


def ismemoryviewiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a memoryview iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a memoryview iterator.

    Returns
    -------
    bool
        Whether the given object is a memoryview iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, MemoryviewIteratorType)


def isordereddictiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a collections.OrderedDict() iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a OrderedDict iterator.

    Returns
    -------
    bool
        Whether the given object is a OrderedDict iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, OrderedDictIteratorType)


def isdefaultdictiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a collections.defaultdict() iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a defaultdict iterator.

    Returns
    -------
    bool
        Whether the given object is a defaultdict iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, DefaultDictIteratorType)


def isenumerateiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is an enumerate iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's an enumerate iterator.

    Returns
    -------
    bool
        Whether the given object is an enumerate iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, EnumerateIteratorType)


def isdequeiterator(object: Iterator[Any]) -> bool:
    """Returns True or False based on whether the given object is a collections.deque() iterator.

    Parameters
    ----------
    object: Any
        The object to see if it's a deque iterator.

    Returns
    -------
    bool
        Whether the given object is a deque iterator.
    """
    if not isiterable(object):
        return False

    return isinstance(object, DequeIteratorType)


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
