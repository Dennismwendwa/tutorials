from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return (f"Item name: {self.name}, price: {self.price}, "
                f"quantity: {self.quantity}")
