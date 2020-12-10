from menu_item import MenuItem
class CoffeeMaker:

    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources"""
        for key in self.resources:
            if key != "coffee":
                print(f"{key}: {self.resources[key]}ml")
            else:
                print(f"{key}: {self.resources[key]}g")
    
    def is_resource_sufficient(self, drink):
        """Parameter drink: The MenuItem object to make."""
        """Return true when the drink order can be made False if ingredients are insufficient."""
        for ingredient in drink.ingredients:
            if drink.ingredients[ingredient] > self.resources[ingredient]:
                return False
        return True

    def make_coffee(self, order):
        """Parameter order: The MenuItem object to make."""
        """Deducts the required ingredients from the resources."""
        for key in self.resources:
            self.resources[key] -= order.ingredients[key]
        