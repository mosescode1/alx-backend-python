#!/usr/bin/env python3
"""Module for testing client """
from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """Test case for github organization client"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_org):
        """Method ot test"""
        client = GithubOrgClient(org_name)
        mock_org.return_value = client.org
        self.assertEqual(client.org, mock_org.return_value)
        mock_org.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
