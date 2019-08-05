"""Tests"""
from unittest import TestCase
from app import app


class TestSoma(TestCase):
    """TestSoma"""
    def test_get_soma(self):
        """Test soma"""
        response = app.get_soma(1, 2)
        print(response)
        self.assertTrue(response, 3)
