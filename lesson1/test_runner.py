import unittest

from lesson1.main import Tester

tester = unittest.TestLoader().loadTestsFromTestCase(Tester)
suite = unittest.TestSuite([tester])
unittest.TextTestRunner(verbosity=2).run(suite)