from django.db import models
from django.urls import reverse
from product.models import product
# Create your models here.
class prodinward(models.Model):
    prod = models.ForeignKey(product, on_delete=models.CASCADE, related_name="product")
    quantity = models.CharField(max_length=100)
    rate = models.FloatField(max_length=100)
    price = models.FloatField(max_length=100)
    discount = models.FloatField(max_length=100, blank=True, null=True)
    gst = models.FloatField(max_length=100, blank=True, null=True)
    is_biiled=models.BooleanField(default=False)
    billed=models.IntegerField(default=0)

    def __str__(self):
        return f"{self.price}"

    def get_absolute_url(self):
        return reverse("closed")