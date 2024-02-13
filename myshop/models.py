from django.db import models
class Southindian(models.Model):
    Image=models.ImageField(upload_to='images/')
    Name=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Price=models.IntegerField()
    class meta:
        Db_table='indian_dishes'
        def __str__(self) :
            return self.Name
class Chinese(models.Model):
    Image=models.ImageField(upload_to='images/')
    Name=models.CharField(max_length=100)
    Description=models.CharField(max_length=100)
    Price=models.IntegerField()
    class meta:
        Db_table='chinese_dishes'
        def __str__(self) :
            return self.Name

class CartItem(models.Model):
    southindian= models.ForeignKey(Southindian, on_delete=models.CASCADE,null=True)
    chinese= models.ForeignKey(Chinese, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        if self.southindian:
            return f'{self.quantity} x {self.southindian.Name}'
        elif self.chinese:
            return f'{self.quantity} x {self.chinese.Name}'
        else:
            return 'Invalid Cart Item'
class Signup_model(models.Model):

    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Phone_No=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    City=models.CharField(max_length=50)
    Pincode=models.IntegerField()
    State=models.CharField(max_length=50)
    def __str__(self):
        return self.First_name   
class Book_Table(models.Model):
    Name=models .CharField(max_length=50)
    Email=models.EmailField()
    Phone_No=models.CharField(max_length=10)
    Date=models.DateField()
    Time=models.TimeField()
    People=models.IntegerField()
    Message=models.CharField(max_length=200)
    def __str__(self):
        return f'{self.Name } {self.Email}'
# Create your models here.
