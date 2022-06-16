from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

chose = Menu()
record = CoffeeMaker()
money_in_themachine = MoneyMachine()
record.report()
money_in_themachine.report()
is_on = True

while is_on:
  choice = chose.get_items()
  select = input(f"What would you like? {choice} :")
  if select == 'off':
    is_on = False
  elif select == 'report':
    record.report()
    money_in_themachine.report()
  else:
    drink = chose.find_drink(select)
    if record.is_resource_sufficient(drink) and money_in_themachine.make_payment(drink.cost):
      record.make_coffee(drink)
      
    
  
