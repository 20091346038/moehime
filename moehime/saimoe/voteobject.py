#!/usr/bin/python
# -*- coding: utf-8 -*-
# moehime / saimoe / vote object
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


class VoteEntry(object):
    def __init__(self, author, ctime, text):
        self.author = author
        self.ctime = ctime
        self.full_text = text
        self.text = ''

        self.code = None
        self.is_valid = True
        self.charas = []
        self.annotations = {}


# vim:ai:et:ts=4:sw=4:sts=4:ff=unix:fenc=utf-8:
