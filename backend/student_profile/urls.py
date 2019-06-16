from django.urls import path,include
from student_profile import views

urlpatterns=[
    path('',views.allStudents.as_view(),name="index"),
    path('upload/',views.model_form_upload,name="upload"),
]