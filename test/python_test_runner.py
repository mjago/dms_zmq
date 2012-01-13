import sys
sys.path.append("../test/")
import unittest
import test_git
import time

suite = unittest.TestLoader().loadTestsFromTestCase(test_git.TestGit)
log_file = 'log_file.txt'
f = open(log_file, "w")
#runner = unittest.TextTestRunner(f)
#    unittest.main(testRunner=runner)
unittest.TextTestRunner(verbosity=4, testRunner=runner).run(suite)
#unittest.main(testRunner=runner)
f.close()
#suite = unittest.TestLoader().loadTestsFromTestCase(test_git.TestGit)
#for t in suite:
#    log_file = 'log_file.txt'
#    f = open(log_file, "w")
#    runner = unittest.TextTestRunner(verbosity=3).run(t)
#    unittest.main(testRunner=runner)
#    f.close


