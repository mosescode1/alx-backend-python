#!/usr/bin/env python3
"""Moduule Test Case"""
from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Testing Access Nested Map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Access map test case"""
        self.assertEqual(access_nested_map(
            nested_map=nested_map, path=path), expected)


if __name__ == "__main__":
    unittest.main()
