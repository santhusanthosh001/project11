from django import forms
class Regform(forms.Form):

    First_name = forms.CharField(max_length=10)
    Last_name = forms.CharField(max_length=10)
    user_name = forms.CharField(max_length=100)
    password = forms.CharField(max_length=10,widget=forms.PasswordInput())
    cpassword = forms.CharField(max_length=10,widget=forms.PasswordInput())
    emailid = forms.EmailField()
    mobilenumber = forms.IntegerField()
class loginform(forms.Form):

    user_name=forms.CharField(max_length=100)
    password=forms.CharField(max_length=10,widget=forms.PasswordInput())

