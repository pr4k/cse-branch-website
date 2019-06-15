from django.urls import path,include
from events import views

urlpatterns=[
    path('',views.eventspage.as_view(),name="index"),
]