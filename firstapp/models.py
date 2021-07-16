from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
# Create your models here.

class UserType(models.Model):
    CUSTOMER = 1
    SELLER = 2
    CHOICES = (
        (CUSTOMER, "Customer"),
        (SELLER, "Seller"),
    )

    user_type_id = models.PositiveSmallIntegerField(choices=CHOICES, primary_key=True)
        

    def __str__(self):
        return f"{self.user_type_id}"


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now=True)
    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    
    # user_type = models.ManyToManyField(UserType)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


    class UserTypes(models.TextChoices):
        CUSTOMER = 'customer', "CUSTOMER"
        SELLER = 'seller', "SELLER"

    
    default_type = UserTypes.CUSTOMER
    type = models.CharField(max_length=10, choices=UserTypes.choices, default=default_type)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.default_type
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.email


    @property
    def is_seller_check(self):
        if self.is_seller:
            return f"{self.email} is seller..!"
        return f"{self.email} is not seller..!"


class CustomerManager(models.Manager):
    def get_queryset(self):
        return super(CustomerManager, self).get_queryset().filter(type='customer')


class SellerManager(models.Manager):
    def get_queryset(self):
        return super(SellerManager, self).get_queryset().filter(type='seller')


class Customer(CustomUser):  # u can not define new fields in proxy models
    objects = CustomerManager()
    default_type = CustomUser.UserTypes.CUSTOMER


    def purchase(self):
        print("Purchasing product")

    @property
    def show_more_fields(self):
        return self.customermorefields

    class Meta:
        proxy = True

class Seller(CustomUser):
    objects = SellerManager()
    default_type = CustomUser.UserTypes.SELLER

    class Meta:
        proxy = True

    def sell(self):
        print("Selling product")

    @property
    def show_more_fields(self):
        return self.sellermorefields
    

class CustomerMoreFields(models.Model):
    address = models.CharField(max_length=100)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class SellerMoreFields(models.Model):
    gst_no = models.CharField(max_length=100)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)



# class Customer(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     del_address = models.CharField(max_length=500)


# class Seller(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     warehouse_location = models.CharField(max_length=100)
#     license_no = models.CharField(max_length=50)




class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    data_created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "cart"


class Product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.FloatField()

    @classmethod
    def create_prod(cls, nm, price):
        obj = cls.objects.create(name=nm, price=price)
        return obj

    @classmethod
    def update_prod(cls, pid, nm=None, price=None):
        obj = cls.objects.get(prod_id=pid)
        if nm:
            obj.name = nm
        if price:
            obj.price = price
        obj.save()
        return obj


    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"

class ProdCart(models.Model):
    prod_cart_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['cart', 'prod']]


PERSON_TYPES = (
    ('emp', 'Employee'),
    ('stud', 'Student'),
)



"""
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
    class PTypes(models.TextChoices):
        EMP = 'emp', "Employee"
        STUD = 'stud', "Student"

    
    default_type = PTypes.EMP
    type = models.CharField(max_length=4, choices=PTypes.choices, default=default_type)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.default_type
        return super().save(*args, **kwargs)

# Person.objects.all() -- filter(type="emp")


class EmployeeManager(models.Manager):
    
    def get_queryset(self):
        return super(EmployeeManager, self).get_queryset().filter(type='emp')


class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(type='stud')


class Employee(Person):
    default_type = Person.PTypes.EMP
    objects = EmployeeManager()
    class Meta:
        proxy = True    


class Student(Person):
    default_type = Person.PTypes.STUD
    objects = StudentManager()
    class Meta:
        proxy = True    

"""


# 3.5 crores -- 35 fields- columns --.values( id, name, is_active, )




        

    