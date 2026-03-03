# test_minevault.py
"""
Tests for MineVault module.
"""

import unittest
from minevault import MineVault

class TestMineVault(unittest.TestCase):
    """Test cases for MineVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MineVault()
        self.assertIsInstance(instance, MineVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MineVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
