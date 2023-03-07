from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("detail/", views.DetailPage.as_view(), name="detail"),
    path("meetup-form/", views.FillForm.as_view(), name="form"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("register/", views.RegisterPageView.as_view(), name="register")
]
