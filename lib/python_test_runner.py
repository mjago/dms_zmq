import sys
sys.path.append("../lib/")
import unittest
import ../test/test_git

suite = unittest.TestLoader().loadTestsFromTestCase(test_git.TestGit)
for t in suite:
    unittest.TextTestRunner(verbosity=3).run(t)
