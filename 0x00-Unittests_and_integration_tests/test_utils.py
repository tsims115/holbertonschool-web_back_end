#!/usr/bin/env python3
"""Test the utilities
"""
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Dict, Sequence, Any, Callable
from parameterized import parameterized


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

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expect):
        """Test for exception"""
        with self.assertRaises(KeyError):
            self.assertEqual(access_nested_map(nested_map, path), expect)


class TestGetJson(unittest.TestCase):
    """testing class"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, payload, test):
        """test get json"""
        test.return_value.json.return_value = payload
        self.assertEqual(get_json(test_url), payload)


class TestMemoize(unittest.TestCase):
    """testing class"""

    def test_memoize(self):
        """memoize"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as m:
            test_class = TestClass()
            test_class.a_property
            test_class.a_property
            m.asset_called_once()
