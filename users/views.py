from django.shortcuts import render
from django.views.generic import View
# Create your views here.

# def IndexView(request):
#     return render(request, "index.html")


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")
    

class DetailPage(View):
    def get(self, request):
        return render(request, "meet_detail.html")
    

class FillForm(View):
    def get(self, request):
        return render(request, "form.html")
    

class LoginPageView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
    

class RegisterPageView(View):
    def get(self, request):
        return render(request, 'accounts/registration.html')