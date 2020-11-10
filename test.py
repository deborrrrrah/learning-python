import unittest
from classes.tests import TestPrice

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestPrice))
    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)