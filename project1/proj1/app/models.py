from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATE_CHOICES= (
('Andaman & Nicobar Island', 'Andaman & Nicobar Island'),
('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),
('Bihar','Bihar'),
('Chhattisgarh','Chhattisgarh'),
('Goa','Goa'),
('Gujarat','Gujarat'),
('Haryana','Haryana',),
('Himachal Pr,adesh','Himachal Pradesh'),
('Jharkhand','Jharkhand'),
('Karnataka','Karnataka'),
('Kerala','Kerla'),
('Madhya Pradesh','Madhya Pradesh'),
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
 ('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Odisha','Odisha') ,
('Rajasthan','Rajasthan') ,
('Punjab','Punjab'),
  ('Sikkim','Sikkim') ,
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),
('Tripura','Tripura'),
('Uttar Pradesh','Uttar Pradesh'),
)

    
CATEGORY_CHOICES=(
    ('CR','curd'),
    ('ML','Milk'),
    ('LS','Laasi'),
    ('MS','Milkshake'),
    ('PN','paneer'),
    ('GH','Ghee'),
    ('CH','chesse'),
    ('IC','Ice-cream'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    descripition = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    Product_image = models.ImageField(upload_to='product')  
    def __str__(self):
        return self.title
    
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name =  models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    # mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name    
    
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE) 
    quantity=models.PositiveIntegerField(default=1)   
    
    @property
    def total_cost(self):
        return self.quantity*self.product.discount_price