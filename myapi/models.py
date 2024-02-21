from django.db import models


class Invoice(models.Model):
    date = models.DateField(auto_now=True)
    customer_name = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name
    

class InvoiceDetails(models.Model):
    invoice = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.FloatField()
    price = models.FloatField()

    def save(self, *args, **kwargs):
        # Calculate the price based on quantity and unit_price
        self.price = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return self.description
