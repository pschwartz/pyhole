#   Copyright 2011 Josh Kearney
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""Pyhole Config Unit Tests"""

import unittest

from pyhole import config


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = config.Config("../pyhole.cfg", "Pyhole")

    def test_sections(self):
        sections = self.config.sections()
        self.assertTrue(isinstance(sections, list))
        self.assertTrue(len(sections) > 1)

    def test_get(self):
        test_int = self.config.get("reconnect_delay", "int")
        self.assertTrue(isinstance(test_int, int))

    def test_get_2(self):
        test_bool = self.config.get("debug", "bool")
        self.assertTrue(isinstance(test_bool, bool))

    def test_get_3(self):
        test_list = self.config.get("admins", "list")
        self.assertTrue(isinstance(test_list, list))

    def test_get_4(self):
        test_str = self.config.get("cache")
        self.assertTrue(isinstance(test_str, str))