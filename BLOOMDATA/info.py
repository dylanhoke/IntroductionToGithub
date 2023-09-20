# import pytest
# import random
# class Product:
#     def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=random.randrange(1000000, 9999999)):
#         self.name = name
#         self.price = price
#         self.weight = weight
#         self.flammability = flammability
#         self.identifier = identifier
#     def stealability(self):
#         ratio = self.price / self.weight
#         if ratio < 0.5:
#             return "Nor so stealable..."
#         elif ratio < 1.0:
#             return "Kinda stealable"
#         else: 
#             return "Very stealable!"