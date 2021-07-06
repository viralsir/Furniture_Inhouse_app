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
    products=prodinward.objects.filter(is_biiled=False).all()
    iform=billform()
    form = inwardform()
    return render(request,"inward_purchase/add_bill.html",{
        "products":products,
        "form":form,
        "iform":iform

    })

def closewindow(request):
    return render(request,"inward_purchase/close_window.html")