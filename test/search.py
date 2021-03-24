#被测方法
import  unittest
class Search:

    def search_fun(self):
        print("search")
        return True

class SearchClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setup")
        cls.search=Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown")

    def test_search1(self):
        print("test_search1")
        #search=Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print("test_search2")
        #search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("test_search3")
        #search = Search()
        assert True == self.search.search_fun()

if __name__=='__main__':
    suite1=unittest.TestLoader().loadTestsFromTestCase(SearchClass)
    suite=unittest.TestSuite(suite1)
    unittest.TextTestRunner().run(suite)