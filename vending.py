from collections import Counter
from dataclasses import dataclass
from decimal import Decimal
import typing

ProductName = typing.NewType('ProductName', str)
SlotCode = typing.NewType('SlotCode', str)
Assortment = typing.Dict[ProductName, 'Product']
Coins = typing.Counter[Decimal]
Menu = typing.Dict[ProductName, typing.Tuple[SlotCode, Decimal]]
Prod2Slot = {}


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
        count = 0
        valulist = list(products.values())
        print(products)
        for count_slot in range(0,machine.slots):
            for count_slot_depth in range(0,machine.slot_depth):
                print(count_slot, count_slot_depth)
                Prod2Slot[f'{valulist[count_slot].quantity}-{valulist[count_slot].name}'] = (count_slot, count_slot_depth)
                valulist[count_slot].quantity -= 1
                if valulist[count_slot].quantity < 0:
                    break
                print(Prod2Slot)
        # machine.slot_depth=machine.slot_depth-valulist[count].quantity
        print(1, valulist[2].name, valulist[2].price, machine.slot_depth)


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
    machine.load_products(products)
    # print(machine.slots, machine.slot_depth)
    print('_____________')

    # cena = products.p
    # Prod2Slot = {productName : (machine.slots, machine.slot_depth)}
    # print(1, products)
    # print(prodlist)
    # valulist[2].quantity=2
    # valulist[2].price = 2.50
    # machine.slot_depth=machine.slot_depth-5 operacje na slotach :)
    # print(valulist[2].name, valulist[2].price, machine.slots, machine.slot_depth) #cena konkretnego produktu
    # print('----------------')
    # print(Assortment)
    # print(products.values())
