class Customer:
    customers= []


    def __init__(self, given_name, last_name):
        self.given_name= given_name
        self.last_name = last_name
        Customer.customers.append(self)
    def given_name(self):
        return self.given_name
    def last_name(self):
        return self.last_name
    def full_name(self):
        return (f'{self.given_name}') +  (f'{self.last_name}')
    def all_names(self):
        return self.Customer 
    
    @classmethod
    def all(cls):
        return cls.customers
    def num_reviews(cls, self):
        return cls.customers()
    def find_by_name(cls, name):
        return cls.name
    def find_all_by_given_name(cls, name):
        return cls._name

customer_one = Customer('George', 'Washington')
print(customer_one.full_name())
