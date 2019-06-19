from django.urls import path,include
from student_profile import views

urlpatterns=[
    path('',views.allStudents.as_view(),name="index"),
    path('upload/<code>/<email>',views.model_form_upload,name="upload"),
    path('email/',views.Email_checker,name="email"),
    
]