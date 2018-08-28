from abc import ABCMeta, abstractmethod

from enum import IntEnum

class Price(metaclass=ABCMeta):
    @abstractmethod
    def get_price_code(self):
        raise NotImplementedError

    def get_charge(self, days_rented: int) -> float:
        pass

    def get_frequent_renter_points(self, days_rented: int) -> int:
        return 1


class ChildrenPrice(Price):
    def get_price_code(self):
        return MoviePriceCode.CHILDREN

    def get_charge(self, days_rented):
        result = 1.5
        if days_rented > 3:
            result += (days_rented - 3) * 1.5
        return result


class NewReleasePrice(Price):
    def get_price_code(self):
        return MoviePriceCode.NEW_RELEASE

    def get_charge(self, days_rented):
        return days_rented * 3

    def get_frequent_renter_points(self, days_rented: int):
        return 2 if days_rented > 1 else 1


class RegularPrice(Price):
    def get_price_code(self):
        return MoviePriceCode.REGULAR

    def get_charge(self, days_rented):
        result = 2
        if days_rented > 2:
            result += (days_rented - 2) * 1.5
        return result


class MoviePriceCode(IntEnum):
    CHILDREN = 2
    REGULAR = 0
    NEW_RELEASE = 1


class Movie:
    def __init__(self, title: str, price_code: int):
        self._title = title
        self.price_code = price_code

    @property
    def price_code(self) -> int:
        return self._price.get_price_code()

    @property
    def title(self) -> str:
        return self._title

    @price_code.setter
    def price_code(self, code):
        if code==MoviePriceCode.REGULAR:
            self._price = RegularPrice()
        elif code==MoviePriceCode.CHILDREN:
            self._price = ChildrenPrice()
        elif code==MoviePriceCode.NEW_RELEASE:
            self._price = NewReleasePrice()
        else:
            raise ValueError()

    def charge(self, days_rented) -> float:
        return self._price.get_charge(days_rented=days_rented)

    def frequent_renter_points(self, days_rented) -> int:
        return self._price.get_frequent_renter_points(days_rented=days_rented)


class Rental:
    def __init__(self, movie: Movie, days_rented: int):
        self._movie = movie
        self._days_rented = days_rented

    @property
    def days_rented(self):
        return self._days_rented

    @property
    def movie(self):
        return self._movie

    @property
    def charge(self) -> float:
        return self._movie.charge(self._days_rented)

    @property
    def frequent_renter_points(self):
        # 新作を２日以上借りた場合はボーナスポイント
        return self._movie.frequent_renter_points(self._days_rented)


class Customer:
    def __init__(self, name: str):
        self._name: str = name
        self._rentals = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def total_charge(self):
        result = 0
        for each in self._rentals:
            result += each.charge
        return result

    @property
    def total_frequent_renter_points(self):
        result = 0
        for each in self._rentals:
            result += each.frequent_renter_points
        return result

    def add_rental(self, rental: Rental):
        self._rentals.append(rental)

    def statement(self) -> str:
        result = f"Rental Record for {self.name}\n"
        for rental in self._rentals:
            result += f"\t{rental.movie.title}\t{str(rental.charge)}\n"

        result += f"Amount owed is {self.total_charge}\n"
        result += f"You earned {self.total_frequent_renter_points} frequent renter points"
        return result


if __name__ == "__main__":
    summerwars = Movie(title="summerwars", price_code=1)
    rental = Rental(movie=summerwars, days_rented=3)
    sato = Customer(name="sato")
    sato.add_rental(rental)
    statement = sato.statement()

    print(statement)
