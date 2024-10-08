#!/usr/bin/env python3
"""Moduule Test Case"""
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({}, ('a',)),
        ({"a": 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test for Raised error"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """Testing the get json method"""
    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    @patch("utils.requests.get")
    def test_get_json(self,  url, payload, mock_get):
        """Test to return a mock request"""
        mock_res = Mock()
        mock_res.json.return_value = payload

        mock_get.return_value = mock_res
        # print(mock_get)
        # print(url)
        # print(payload)
        # print(mock_get.return_value)
        # mock_get.return_value = mock_res

        user_data = get_json(url)

        self.assertEqual(user_data, payload)


class TestMemoize(unittest.TestCase):
    """Testing for memorization"""
    class TestClass:
        """Test case for"""

        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    @patch.object(TestClass, "a_method")
    def test_memoize(self, mock_methd):
        """Function to test memonize"""

        mock = self.TestClass()
        # mock_methd.return_value = 42

        # First call to a_property should call a_method
        result1 = mock.a_property
        mock_methd.assert_called_once()

        # Second call to a_property should not call a_method again
        result2 = mock.a_property
        mock_methd.assert_called_once()  # Should still be called only once

        # # Ensure the property returns the correct value
        # self.assertEqual(result1, 42)
        # self.assertEqual(result2, 42)


if __name__ == "__main__":
    unittest.main()
