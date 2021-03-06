#!/usr/bin/python
# -*- coding: utf-8 -*-
# moehime / saimoe / exception classes
#
# Copyright (C) 2012 Wang Xuerui <idontknw.wang@gmail.com>
#
# This file is part of moehime.
#
# moehime is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# moehime is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
# License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with moehime.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals, division


class ThreadInfoError(ValueError):
    pass


class ThreadBadTitleError(ThreadInfoError):
    pass


class PostError(ValueError):
    pass


class PostBadHeaderError(PostError):
    pass


class PostOutOfRangeError(PostError):
    pass


class MalformedCodeError(ValueError):
    pass


# vim:ai:et:ts=4:sw=4:sts=4:ff=unix:fenc=utf-8:
