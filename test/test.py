import unittest

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("start")

    @classmethod
    def tearDownClass(cls) -> None:
        print("end")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_abc(self):
        print("test")

    def test_upper(self):
        print("upper")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("isupper")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("split")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()