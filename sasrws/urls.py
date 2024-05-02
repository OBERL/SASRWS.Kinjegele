from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("loan",views.loan,name="loan"),
    path("base",views.base,name="base"),
    path("checkup",views.checkup,name="checkup"),
    path("analytics",views.analytics,name="analytics"),
    path("trend",views.trend,name="trend"),
    path("customers",views.customers,name="customers"),
]