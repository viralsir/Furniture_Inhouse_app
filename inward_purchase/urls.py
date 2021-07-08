from django.urls import path
from .views import *

urlpatterns=[
    path("new/",NewInwardBill.as_view(),name="new-purchase"),
    path("closed/",closewindow,name="closed"),
    path("view/",ViewPurchaseBill.as_view(),name="view-purchase"),
    path("detail/<int:pk>",DetailPurchaseBill.as_view(),name="detail-purchase")
]