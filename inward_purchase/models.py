from django.db import models
from datetime import  datetime
from prodinward.models import prodinward

# Create your models here.
class inward_purchase(models.Model):
    date=models.DateField(default=datetime.utcnow)
    products=models.ManyToManyField(prodinward,related_name='inward_purchase_bill')
    total_amount=models.IntegerField()
    gst=models.DecimalField(max_digits=9,decimal_places=2)
    discount=models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)
    net_amount=models.DecimalField(max_digits=9,decimal_places=2)
    due_amount=models.DecimalField(max_digits=9,decimal_places=2,blank=True,null=True)

    def __str__(self):
        return f"{self.id} - {self.date}"




