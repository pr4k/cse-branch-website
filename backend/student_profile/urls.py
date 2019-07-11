from django.urls import path,include
from student_profile import views

urlpatterns=[
    path('',views.allStudentssecondyear.as_view(),name="secondstudentpage"),
    path('thirdyear',views.allStudentsthirdyear.as_view(),name="thirdstudentpage"),
    path('upload/<code>/<email>',views.model_form_upload,name="upload"),
    path('email/',views.Email_checker,name="email"),
    
]