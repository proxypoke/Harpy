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

from contextlib import contextmanager


@contextmanager
def lock(redis_instance, key):
    '''Lock a key for the duration of change.'''
    keylock = key + ".lock"
    spinlock = redis_instance.getset(keylock, 1)
    while spinlock:
        spinlock = redis_instance.getset(keylock, 1)
    yield
    redis_instance.delete(keylock)
