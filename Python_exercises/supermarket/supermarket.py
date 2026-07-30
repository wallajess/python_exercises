from dataclasses import dataclass


@dataclass
class Food:
    expiration_date: str


@dataclass
class NonFood:
    pass


Kind = Food | NonFood


@dataclass
class Stock:
    name: str
    units: int
    price_per_unit: int
    kind: Kind


def is_expired(item: Stock, date: str) -> bool:
    """Determines whether a perishable is expired."""
    match item.kind:
        case Food(expiration_date):
            if expiration_date < date:
                return True
    return False


def get_expired(in_stock: list, date: str) -> list:
    """Returns a list of all expired items."""
    expired = []
    for x in in_stock:
        if is_expired(x, date):
            expired += [x]
    return expired


def buy(stocks: Stock, num_units: int) -> int:
    """Reduces teh stocks by the number of units and returns the number of units sold.
    Stocks must never go below 0, so that if more units are requested than available,
    only as many units can be sold as are on stock."""
    units_sold = 0
    if num_units > stocks.units:
        num_units = stocks.units
    stocks.units -= num_units
    units_sold += num_units
    return units_sold