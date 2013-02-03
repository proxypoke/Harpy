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

from ._redis import _acquire as acquire
from ._redis import initialize

from .string import HarpyString as String
