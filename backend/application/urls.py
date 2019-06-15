from django.urls import path,include
from application import views

urlpatterns=[
    path('cr_elections',views.crElections.as_view(),name="index"),
    path('mr_and_miss_cse',views.mrAndMissCse.as_view(),name="index")
]