class Resturants:
    """Resturants system
    """
    def __init__(self,restaurant_name,cuisine_type):
        self.resturant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(self.resturant_name)
        print(self.cuisine_type)
        
    def open_restaurant(self):
        print(f"{self.resturant_name} is open")
        
restaurant_one = Resturants("mc","fast food")

restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

resturant_two = Resturants("kudu","Classic")
resturant_two.describe_restaurant()
resturant_two.open_restaurant()