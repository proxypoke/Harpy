# Harpy - Handy Abstraction of Redis in PYthon
#
# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is free software under the non-terms
# of the Anti-License. Do whatever the fuck you want.
#
# Github: https://www.github.com/proxypoke/harpy
# (Shortlink: https://git.io/harpy)
#
# Format options for vim. Please adhere to them.
# vim: set et ts=4 sw=4 tw=80:

import sys
import collections
import pickle

from ._redis import _acquire
from .base import HarpyBase
from . import utils


class HarpyString(HarpyBase, collections.ByteString):
    '''banana banana banana'''

    def __init__(self, rediskey, obj, encoding=None, errors='strict'):
        if encoding is None:
            encoding = sys.getdefaultencoding()
        self._encoding = encoding
        self._errors = errors
        s = obj.encode(encoding, errors)
        sp = pickle.dumps(s)
        super().__init__(rediskey, b'string', sp)

    def set_value(self, value):
        r = _acquire()
        r.set("harpy." + self._rediskey + ".contents", value)

    def _get(self):
        r = _acquire()
        with utils.lock(r, self._rediskey):
            picstr = r.get("harpy." + self._rediskey + ".contents")
            bytstr = pickle.loads(picstr)
            return bytstr.decode(self._encoding, self._errors)

    def __getitem__(self, i):
        return self._get()[i]

    def __len__(self):
        return len(self._get())

    def __str__(self):
        return self._get()

    def __iadd__(self, other):
        redis = _acquire()
        redis.append(self._rediskey, other)
        return self

    def __add__(self, other):
        return other + str(self)

    def __radd__(self, other):
        return self + other
