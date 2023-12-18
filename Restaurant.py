class Restaurant:
    restuarants=[]
    def __init__(self, name):
        self._name= name
        Restaurant.restuarants.append(self)
    def restaurant_name(self):
        return self._name
    @classmethod
    def all(cls):
        return cls.restuarants
    def average_star_rating(self, reviews):
        return restaurant.reviews / len(reviews)
    def customer(self, customer):
        self.customer= customer
        return self.customer
    def reviews(self):
        return self._name
    
    
restaurant= Restaurant(name='La Bodega')
print(restaurant._name)
