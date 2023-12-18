class Review:
    reviews=[]
    def __init__(self, customer, restuarant, rating):
        self._customer = customer
        self._restaurant = restuarant
        self.rating = rating
        Review.reviews.append(self)
    def rating(self):
        return self.rating
    def all(cls):
        return cls.reviews
    def customer(self):
        return self._customer
    def restaurant(self):
        return self._restaurant

first_rating= Review('Gabrielle', 'La Bodega', 10)
print(first_rating.rating)
