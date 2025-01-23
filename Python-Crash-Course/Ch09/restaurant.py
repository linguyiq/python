class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("My restaurant name is " + self.restaurant_name.title())
        print("My cuisine type is " + self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open today!")



restaurant = Restaurant('Big Bite', 'fast food')
restaurant.describe_restaurant()
restaurant.open_restaurant()