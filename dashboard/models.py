from django.db import models
from django.contrib.auth.models import User
from datetime import *
import uuid
from django.utils import timezone

# Create your models here.



###############################to be continued client provider
class Customer(models.Model):
    name = models.CharField(max_length=500, unique=True, null =True)
    email = models.EmailField(max_length=254, null=True, default = 'default@default.com')
    phone = models.PositiveIntegerField(null=True, default = 0)
    address = models.CharField(max_length=500, default ='--------', null =True)
    #info = models.JSONField()

    def __str__(self):
        return '{0}'.format(self.name)


class Provider(models.Model):
    name = models.CharField(max_length=500, unique=True, null=True)

    #info = models.JSONField()

    def __str__(self):
        return 'Client : {0}'.format(self.id)








class ModelCounter(models.Model):
    name = models.CharField(max_length=500, help_text='')

    def __str__(self):
        return 'ModelCounter : {0}'.format(self.name)


Currency_Category = (
    ('HTG', 'HTG'),
    #('$', '$'),
)
Payment_Type = (
    ('Cash', 'Cash'),
    ('Check', 'Check'),
    ('Credit', 'Credit'),
)


class Category(models.Model):
    name = models.CharField(max_length=500, help_text='')

    def __str__(self):
        return '{0}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=500, unique=True, null = True)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.FloatField(null=True)

    #remark   = models.CharField(max_length=300, null =True)
    #currency = models.CharField(max_length=50, choices=Currency_Category, null=True)
    def __str__(self):
        return 'Product : {0}'.format(self.name)


class Invoice(models.Model):
    #info = models.JSONField(null=True)
    #example of multiple objects: [{"name": "T-shirt", "category": "Clothe", "quantity": 2, "price": 6.1}, {"name": "T-shirt2", "category": "Clothe2", "quantity": 22, "price": 6.12}]
    #Total = models.FloatField()
    #
    #client = models.CharField('Client', max_length=300, null=True)
    client = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    name_backup = models.CharField(max_length=500, null = True)
    email_backup = models.EmailField(max_length=254, null=True)
    phone_backup = models.PositiveIntegerField(null=True)
    address_backup = models.CharField(max_length=500, null=True )

    PoNumber = models.IntegerField('P.O Number',null=True)
    PaymentType = models.CharField('Payment Type',
                                   max_length=50,
                                   choices=Payment_Type,
                                   null=True)
    #PaymentAmount = models.FloatField('Payment Amount', null=True)
    #Balance = models.FloatField(null=True)

    Date   = models.DateTimeField('Date',
                              default=datetime.now, blank=True
                              #default=timezone.now,
                              #null= False,
                              #blank=False
                              )
    Total = models.FloatField(null=True, default = 0.0)
    discount = models.FloatField('Discount',null=True, default = 0.0)
    Balance = models.FloatField(null=True)
    currency = models.CharField(max_length=50, choices=Currency_Category,default='HTG',null=True)
    class Meta:
        ordering = ('Date',)
    def __str__(self):
        return 'Invoice : {0}'.format(self.id)


class InvoiceProduct(models.Model):
    Invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    productName = models.CharField(max_length=500,  null=True)
    quantity = models.PositiveIntegerField(null=True)
    dueQuantity = models.PositiveIntegerField('Due Qtty', null=True)
    price = models.FloatField(null=True)
    Total = models.FloatField(null=True)

    def __str__(self):
        return 'Product in invoice : {0}'.format(self.Invoice.id)


class InvoiceDeposit(models.Model):
    Invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)

    Amount = models.FloatField(null=True)
    Date   = models.DateTimeField('Date',
                              default=datetime.now, blank=True
                              #default=timezone.now,
                              #null= False,
                              #blank=False
                              )

    def __str__(self):
        return 'Deposit of : {0}'.format(self.Date)


class Salesorder(models.Model):
    #info = models.JSONField(null=True)
    #example of multiple objects: [{"name": "T-shirt", "category": "Clothe", "quantity": 2, "price": 6.1}, {"name": "T-shirt2", "category": "Clothe2", "quantity": 22, "price": 6.12}]
    #Total = models.FloatField()
    #
    #client = models.CharField('Client', max_length=300, null=True)
    client = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    name_backup = models.CharField(max_length=500, null = True)
    email_backup = models.EmailField(max_length=254, null=True)
    phone_backup = models.PositiveIntegerField(null=True)
    address_backup = models.CharField(max_length=500, null=True )

    PoNumber = models.IntegerField('P.O Number',null=True)
    PaymentType = models.CharField('Payment Type',
                                   max_length=50,
                                   choices=Payment_Type,
                                   null=True)
    #PaymentAmount = models.FloatField('Payment Amount', null=True)
    #Balance = models.FloatField(null=True)

    Date   = models.DateTimeField('Date',
                              default=datetime.now, blank=True
                              #default=timezone.now,
                              #null= False,
                              #blank=False
                              )
    Total = models.FloatField(null=True, default = 0.0)
    discount = models.FloatField('Discount',null=True, default = 0.0)
    currency = models.CharField(max_length=50, choices=Currency_Category,default='HTG',null=True)
    class Meta:
        ordering = ('Date',)
    def __str__(self):
        return 'Sales order : {0}'.format(self.id)


