import MenuItme from menu_item

class Manu:
    """Models the Menu with drinks"""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte",water=200, milk=150,coffee=24, cost=2.5),
            MenuItem(name="espresso",water=50, milk=0,coffee=18, cost=1.5),
            MenuItem(name="cappucino",water=250, milk=50,coffee=24, cost=3)
        ] 
    
    def get_items(self):
        """Returns all the names of the available menu itmes"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options
    
    def find_drink(self, order_name):
       """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
       for item in self.menu:
           if order_name == item.name:
               return item
       print("Sorry that item is not available")