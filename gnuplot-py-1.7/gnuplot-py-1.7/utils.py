#! /usr/bin/env python

# $Id: utils.py,v 2.4 2003/04/21 09:44:09 mhagger Exp $

# Copyright (C) 1998-2003 Michael Haggerty <mhagger@alum.mit.edu>
#
# This file is licensed under the GNU Lesser General Public License
# (LGPL).  See LICENSE.txt for details.

"""utils.py -- Utility functions used by Gnuplot.

This module contains utility functions used by Gnuplot.py which aren't
particularly gnuplot-related.

"""

__cvs_version__ = '$Revision: 2.4 $'

import string
import Numeric


def float_array(m):
    """Return the argument as a Numeric array of type at least 'Float32'.

    Leave 'Float64' unchanged, but upcast all other types to
    'Float32'.  Allow also for the possibility that the argument is a
    python native type that can be converted to a Numeric array using
    'Numeric.asarray()', but in that case don't worry about
    downcasting to single-precision float.

    """

    try:
        # Try Float32 (this will refuse to downcast)
        return Numeric.asarray(m, Numeric.Float32)
    except TypeError:
        # That failure might have been because the input array was
        # of a wider data type than Float32; try to convert to the
        # largest floating-point type available:
        return Numeric.asarray(m, Numeric.Float)


def write_array(f, set,
                item_sep=' ',
                nest_prefix='', nest_suffix='\n', nest_sep=''):
    """Write an array of arbitrary dimension to a file.

    A general recursive array writer.  The last four parameters allow
    a great deal of freedom in choosing the output format of the
    array.  The defaults for those parameters give output that is
    gnuplot-readable.  But using '(",", "{", "}", ",\n")' would output
    an array in a format that Mathematica could read.  'item_sep'
    should not contain '%' (or if it does, it should be escaped to
    '%%') since it is put into a format string.

    The default 2-d file organization::

        set[0,0] set[0,1] ...
        set[1,0] set[1,1] ...

    The 3-d format::

        set[0,0,0] set[0,0,1] ...
        set[0,1,0] set[0,1,1] ...

        set[1,0,0] set[1,0,1] ...
        set[1,1,0] set[1,1,1] ...

    """

    if len(set.shape) == 1:
        (columns,) = set.shape
        assert columns > 0
        fmt = string.join(['%s'] * columns, item_sep)
        f.write(nest_prefix)
        f.write(fmt % tuple(set.tolist()))
        f.write(nest_suffix)
    elif len(set.shape) == 2:
        # This case could be done with recursion, but `unroll' for
        # efficiency.
        (points, columns) = set.shape
        assert points > 0 and columns > 0
        fmt = string.join(['%s'] * columns, item_sep)
        f.write(nest_prefix + nest_prefix)
        f.write(fmt % tuple(set[0].tolist()))
        f.write(nest_suffix)
        for point in set[1:]:
            f.write(nest_sep + nest_prefix)
            f.write(fmt % tuple(point.tolist()))
            f.write(nest_suffix)
        f.write(nest_suffix)
    else:
        # Use recursion for three or more dimensions:
        assert set.shape[0] > 0
        f.write(nest_prefix)
        write_array(f, set[0],
                    item_sep, nest_prefix, nest_suffix, nest_sep)
        for subset in set[1:]:
            f.write(nest_sep)
            write_array(f, subset,
                        item_sep, nest_prefix, nest_suffix, nest_sep)
        f.write(nest_suffix)

