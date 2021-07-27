from typing import Any, Iterable, Iterator

__all__ = (
    "DictKeyIteratorType",
    "DictItemIteratorType",
    "DictValueIteratorType",
    "FrozensetIteratorType",
    "ListIteratorType",
    "SetIteratorType",
    "StringIteratorType",
    "TupleIteratorType",
    "isiterable",
    "filter_array",
    "filter_iterable",
    "filter_noniterable",
    "isstringiterator",
    "istupleiterator",
    "islistiterator",
    "issetiterator",
    "isfrozensetiterator",
    "isdictiterator",
    "isdictkeyiterator",
    "isdictitemiterator",
    "isdictvalueiterator",
)

StringIteratorType = type(iter(""))
TupleIteratorType = type(iter((1,)))
ListIteratorType = type(iter([]))
SetIteratorType = type(iter({1,}))
FrozensetIteratorType = type(iter({1,}))  # same as set
DictKeyIteratorType = type(iter({}))
DictItemIteratorType = type(iter({}.items()))
DictValueIteratorType = type(iter({}.values()))


def _filter_base_type(t: type):
    return lambda x: type(x) == t


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


def isstringiterator(iterator: Iterator[Any]) -> bool:
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
    if not isiterable(iterator):
        return False

    return isinstance(iterator, StringIteratorType)


def istupleiterator(iterator: Iterator[Any]) -> bool:
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
    if not isiterable(iterator):
        return False

    return isinstance(iterator, TupleIteratorType)


def islistiterator(iterator: Iterator[Any]) -> bool:
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
    if not isiterable(iterator):
        return False

    return isinstance(iterator, TupleIteratorType)


def issetiterator(iterator: Iterator[Any]) -> bool:
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
    if not isiterable(iterator):
        return False

    return isinstance(iterator, SetIteratorType)


def isfrozensetiterator(iterator: Iterator[Any]) -> bool:
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
    if not isiterable(iterator):
        return False

    return isinstance(iterator, FrozensetIteratorType)


def isdictiterator(iterator: Iterator[Any]) -> bool:
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
    return isdictkeyiterator(iterator)


def isdictkeyiterator(iterator: Iterator[Any]) -> bool:
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
    if not isiterable(iterator):
        return False

    return isinstance(iterator, DictKeyIteratorType)


def isdictitemiterator(iterator: Iterator[Any]) -> bool:
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
    if not isiterable(iterator):
        return False

    return isinstance(iterator, DictItemIteratorType)


def isdictvalueiterator(iterator: Iterator[Any]) -> bool:
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
    if not isiterable(iterator):
        return False

    return isinstance(iterator, DictValueIteratorType)


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
