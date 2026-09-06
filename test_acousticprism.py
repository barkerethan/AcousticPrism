# test_acousticprism.py
"""
Tests for AcousticPrism module.
"""

import unittest
from acousticprism import AcousticPrism

class TestAcousticPrism(unittest.TestCase):
    """Test cases for AcousticPrism class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AcousticPrism()
        self.assertIsInstance(instance, AcousticPrism)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AcousticPrism()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
