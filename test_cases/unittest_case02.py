# coding=utf-8
import unittest


class FirstCase02(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("22222所有case执行之前的前置")

    @classmethod
    def tearDownClass(cls):
        print("22222所有case执行之后的后置")

    def setUp(self):
        print("22222这个是case的前置条件")

    def tearDown(self):
        print("22222这个是case的后置调键\n")

    # @unittest.skip("不执行第一条")
    def testfirst001(self):
        print("22222这个第0一条case")

    def testfirst002(self):
        print("22222这是第0二条case")

    def testfirst003(self):
        print("22222这是第003条case")


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('testfirst002'))
    suite.addTest(FirstCase02('testfirst001'))
    suite.addTest(FirstCase02('testfirst003'))
    unittest.TextTestRunner().run(suite)
