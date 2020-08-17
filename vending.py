from collections import Counter
from dataclasses import dataclass
from decimal import Decimal
import typing

ProductName = typing.NewType('ProductName', str)
SlotCode = typing.NewType('SlotCode', str)
Assortment = typing.Dict[ProductName, 'Product']
Coins = typing.Counter[Decimal]
Menu = typing.Dict[ProductName, typing.Tuple[SlotCode, Decimal]]
Prod2Slot = typing.Dict[ProductName, typing.Tuple['slots', 'slot_depth']]


class MachineOverloadedException(Exception):
    pass


@dataclass
class Product:
    name: ProductName
    quantity: int
    price: Decimal


class Machine:
    def __init__(self, slots: int, slot_depth: int) -> None:
        self.slots = slots
        self.slot_depth = slot_depth
        pass

    def load_products(self, assortment: Assortment) -> None:
        pass

    def load_coins(self, coins: Coins) -> None:
        pass

    def get_available_products(self) -> Menu:
        pass

    def choose_product(self, product_code: SlotCode, money: Coins) -> typing.Tuple[typing.Optional[Product], typing.Optional[Coins]]:
        pass

    def get_balance(self) -> Decimal:
        pass

    def cash_out(self) -> Coins:
        pass


if __name__ == '__main__':
    machine = Machine(slots=6, slot_depth=10)
    products = {
        ProductName("coca-cola"): Product(name=ProductName("coca-cola"), quantity=7, price=Decimal('2.1')),
        ProductName("mars"): Product(name=ProductName("mars"), quantity=5, price=Decimal('1.9')),
        ProductName("orbit"): Product(name=ProductName("orbit"), quantity=6, price=Decimal('2.3')),
    }

    # print(machine.slots, machine.slot_depth)

    print(products.keys())
    Prod2Slot = {'productName': (machine.slots, machine.slot_depth)}
    print(Prod2Slot)
