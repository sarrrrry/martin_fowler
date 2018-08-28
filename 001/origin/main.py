class Movie:
    CHILDREN = 2
    REGULAR = 0
    NEW_RELEASE = 1

    def __init__(self, title: str, price_code: int):
        self._title = title
        self._price_code = price_code

    def get_price_code(self) -> int:
        return self._price_code

    def set_priceCode(self, price_code):
        self._price_code = price_code

    def get_title(self) -> str:
        return self._title


class Rental:
    def __init__(self, movie: Movie, days_rented: int):
        self._movie = movie
        self._days_rented = days_rented

    def get_days_rented(self) -> int:
        return self._days_rented

    def get_movie(self) -> Movie:
        return self._movie

class Customer:
    def __init__(self, name: str):
        self._name: str = name
        self._rentals = []

    def add_rental(self, rental: Rental):
        self._rentals.append(rental)

    def get_name(self) -> str:
        return self._name

    def statement(self) -> str:
        total_amount: float = 0
        frequent_renter_points: int = 0
        rentals = self._rentals  # javaだと.elementsになるところ

        result = "Rental Record for " + self.get_name() + "\n"
        for each in rentals:
            this_amount = 0

            # 一行ごとに金額を計算
            price_code = each.get_movie().get_price_code()
            if price_code == Movie.REGULAR:
                this_amount += 2
                if each.get_days_rented() > 2:
                    this_amount += (each.get_days_rented() - 2) * 1.5

            elif price_code == Movie.NEW_RELEASE:
                this_amount += each.get_days_rented() * 3

            elif price_code == Movie.CHILDREN:
                this_amount += 1.5
                if each.get_days_rented() > 3:
                    this_amount += (each.get_days_rented - 3) * 1.5

            # レンタルポイントを加算
            frequent_renter_points += 1

            # 新作を２日以上借りた場合はボーナスポイント
            if (each.get_movie().get_price_code() == Movie.NEW_RELEASE) and (each.get_days_rented() > 1):
                frequent_renter_points += 1

            result += "\t" + each.get_movie().get_title() + "\t" \
                      + str(this_amount) + "\n"
            total_amount += this_amount


        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"
        return result



if __name__ == "__main__":
    summerwars = Movie(title="summerwars", price_code=1)
    rental = Rental(movie=summerwars, days_rented=3)
    sato = Customer(name="sato")
    sato.add_rental(rental)
    statement = sato.statement()

    print(statement)
