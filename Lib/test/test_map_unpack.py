doctests = """

Unpack dict

    >>> {'a': a, 'b': b, 'c': c} = dict(a=1, b=2, c=3)
    >>> (a, b, c) == (1, 2, 3)
    True

Partially unpack dict

    >>> {'a': a} = dict(a=1, b=2, c=3)
    >>> a == 1
    True

Unpack complex keys

    >>> {(1, 2): a} = {(1, 2): 3}
    >>> a == 3
    True

Unpacking missing keys

    >>> {'d': d} = dict(a=1, b=2, c=3)
    Traceback (most recent call last):
      ...
    KeyError: 'd'

Unpacking is atomic

    >>> {'a': a, 'b': b, 'c': c, 'd': d} = dict(a=1, b=2, c=3)
    Traceback (most recent call last):
      ...
    KeyError: 'd'
    >>> a
    Traceback (most recent call last):
        ...
    NameError: name 'a' is not defined
    >>> b
    Traceback (most recent call last):
        ...
    NameError: name 'b' is not defined
    >>> c
    Traceback (most recent call last):
        ...
    NameError: name 'c' is not defined

"""

__test__ = {'doctests' : doctests}

def test_main(verbose=False):
    from test import support
    from test import test_map_unpack
    support.run_doctest(test_map_unpack, verbose)

if __name__ == "__main__":
    test_main(verbose=True)
