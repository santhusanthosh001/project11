

from django.contrib import admin
from django.urls import path
from regandloginapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view()),
    path('reginput/',views.RegInput.as_view()),
    path('logininput/',views.LoginInput.as_view()),
    path('reginput/reg/',views.RegView.as_view()),
    path('logininput/login/',views.Loginview.as_view()),

]