class SalesorderProduct(models.Model):
    Salesorder = models.ForeignKey(Salesorder, on_delete=models.CASCADE, null=True)
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    productName = models.CharField(max_length=500,  null=True)
    quantity = models.PositiveIntegerField(null=True)
    dueQuantity = models.PositiveIntegerField('Due Qtty', null=True)
    price = models.FloatField(null=True)
    Total = models.FloatField(null=True)

    def __str__(self):
        return 'Product in Sales order : {0}'.format(self.Salesorder.id)


class SalesorderDeposit(models.Model):
    Salesorder = models.ForeignKey(Salesorder, on_delete=models.CASCADE, null=True)

    Amount = models.PositiveIntegerField(null=True)
    Date   = models.DateTimeField('Date',
                              default=datetime.now, blank=True
                              #default=timezone.now,
                              #null= False,
                              #blank=False
                              )

    def __str__(self):
        return 'Deposit of : {0}'.format(self.Date)



class Delivery(models.Model):
    #info = models.JSONField(null=True)
    #example of multiple objects: [{"name": "T-shirt", "category": "Clothe", "quantity": 2, "price": 6.1}, {"name": "T-shirt2", "category": "Clothe2", "quantity": 22, "price": 6.12}]
    #Total = models.FloatField()
    #
    #client = models.CharField('Client', max_length=300, null=True)
    client = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    name_backup = models.CharField(max_length=500, null = True)
    email_backup = models.EmailField(max_length=254, null=True)
    phone_backup = models.PositiveIntegerField(null=True)
    address_backup = models.CharField(max_length=500, null=True )

    PoNumber = models.IntegerField('P.O Number',null=True)
    PaymentType = models.CharField('Payment Type',
                                   max_length=50,
                                   choices=Payment_Type,
                                   null=True)
    #PaymentAmount = models.FloatField('Payment Amount', null=True)
    #Balance = models.FloatField(null=True)

    Date   = models.DateTimeField('Date',
                              default=datetime.now, blank=True
                              #default=timezone.now,
                              #null= False,
                              #blank=False
                              )
    Total = models.FloatField(null=True, default = 0.0)
    discount = models.FloatField('Discount',null=True, default = 0.0)
    currency = models.CharField(max_length=50, choices=Currency_Category,default='HTG',null=True)
    class Meta:
        ordering = ('Date',)
    def __str__(self):
        return 'Delivery : {0}'.format(self.id)


class DeliveryProduct(models.Model):
    Delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, null=True)
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    productName = models.CharField(max_length=500,  null=True)
    quantity = models.PositiveIntegerField(null=True)
    dueQuantity = models.PositiveIntegerField('Due Qtty', null=True)
    price = models.FloatField(null=True)
    Total = models.FloatField(null=True)

    def __str__(self):
        return 'Product in Delivery : {0}'.format(self.Delivery.id)





class DeliveryDeposit(models.Model):
    Delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, null=True)

    Amount = models.PositiveIntegerField(null=True)
    Date   = models.DateTimeField('Date',
                              default=datetime.now, blank=True
                              #default=timezone.now,
                              #null= False,
                              #blank=False
                              )

    def __str__(self):
        return 'Deposit of : {0}'.format(self.Date)









class Proforma(models.Model):
    client = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    name_backup = models.CharField(max_length=500, null = True)
    email_backup = models.EmailField(max_length=254, null=True)
    phone_backup = models.PositiveIntegerField(null=True)
    address_backup = models.CharField(max_length=500, null=True )



    Date   = models.DateTimeField('Date',
                              default=datetime.now, blank=True)
    Total = models.FloatField(null=True, default = 0.0)
    discount = models.FloatField('Discount',null=True, default = 0.0)
    currency = models.CharField(max_length=50, choices=Currency_Category,default='HTG',null=True)
    class Meta:
        ordering = ('Date',)
    def __str__(self):
        return 'Proforma : {0}'.format(self.id)


class ProformaProduct(models.Model):
    Proforma = models.ForeignKey(Proforma, on_delete=models.CASCADE, null=True)
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    productName = models.CharField(max_length=500,  null=True)
    quantity = models.PositiveIntegerField(null=True)
    price = models.FloatField(null=True)
    Total = models.FloatField(null=True)

    def __str__(self):
        return 'Product in Proforma : {0}'.format(self.Proforma.id)













################################################################################
#CATEGORY = (
#    ('Stationary', 'Stationary'),
#    ('Electronics', 'Electronics'),
#    ('Food', 'Food'),
#)


class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'
