from django.contrib import admin
from .models import * #Product, Order


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Invoice)
admin.site.register(InvoiceProduct)
admin.site.register(Proforma)
admin.site.register(ProformaProduct)




admin.site.site_header = "Cheap Solutions's Administration"
admin.site.site_title  = "Cheap Solutions"
admin.site.index_title = "Administration"