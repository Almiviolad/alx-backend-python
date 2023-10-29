#!/usr/bin/env python3
"""Familiarize yourself with the utils.access_nested_map function
and understand its purpose. Play with it in the Python
console to make sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method
to test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand
to test the function for following inputs:"""
import unittest
from parameterized import parameterized
from utils import (get_json, access_nested_map)
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,)
from unittest.mock import patch, Mock
import re
import requests


class TestAccessNestedMap(unittest.TestCase):
    """Class to test AccessNestedMap function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence,
                               expected: Any):
        """method to test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence):
        """test that a KeyError is raised for wrong inputs"""
        pattern = "KeyError: '.*'"
        with self.assertRaises(KeyError) as c:
            access_nested_map(nested_map, path)
            msg = str(c.exception)
            self.assertTrue(re.match(pattern, msg))


class TestGetJson(unittest.TestCase):
    """class to test gwt jsn function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """test that utils.get_json returns the expected result."""
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mock_get.assert_called_once_with(test_url)
