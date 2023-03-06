from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("detail/", views.DetailPage.as_view(), name="detail")
]
