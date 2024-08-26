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

    def test_memonize(self):
        """Testing  for memonize"""

        class TestClass:
            """Test case for memonize"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
