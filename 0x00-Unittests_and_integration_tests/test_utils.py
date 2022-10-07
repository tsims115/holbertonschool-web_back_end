#!/usr/bin/env python3
"""Test the utilities
"""
import inspect
import pep8
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """Test the access map utility"""

    @parameterized.expand([
        ({'a': 1}, ('a'), 1),
        ({'a': {'b': 2}}, ('a'), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expect):
        """Tests the access nested map function"""
        self.assertEqual(access_nested_map(nested_map, path), expect)
