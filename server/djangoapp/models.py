from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.TextField()
    description = models.TextField() 

    def __str__(self):
        return self.name + "," + sel.description


class CarModel(models.Model):
    truck = 'truck'
    sedan = 'sedan'
    suv = 'suv'
    type_choices= [
        (truck, 'Truck'),
        (sedan, 'Sedan'),
        (suv, 'SUV'),
    ]
    carmodel = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.TextField()
    type = models.CharField(max_length=15, choices=type_choices)
    year = models.DateField()

    def __str__(self):
        return str(self.year) +"/"+ self.name +"/"+ self.type


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:

    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.id = id


    def __str__(self):
        return self.dealership + ":" + self.review
