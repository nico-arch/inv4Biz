from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),


# Product
    path('products/', views.products, name='dashboard-products'),
    path('products/delete/<int:pk>/', views.product_delete, name='dashboard-products-delete'),
    path('products/detail/<int:pk>/', views.product_detail, name='dashboard-products-detail'),
    path('products/edit/<int:pk>/',   views.product_edit,   name='dashboard-products-edit'),


# Category
    path('products-category/', views.products_category, name='dashboard-products-category'),
    path('products-category/delete/<int:pk>/', views.product_category_delete, name='dashboard-products-category-delete'),
    path('products-category/detail/<int:pk>/', views.product_category_detail, name='dashboard-products-category-detail'),
    path('products-category/edit/<int:pk>/',   views.product_category_edit,   name='dashboard-products-category-edit'),

# Deposit
    #path('deliveries/deposit/show/<int:pk>/', views.deliveries_deposit_show, name='dashboard--delivery-deposit-show'),
    #path('salesorders/deposit/show/<int:pk>/', views.salesorders_deposit_show, name='dashboard-salesorder-deposit-show'),

# Invoice
    path('salesorder/', views.invoices_salesorder, name='dashboard-invoices-salesorder'),#salesorder
    path('delivery/', views.invoices_delivery, name='dashboard-invoices-delivery'),#delivery

    path('invoices/', views.invoices, name='dashboard-invoices'),#invoice
    path('invoices/delete/<int:pk>/', views.invoices_delete, name='dashboard-invoices-delete'),
    path('invoices/detail/<int:pk>/', views.invoices_detail, name='dashboard-invoices-detail'),
    path('invoices/edit/<int:pk>/',   views.invoices_edit,   name='dashboard-invoices-edit'),
    path('invoices/invoice/edit_product/<int:pk>/',   views.invoices_edit_product,   name='dashboard-invoices-edit-product'),
    path('invoices/invoice/edit_product2/<int:invoice_pk>/<int:product_pk>', views.invoices_edit_product_add,   name='dashboard-invoices-edit-product-add'),
    path('invoices/invoice/delete_product/<int:invoice_pk>/<int:invoice_product_pk>', views.invoices_edit_product_delete,   name='dashboard-invoices-edit-product-delete'),
    path('invoices/invoice/delete_product2/<int:invoice_pk>/<int:invoice_product_pk>', views.invoices_edit_product_finish,   name='dashboard-invoices-edit-product-finish'),

    path('invoices/add_due/<int:invoice_pk>/<int:product_pk>', views.invoices_edit_add_due, name='dashboard-invoices-add-due'),
    path('invoices/tranfer_delete_due/<int:invoice_pk>/<int:invoice_product_pk>', views.invoices_edit_transfer_delete_due, name='dashboard-invoices-transfer-delete-due'),


    path('invoices/invoice/printed/<int:pk>/', views.invoices_printed,   name='dashboard-invoices-printed'),
    path('invoices/deposit/show/<int:pk>/', views.invoices_deposit_show, name='dashboard-invoices-deposit-show'),
    path('invoices/deposit/add/<int:pk>/', views.invoices_deposit_add, name='dashboard-invoices-deposit-add'),
    path('invoices/deposit/delete/<int:deposit_pk>/<int:invoice_pk>/', views.invoices_deposit_delete, name='dashboard-invoices-deposit-delete'),



# Proforma
    path('proformas/', views.proformas, name='dashboard-proformas'),
    path('proformas/delete/<int:pk>/', views.proformas_delete, name='dashboard-proformas-delete'),
    #path('proformas/detail/<int:pk>/', views.invoices_detail, name='dashboard-proformas-detail'),
    #path('proformas/edit/<int:pk>/',   views.invoices_edit,   name='dashboard-proformas-edit'),
    path('proformas/proforma/edit_product/<int:pk>/',   views.proformas_edit_product,   name='dashboard-proformas-edit-product'),
    path('proformas/proforma/edit_product2/<int:proforma_pk>/<int:product_pk>', views.proformas_edit_product_add,   name='dashboard-proformas-edit-product-add'),
    path('proformas/proforma/delete_product/<int:proforma_pk>/<int:proforma_product_pk>', views.proformas_edit_product_delete,   name='dashboard-proformas-edit-product-delete'),
    path('proformas/proforma/delete_product2/<int:proforma_pk>/<int:proforma_product_pk>', views.proformas_edit_product_finish,   name='dashboard-proformas-edit-product-finish'),
    path('proformas/proforma/printed/<int:pk>/', views.proformas_printed,   name='dashboard-proformas-printed'),


#Customer
    path('customers/', views.customers, name='dashboard-customers'),
    path('customers/edit/<int:pk>/',   views.customers_edit,   name='dashboard-customers-edit'),
    path('customers/delete/<int:pk>/', views.customers_delete, name='dashboard-customers-delete'),
    #path('customers/detial/<int:pk>/', views.customer_detail,name='dashboard-customer-detail'),

#Orders
    path('order/', views.order, name='dashboard-order'),
]
