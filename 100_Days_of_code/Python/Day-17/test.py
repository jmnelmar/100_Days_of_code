from coffee_maker import CoffeeMaker
from menu_item import MenuItem

menuItem = MenuItem( name="latte",water=100,milk=0,coffee=24,cost=2.5 )

cm = CoffeeMaker()
cm.report()

print(cm.is_resource_sufficient(menuItem))

cm.make_coffee(menuItem)
cm.report()