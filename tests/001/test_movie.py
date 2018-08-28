import unittest

from chapter001.refactored.refactored import Movie, MoviePriceCode


class TestMovie(unittest.TestCase):

    def test_getter_is_correct(self):
        title = "summerwars"
        price_code = MoviePriceCode.REGULAR
        summerwars = Movie(title=title, price_code=price_code)
        self.assertEqual(title, summerwars.title)
        self.assertEqual(price_code, summerwars.price_code)

        title = "hogehoge"
        price_code = MoviePriceCode.NEW_RELEASE
        summerwars = Movie(title=title, price_code=price_code)
        self.assertEqual(title, summerwars.title)
        self.assertEqual(price_code, summerwars.price_code)

    def test_setter_is_correct(self):
        title = "summerwars"
        old_price_code = MoviePriceCode.REGULAR
        summerwars = Movie(title=title, price_code=old_price_code)
        self.assertEqual(old_price_code, summerwars.price_code)

        new_price_code = MoviePriceCode.CHILDREN
        summerwars.price_code = new_price_code
        self.assertEqual(new_price_code, summerwars.price_code)

if __name__ == "__main__":
    unittest.main()