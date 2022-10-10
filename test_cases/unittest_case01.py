# coding = utf-8
import unittest


class Case01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("11111所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls):
        print("11111所有case执行之后的后置")

    def setUp(self):
        print("11111这个是case的前置条件")

    def tearDown(self):
        print("11111这个是case的后置调键\n")

    # @unittest.skip("不执行第一条")
    def testfirst01(self):
        print("11111这个第一条case")

    def testfirst02(self):
        print("11111这是第二条case")

    def testfirst03(self):
        print("11111这是第3条case")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Case01('testfirst02'))
    suite.addTest(Case01('testfirst01'))
    suite.addTest(Case01('testfirst03'))
    unittest.TextTestRunner().run(suite)
