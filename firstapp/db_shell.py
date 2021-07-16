# exec(open(r"F:\Class\B3-B4\Django\ecomapp\firstapp\db_shell.py").read())


from firstapp.models import *

# p1 = Person.objects.create(first_name="rfwf", last_name="xyz")   # 2type = emp
# print(p1)

# print(Person.objects.all()[0].__dict__)

# print(Employee.objects.all())

# print(Student.objects.all())

# Employee.objects.create(first_name="Pankaj", last_name="Suryawanshi")

# Student.objects.create(first_name="AAA", last_name="BBB")


# c1 = Customer.objects.create(email="c3@gmail.com", password="admin")
# print(c1.type)

# print(Customer.objects.all()[0].purchase())
# print(Seller.objects.all()[0].sell())


# c1 = Seller.objects.first()
# print(c1.show_more_fields)
# cm1 = CustomerMoreFields.objects.create(address="Pune", user=c1)
# cm1 = SellerMoreFields.objects.create(gst_no="JJH6SD6W2FWWF1", user=c1)
# print(c1.show_more_fields)

c = Customer.objects.only('id', 'email', 'type')
# print(c)

print(CustomUser.objects.values().order_by("-id")[1])  # 

# Q -- & | ~


# from django.db.models import Subquery
# Subquery(CustomUser.objects.values('id')):   # ids
    