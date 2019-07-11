from django.urls import path,include
from contact import views

urlpatterns=[
    path('',views.contactpage,name="contact"),
]