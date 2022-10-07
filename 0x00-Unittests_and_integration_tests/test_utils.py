#!/usr/bin/env python3
"""Test the utilities
"""
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from parameterized import parameterized
from typing import Mapping, Dict, Sequence, Any, Callable

class TestAccessNestedMap(unittest.TestCase):
    """testing class"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expect: Any
                               ):
        """test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expect)
