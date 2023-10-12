from django.db import models

class Reg(models.Model):

    First_name=models.CharField(max_length=10)
    Last_name=models.CharField(max_length=10)
    user_name=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    cpassword=models.CharField(max_length=10)
    emailid=models.EmailField()
    mobilenumber=models.IntegerField()
    def __str__(self):
        return self.user_name



