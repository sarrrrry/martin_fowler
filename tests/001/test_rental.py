import unittest
from chapter001.refactored.refactored import Movie, MoviePriceCode, Rental


class TestRental(unittest.TestCase):
    def test_getter_is_correct(self):
        title = "summerwars"
        price_code = MoviePriceCode.REGULAR
        days_rented = 3

        summerwars = Movie(title=title, price_code=price_code)
        rental = Rental(movie=summerwars, days_rented=days_rented)

        self.assertEqual(rental.movie, summerwars)
        self.assertEqual(rental.days_rented, days_rented)


if __name__ == "__main__":
    unittest.main()

