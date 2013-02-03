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

"""harpy_redis.py - implements control of the Redis backend."""


import redis

# Global redis connection.
__redis = None


def _acquire():
    '''Get the Redis connection. Raises ConnectionError if there is none.

    Note that this is for internal use, you shouldn't touch the Redis database
    directly when using Harpy.
    '''
    if __redis is None:
        raise ConnectionError("No initialized Redis connection.")
    else:
        return __redis


def initialize(host='localhost',
               port=6379,
               db=0,
               password=None,
               socket_timeout=None,
               connection_pool=None,
               charset='utf-8',
               errors='strict',
               decode_responses=False,
               unix_socket_path=None):
    '''Initialize the Redis backend. This takes the same arguments as
    redis.StrictRedis and has the same defaults.'''
    global __redis
    if __redis is not None:
        raise ConnectionError("A Redis connection already exists. Close it to "
                              "initialize a new one.")
    __redis = redis.StrictRedis(host, port, db, password, socket_timeout,
                                connection_pool, charset, errors, decode_responses,
                                unix_socket_path)


def close():
    '''"Close" the Redis connection.

    This makes it possible to initialize new a Redis connection.
    '''
    global __redis
    __redis = None
