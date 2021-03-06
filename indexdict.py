# -*- coding: utf-8 -*

"""
    pymeasure.indexdict
    -------------------

    The module is part of the pymeasure package. It contains the IndexDict
    class which provides a lightweight and intuitiv interface for the
    collections.OrderedDict class with additional indexing.

"""

from collections import OrderedDict


class IndexDict(object):
    """Light interface for collections.OrderedDict with additional indexing.

    The class got designed for an intuitive, interactive work on the
    ipython shell. The indices give easy access to the items while the keys
    allow a description of the content. IndexDict is compareable to a table
    which has an caption for each column.

    """

    def __init__(self):
        """Initialize an indexable dictionary.

        """

        self._odict = OrderedDict()

    def __iter__(self):
        """x.__iter__() <==> iter(x)

        Return listiterator for IndexDict values.

        """

        return iter(list(self._odict.values()))

    def __len__(self):
        """x.__len__() <==> len(x)

        Return number of items in IndexDict.

        """

        return len(self._odict)

    def __getitem__(self, key):
        """x.__getitem__(key) <==> x[key]

        Return IndexDict item of key.

        """

        # Try to get the item which belongs to the key
        try:
            return self._odict[key]
        # If direct key lookup fails try the index.
        except KeyError:
            try:
                # Get the key that bekongs ot the index
                key = list(self._odict.keys())[key]
                return self._odict[key]
            except:
                raise KeyError

    def __setitem__(self, key, item):
        """x.__setitem__(key, item) <==> x[key]=item

        The key must be a str to allow additional indexing.

        """

        if type(key) is not str:
            raise KeyError('key must be str')
        else:
            self._odict[key] = item

    def __delitem__(self, key):
        """x.__delitem__(key) <==> del x[key]

        Removes IndexDict pair of key.

        """

        try:
            del self._odict[key]
        except KeyError:
            try:
                key = list(self._odict.keys())[key]
                del self._odict[key]
            except:
                raise KeyError

    def __repr__(self):
        """x.__repr__() <==> repr(x)

        Returns the string 'IndexDict([0: 'key0', 1: 'key1', ....])'
        """

        repr_str = self.__class__.__name__

        if self.__len__():
            repr_str += '['
            for index, key in enumerate(self._odict.keys()):
                repr_str += str(index) + ': \'' + key + '\', '
            repr_str = repr_str[:-2] + ']'

            return repr_str

        else:
            return repr_str + '[]'

    def index(self):
        """Return a list of the all (index, key) pairs.

        """
        index_keys = list()
        for pair in enumerate(self._odict.keys()):
            index_keys.append(pair)
        return index_keys

    def keys(self):
        """Return list of keys in IndexDict

        """
        return list(self._odict.keys())

    def items(self):

        return list(self._odict.items())
