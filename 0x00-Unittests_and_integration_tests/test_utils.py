#!/usr/bin/env python3
"""Test the utilities
"""
import inspect
import pep8
import unittest
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """Test the access map utility"""

    @parameterized.expand
    def test_access_nested_map(self):
        """Tests the accessnested map function"""
        self.assertEqual()
