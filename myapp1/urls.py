from django.contrib import admin
from django.urls import path
from myapp1 import views

urlpatterns = [
    # path('', views.test, name="test"),
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"), 
    # path('course/', views.course, name="course"), 
    # path('course/<courseId>/', views.courseDetails),
    # path('renderPage/', views.htmlRenderPage)  

    path('user-form/',views.userForm, name='userForm'),
]

