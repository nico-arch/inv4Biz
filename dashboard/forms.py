from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'



class InvoiceForm(forms.ModelForm):
  class Meta:
    model = Invoice
    fields = ['client', 
                  'PaymentType', 
                  #'PaymentAmount',
                  'discount',
                  'currency',
                  'name_backup',
                  'email_backup',
                  'phone_backup',
                  'address_backup',]
                  
  def __init__(self, *args, **kwargs):
    super(InvoiceForm, self).__init__(*args, **kwargs)
    for field in self.fields:
      self.fields['name_backup'].widget = forms.HiddenInput()
      self.fields['email_backup'].widget = forms.HiddenInput()
      self.fields['phone_backup'].widget = forms.HiddenInput()
      self.fields['address_backup'].widget = forms.HiddenInput()
      #widgets = {'name_backup': forms.HiddenInput()}


class ProformaForm(forms.ModelForm):
  class Meta:
    model = Proforma
    fields = ['client', 
                  'discount',
                  'currency',
                  'name_backup',
                  'email_backup',
                  'phone_backup',
                  'address_backup',]
  def __init__(self, *args, **kwargs):
    super(ProformaForm, self).__init__(*args, **kwargs)
    for field in self.fields:
      self.fields['name_backup'].widget = forms.HiddenInput()
      self.fields['email_backup'].widget = forms.HiddenInput()
      self.fields['phone_backup'].widget = forms.HiddenInput()
      self.fields['address_backup'].widget = forms.HiddenInput()
      #widgets = {'name_backup': forms.HiddenInput()}





class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


#############################################
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'order_quantity']
