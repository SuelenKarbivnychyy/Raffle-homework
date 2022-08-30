"""Read customer data from file and run a raffle."""

# from random import choice
import random


class Customer:
    """A customer at Ubermelon."""

    def __init__(self, name, email, street, city, zipcode):
        self.name = name
        self.email = email
        self.street = street
        self.city = city
        self.zipcode = zipcode


