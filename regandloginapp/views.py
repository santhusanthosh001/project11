from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Reg
from .forms import Regform,loginform
class Home(View):
    def get(self,request):
        return render(request,template_name="home.html")
class LoginInput(View):
    def get(self,request):
        con_dic={"loginform":loginform()}
        return render(request,template_name="login.html",context=con_dic)
class RegInput(View):
    def get(selfself,request):
        con_dic={"regform": Regform()}
        return render(request,template_name="reginput.html",context=con_dic)
class RegView(View):
    def post(self,request):
        ref =Regform(request.POST)
        if ref.is_valid():
            r1=Reg(First_name=ref.cleaned_data["First_name"],
                   Last_name=ref.cleaned_data["Last_name"],
                   user_name=ref.cleaned_data["user_name"],
                   password=ref.cleaned_data["password"],
                   cpassword=ref.cleaned_data["cpassword"],
                   emailid=ref.cleaned_data["emailid"],
                   mobilenumber=ref.cleaned_data["mobilenumber"])
            r1.save()
        return HttpResponse("""<html> <body g bgcolor="teal"> <center> <h1> registration completed </h1><h1>thank you</h1> </center> </body></html>""")
class Loginview(View):
    def post(self,request):
        lf=loginform(request.POST)
        if lf.is_valid():
            res=Reg.objects.filter(user_name=lf.cleaned_data["user_name"],
                                   password=lf.cleaned_data["password"])
            if res:
                return HttpResponse("""<html> <body bgcolor="seagreen"> <center> <h1> login susccess </h1><h1>thank you</h1> </center> </body></html>""")
            else:
                return HttpResponse("""<html> <body bgcolor="lightpink"> <center> <h1> login failed </h1> </center> </body></html>""")
