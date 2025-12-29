from typing import List, Tuple, Dict, Set, Union
class Customer:
    _cid_counter = 0
    def __init__(self, name : str, from_place : str , to_place : str , amount : int):
        if not name:
            raise ValueError("Customer name is required")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.cid =Customer._cid_counter 
        Customer._cid_counter += 1
        self.name = name
        self.from_place = from_place
        self.to_place = to_place
        self.amount = amount
    def __repr__(self):
        return f"Customer({self.name}, {self.from_place} -> {self.to_place}, {self.amount})"
    

class Ship:
    def __init__(self, sid: int, name : str ):
        if not name:
            raise ValueError("Ship name is required")
        self.sid = sid
        self.name = name
        self.customers : List[Customer] = []

    def add_customer(self, customer:Customer) -> None:
        if not isinstance(customer, Customer):
            raise TypeError("Expected customer instance")
        self.customers.append(customer)

    def total_amount(self) -> int:
        return sum(c.amount for c in self.customers)

    def __eq__(self, value):
        return isinstance(value, Ship) and self.sid == value.sid
    def __hash__(self):
        return hash(self.sid)
    def __repr__(self):
        return f"Ship({self.name}, Customers={len(self.customers)})"


class CruiseShip(Ship):
    """Cruise Ships can carry passengers"""
    pass


class CargoShip(Ship):
    """Cargo ships cannot carry passengers"""
    def add_customer(self, customer : Customer) -> None:
        raise ValueError("Cargo ships cannot have passengers")

class MarineCompany:
    def __init__(self, name):
        if not name:
            raise ValueError("Company name is required")

        self.name = name
        self.ships : Set[Union[CruiseShip, CargoShip]] = set()

    def add_ship(self, ship : Union[CruiseShip, CargoShip]) -> None:
        if not isinstance(ship, Ship):
            raise TypeError("Expected cruiseship or Cargoship instance")
        if ship in self.ships:
            raise ValueError(f"ship {ship.name} already exists in company")
        self.ships.add(ship)
    def __repr__(self):
        return f"MarineCompany({self.name}, Ships={len(self.ships)})"





class MarineService:

    @staticmethod
    def total_amount_collected(company: MarineCompany) -> int:
        return sum(ship.total_amount() for ship in company.ships)

    @staticmethod
    def amount_per_ship(company: MarineCompany) -> Dict[str, int]:
        return {ship.name: ship.total_amount() for ship in company.ships}

    @staticmethod
    def customers_for_cruise_ship(ship: CruiseShip) -> List[Tuple[str, str, str, int]]:
        if not isinstance(ship, CruiseShip):
            raise TypeError("Expected CruiseShip instance")
        return [(c.name, c.from_place, c.to_place, c.amount) for c in ship.customers]


def create_sample_company() -> MarineCompany:
    company = MarineCompany("Oceanic Travels")

    cruise1 = CruiseShip(1, "Sea Queen")
    cruise2 = CruiseShip(2, "Blue Pearl")
    cargo1 = CargoShip(3, "Cargo Master")

    company.add_ship(cruise1)
    company.add_ship(cruise2)
    company.add_ship(cargo1)

    cruise1.add_customer(Customer("Ravi", "Chennai", "Goa", 5000))
    cruise1.add_customer(Customer("Anita", "Mumbai", "Cochin", 6500))
    cruise2.add_customer(Customer("Kumar", "Delhi", "Dubai", 20000))

    return company


if __name__ == "__main__":
    company = create_sample_company()

    print("Total Amount Collected:", MarineService.total_amount_collected(company))
    print("Amount Collected Per Ship:", MarineService.amount_per_ship(company))

    cruise_ship = next(s for s in company.ships if isinstance(s, CruiseShip))
    print("Customers for Cruise Ship 'Sea Queen':",
          MarineService.customers_for_cruise_ship(cruise_ship))
