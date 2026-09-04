# test_irisember.py
"""
Tests for IrisEmber module.
"""

import unittest
from irisember import IrisEmber

class TestIrisEmber(unittest.TestCase):
    """Test cases for IrisEmber class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = IrisEmber()
        self.assertIsInstance(instance, IrisEmber)
        
    def test_run_method(self):
        """Test the run method."""
        instance = IrisEmber()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
