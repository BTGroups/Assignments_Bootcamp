class Customer:
    def __init__(self, cid, name, from_place, to_place, amount):
        self.cid = cid
        self.name = name
        self.from_place = from_place
        self.to_place = to_place
        self.amount = amount
class Ship:
    def __init__(self, sid, name):
        self.sid = sid
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def total_amount(self):
        return sum(c.amount for c in self.customers)


class CruiseShip(Ship):
    pass


class CargoShip(Ship):
    pass
class MarineCompany:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

class MarineService:

    # 1. Total amount collected by the company
    @staticmethod
    def total_amount_collected(company):
        return sum(ship.total_amount() for ship in company.ships)

    # 2. Total amount for every ship
    @staticmethod
    def amount_per_ship(company):
        return {ship.name: ship.total_amount() for ship in company.ships}

    # 3. List all customer details for a particular cruise ship
    @staticmethod
    def customers_for_cruise_ship(ship):
        if isinstance(ship, CruiseShip):
            return [(c.name, c.from_place, c.to_place, c.amount) for c in ship.customers]
        return []
if __name__ == "__main__":

    company = MarineCompany("Oceanic Travels")

    cruise1 = CruiseShip(1, "Sea Queen")
    cruise2 = CruiseShip(2, "Blue Pearl")
    cargo1 = CargoShip(3, "Cargo Master")

    company.add_ship(cruise1)
    company.add_ship(cruise2)
    company.add_ship(cargo1)

    c1 = Customer(1, "Ravi", "Chennai", "Goa", 5000)
    c2 = Customer(2, "Anita", "Mumbai", "Cochin", 6500)
    c3 = Customer(3, "Kumar", "Delhi", "Dubai", 20000)
    c4 = Customer(4, "Logistics Ltd", "Chennai", "Singapore", 50000)

    cruise1.add_customer(c1)
    cruise1.add_customer(c2)
    cruise2.add_customer(c3)
    cargo1.add_customer(c4)

    print("Total Amount Collected:",
          MarineService.total_amount_collected(company))

    print("Amount Collected Per Ship:",
          MarineService.amount_per_ship(company))

    print("Customers for Cruise Ship 'Sea Queen':",
          MarineService.customers_for_cruise_ship(cruise1))
