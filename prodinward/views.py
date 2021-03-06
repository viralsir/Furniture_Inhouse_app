from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
# Create your views here.
class Newproduct(CreateView):
    model = prodinward
    fields = ['prod','quantity','rate','price','discount','gst']


class Viewproduct(ListView):
    model = prodinward
    context_object_name = 'prod'


class Updateproduct(UpdateView):
    model = prodinward
    fields = '__all__'



class Deleteproduct(DeleteView):
    model = prodinward
    success_url = '/inward_purchase/closed'