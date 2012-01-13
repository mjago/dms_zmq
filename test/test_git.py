import sys
sys.path.append("../lib/")
import unittest
import git

class TestGit(unittest.TestCase):

    def setUp(self):
        pass

    def test_gitInitCmd_causes_exception_when_directory_does_not_exist(self):
        self.assertRaises(Exception, git.gitInitCmd, 'doesnt-exist')

    def test_gitInitCmd_returns_correct_git_command(self):
        self.assertEqual('CD ../test/test_project; git init',
                         git.gitInitCmd('../test/test_project'))

    def test_gitInitCmd_causes_exception_when_passed_number(self):
        self.assertRaises(Exception, git.gitInitCmd, 2)

    def test_gitInitCmd_causes_exception_when_passed_empty_string(self):
        self.assertRaises(Exception, git.gitInitCmd, '')

    def test_gitInitCmd_causes_exception_when_git_directory_already_exists(self):
        self.assertRaises(Exception, git.gitInitCmd, "test_project/git_exists")

    def test_gitCheckHasRepo(self):
        self.assertFalse(git.gitCheckHasRepo("test_project/git_doesnt_exist"))

    def test_gitCheckHasRepo(self):
        self.assertTrue(git.gitCheckHasRepo("test_project/git_exists"))

    def test_gitCheckDirectoryString_returns_False_when_not_passed_string(self):
        self.assertFalse(git.gitCheckDirectoryString( 123 ))

    def test_gitCheckDirectoryString_returns_False_when_passed_empty_string(self):
        self.assertFalse(git.gitCheckDirectoryString( "" ))

    def test_gitCheckDirectoryString_returns_True_when_passed_string_that_could_be_directory(self):
        self.assertTrue(git.gitCheckDirectoryString( "abc" ))

    def test_gitAddCmd_causes_exception_when_project_doesnt_contain_repo(self):
        self.assertRaises(Exception,
                          git.gitAddCmd,
                          "test_project/git_exists/lib/test.py", "lib/dummy.py")

    def test_gitAddCmd_causes_exception_when_passed_number_as_parameter(self):
        self.assertRaises(Exception,
                          git.gitAddCmd, 123, "test_project/git_exists/lib/test.py")
        self.assertRaises(Exception,
                          git.gitAddCmd, "test_project/git_exists/", 456)

    def test_gitAddCmd_causes_exception_when_passed_empty_string(self):
        self.assertRaises(Exception,
                          git.gitAddCmd, '', 'sss')

    def test_gitAddCmd_causes_exception_when_passed_empty_string(self):
        self.assertRaises(Exception,
                          git.gitAddCmd,
                          'test_project/git_exists/', '')

    def test_gitAddCmd_causes_exception_when_project_directory_doesnt_exist(self):
        self.assertRaises(Exception,
                          git.gitAddCmd,
                          'test_project/rubbish', 'lib/dummy.py')

    def test_gitAddCmd_causes_exception_when_file_to_add_doesnt_exist(self):
        self.assertRaises(Exception,
                          git.gitAddCmd,
                          'test_project/git_exists/', 'lib/dummy.py')

    def test_gitAddCmd_returns_correct_git_command(self):
        self.assertEqual( 'CD test_project/git_exists/; git add lib/test.py',
                          git.gitAddCmd('test_project/git_exists/',
                                        'lib/test.py'))














#    def test_numbers_equality(self):
#        self.assertEqual(2, 3 - 1)
#
#    def test_numbers_inequality(self):
#        self.assertNotEqual(2, 3 + 1)
#
#    def test_string_equality(self):
#        self.assertEqual("2", "2")
#
#    def test_shuffle(self):
#        # make sure the shuffled sequence does not lose any elements
#        random.shuffle(self.seq)
#        self.seq.sort()
#        self.assertEqual(self.seq, range(10))
#
#        # should raise an exception for an immutable sequence
#        self.assertRaises(TypeError, random.shuffle, (1,2,3))
#
#    def test_choice(self):
#        element = random.choice(self.seq)
#        self.assertTrue(element in self.seq)
#
#    def test_sample(self):
#        for element in random.sample(self.seq, 5):
#            self.assertTrue(element in self.seq)
#
#    def test_fib_returns_correct_answer(self):
#        self.assertEqual(dms.fib(1), [])
#        self.assertEqual(dms.fib(2), [1, 1])
#        self.assertEqual(dms.fib(3), [1, 1, 2])
#        self.assertEqual(dms.fib(4), [1, 1, 2, 3])
#        self.assertEqual(dms.fib(5), [1, 1, 2, 3])
#        self.assertEqual(dms.fib(6), [1, 1, 2, 3, 5])
#        self.assertEqual(dms.fib(7), [1, 1, 2, 3, 5])
#        self.assertEqual(dms.fib(8), [1, 1, 2, 3, 5])
#        self.assertEqual(dms.fib(9), [1, 1, 2, 3, 5, 8])
#        self.assertEqual(dms.fib(0), [])
#        self.assertEqual(dms.fib(-1), [])
#
#    def test_return_twice(self):
#        self.assertEqual(2, dms.return_double(1))
#        self.assertEqual(4, dms.return_double(2))
#        self.assertEqual(-40, dms.return_double(-20))
#
#    def test_factorial(self):
#        self.assertEqual(1, dms.factorial(0))
#        self.assertEqual(1, dms.factorial(1))
#        self.assertEqual(2, dms.factorial(2))
#        self.assertEqual(6, dms.factorial(3))
#        self.assertEqual(24, dms.factorial(4))
#        self.assertEqual(120, dms.factorial(5))
#        self.assertEqual(720, dms.factorial(6))

if __name__ == '__main__':
#    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    unittest.TextTestRunner(verbosity=2).run(suite)

