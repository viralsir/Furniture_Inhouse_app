from django.http import HttpResponseRedirect
from django.shortcuts import render
from prodinward.models import prodinward
from django import forms
from .models import inward_purchase
from django.views.generic import CreateView,ListView,DetailView,DeleteView


class NewInwardBill(CreateView):
    model = inward_purchase
    fields = ['date','total_amount','net_amount','gst','discount','due_amount']
    template_name = "inward_purchase/add_bill.html"
    success_url = '/inward_purchase/view'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = prodinward.objects.filter(billed=0).all()
        return context


    def form_valid(self, form):
        print("inside  form valid before save")
        self.object = form.save()
        print("inside  form valid")
        for product in prodinward.objects.filter(billed=0).all():
            self.object.products.add(product)
            product.billed=1;
            product.save()
        self.object.save()
        print("object is saved")
        return HttpResponseRedirect(self.get_success_url())


class ViewPurchaseBill(ListView):
    model = inward_purchase
    context_object_name = "bills"


class DetailPurchaseBill(DetailView):
    model = inward_purchase



# Create your views here.
# class billform(forms.ModelForm):
#
#     class Meta:
#         model=inward_purchase
#         fields='__all__'
#
# class inwardform(forms.ModelForm):
#
#     class Meta:
#         model=prodinward
#         fields='__all__'
#
# def new_bill(request):
#     products=prodinward.objects.filter(is_biiled=False).all()
#     iform=billform()
#     form = inwardform()
#     return render(request,"inward_purchase/add_bill.html",{
#         "products":products,
#         "form":form,
#         "iform":iform
#
#     })
#
def closewindow(request):
     return render(request,"inward_purchase/close_window.html")