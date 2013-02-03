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

import pickle
import abc

from ._redis import _acquire
from . import utils


class HarpyBase(metaclass=abc.ABCMeta):
    '''Abstract base class for all other Harpy classes.'''

    def __init__(self, rediskey, type_, value=None):
        self._rediskey = rediskey
        self._type = type_
        super().__init__()
        self._create(value)

    def _create(self, value=None):
        '''Check if a key exists, and if not, create it.

        If value is given, initialize it with the correct value.
        '''
        r = _acquire()
        with utils.lock(r, self._rediskey):
            t = r.type(self._rediskey)
            if t != self._type and t != b'none':
                raise TypeError("Key {0} has the wrong type. " +
                                "Got {1}, expected {2}.".format(
                                    self._rediskey,
                                    t,
                                    self._type))
            # set the key to indicate its existence
            r.set('harpy.' + self._rediskey, 1)
            if value is not None:
                self.set_value(value)

    @abc.abstractmethod
    def set_value(self, value):
        '''Set the contents of this key to a value. Must be implemented by
        child classes. value must be an instance of self._type.
        '''
        return NotImplemented
