import unittest
from chapter001.refactored.refactored import Movie, MoviePriceCode, Rental, Customer

class TestCustomer(unittest.TestCase):
    def test_rental_is_added_correctly(self):
        title = "summerwars"
        price_code = MoviePriceCode.REGULAR
        summerwars = Movie(title=title, price_code=price_code)
        days_rented = 3
        rental = Rental(movie=summerwars, days_rented=days_rented)

        name = "sato"
        sato = Customer(name)
        sato.add_rental(rental)

        msg = "Rental Record for sato\n\tsummerwars\t3.5\nAmount owed is 3.5\nYou earned 1 frequent renter points"
        self.assertEqual(msg, sato.statement())


if __name__ == "__main__":
    unittest.main()
