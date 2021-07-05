from django.shortcuts import render
from prodinward.models import prodinward
from django import forms
from .models import inward_purchase
# Create your views here.
class billform(forms.ModelForm):

    class Meta:
        model=inward_purchase
        fields='__all__'

class inwardform(forms.ModelForm):

    class Meta:
        model=prodinward
        fields='__all__'

def new_bill(request):
    products=prodinward.objects.all()
    form=billform()
    iform = inwardform()
    return render(request,"inward_purchase/add_bill.html",{
        "products":products,
        "form":form,
        "iform":iform

    })