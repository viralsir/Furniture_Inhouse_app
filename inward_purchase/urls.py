from django.urls import path
from .views import *

urlpatterns=[
    path("new/",new_bill,name="new-purchase")
]