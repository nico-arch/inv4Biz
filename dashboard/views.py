from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
""""
category = Category.objects.all()
category_count = category.count()


product = Product.objects.all()
product_count = product.count()
order = Order.objects.all()
order_count = order.count()
customer = User.objects.filter(groups=2)
customer_count = customer.count()
"""

# Create your views here.

#index
@login_required(login_url='user-login')
def index(request):
    """"""
    proforma = Proforma.objects.all().order_by('-id',)
    proforma_count = proforma.count()

    invoice = Invoice.objects.all().order_by('-id',)
    invoice_count = invoice.count()

    category = Category.objects.all()
    category_count = category.count()

    product = Product.objects.all().order_by('-id',)
    product_count = product.count()
    order = Order.objects.all().order_by('-id',)
    order_count = order.count()
    customer = Customer.objects.all()
    customer_count = customer.count()
    """"""

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'proforma':proforma,
        'proforma_count':proforma_count,
        'invoice': invoice,
        'invoice_count': invoice_count,
        'category': category,
        'category_count': category_count,
        'form': form,
        'order': order,
        'product': product,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/index.html', context)


#Product views
@login_required(login_url='user-login')
def products(request):
    """"""
    proforma = Proforma.objects.all().order_by('-id',)
    proforma_count = proforma.count()

    invoice = Invoice.objects.all().order_by('-id',)
    invoice_count = invoice.count()

    category = Category.objects.all()
    category_count = category.count()

    product = Product.objects.all().order_by('name',)
    product_count = product.count()
    customer = Customer.objects.all()
    customer_count = customer.count()
    order = Order.objects.all().order_by('-id',)
    order_count = order.count()
    product_quantity = Product.objects.filter(name='')
    """"""

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'proforma':proformas_delete,
        'proforma_count':proforma_count,
        'invoice': invoice,
        'invoice_count': invoice_count,
        'category': category,
        'category_count': category_count,
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/products.html', context)


@login_required(login_url='user-login')
def product_detail(request, pk):
    context = {}
    return render(request, 'dashboard/products_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            product = Product.objects.get(id=pk)
            product_in_invoice = InvoiceProduct.objects.all()
            product_in_proforma = ProformaProduct.objects.all()

            #Update the product in the invoices and proformas
            for piin in product_in_invoice:
              if piin.Product == product:
                piin.productName = product.name
                piin.price = product.price
                total = piin.quantity * piin.price
                piin.Total = total
                piin.save()
            for pipr in product_in_proforma:
              if pipr.Product == product:
                pipr.productName = product.name
                pipr.price = product.price
                total = pipr.quantity * pipr.price
                pipr.Total = total
                pipr.save()

            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {'item': item}
    return render(request, 'dashboard/products_delete.html', context)


######################################################################################


#Category's views
@login_required(login_url='user-login')
def products_category(request):
    """"""
    proforma = Proforma.objects.all().order_by('-id',)
    proforma_count = proforma.count()

    invoice = Invoice.objects.all().order_by('-id',)
    invoice_count = invoice.count()

    category = Category.objects.all().order_by('name',)
    category_count = category.count()

    product = Product.objects.all().order_by('-id',)
    product_count = product.count()
    customer = Customer.objects.all()
    customer_count = customer.count()
    order = Order.objects.all().order_by('-id',)
    order_count = order.count()
    """"""

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            product_category_name = form.cleaned_data.get('name')
            messages.success(request,
                             f'{product_category_name} has been added')
            return redirect('dashboard-products-category')
    else:
        form = CategoryForm()

    context = {
        'proforma':proforma,
        'proforma_count':proforma_count,
        'invoice': invoice,
        'invoice_count': invoice_count,
        'category': category,
        'category_count': category_count,
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/category.html', context)


@login_required(login_url='user-login')
def product_category_detail(request, pk):
    context = {}
    return render(request, 'dashboard/category_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_category_edit(request, pk):
    item = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products-category')
    else:
        form = CategoryForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/category_edit.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def product_category_delete(request, pk):
    item = Category.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products-category')
    context = {'item': item}
    return render(request, 'dashboard/category_delete.html', context)


#Invoice
@login_required(login_url='user-login')
def invoices(request):
    """"""
    proforma = Proforma.objects.all().order_by('-id',)
    proforma_count = proforma.count()

    invoice = Invoice.objects.all().order_by('-id',)
    invoice_count = invoice.count()

    category = Category.objects.all().order_by('-id',)
    category_count = category.count()

    product = Product.objects.all().order_by('-id',)
    product_count = product.count()
    customer = Customer.objects.all()
    customer_count = customer.count()
    order = Order.objects.all().order_by('-id',)
    order_count = order.count()
    """"""

    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if request.POST.get("client"):
          custo = Customer.objects.get(id=int(request.POST.get("client")))


          request.POST._mutable = True
          request.POST['name_backup'] = custo.name
          request.POST['email_backup'] = custo.email
          request.POST['phone_backup'] = custo.phone
          request.POST['address_backup'] = custo.address

          #messages.success(request, f'{custo.name}: inside post client')
          #form.save()

          #if form.is_valid():
          #  form.save()
          #  messages.success(request, f'inside is valid after client')
          #  return redirect('dashboard-invoices')


        if form.is_valid():
          form.save()
          messages.success(request, f'An invoice has been added')
          return redirect('dashboard-invoices')
    else:
       #messages.success(request, f'inside else')
       form = InvoiceForm()


    context = {
        'proforma':proforma,
        'proforma_count':proforma_count,
        'invoice': invoice,
        'invoice_count': invoice_count,
        'category': category,
        'category_count': category_count,
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/invoice.html', context)


@login_required(login_url='user-login')
def invoices_detail(request, pk):
    context = {}
    return render(request, 'dashboard/invoice_detail.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_edit(request, pk):
    item = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-invoices')
    else:
        form = InvoiceForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/invoice_edit.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_edit_product(request, pk):
    proforma = Proforma.objects.all().order_by('-id',)
    proforma_count = proforma.count()

    invoice = Invoice.objects.all().order_by('-id',)
    invoice_product = InvoiceProduct.objects.all()
    invoice_count = invoice.count()
    category = Category.objects.all().order_by('-id',)
    category_count = category.count()

    query = request.GET.get('q', '')
    if query == '':
      product = Product.objects.all()
    else:
      product = Product.objects.filter(
            Q(name__icontains=query) #| Q(state__icontains=query)
        )


    page = request.GET.get('page', 1)
    paginator = Paginator(product, 5)

    try:
        productss = paginator.page(page)
    except PageNotAnInteger:
        productss = paginator.page(1)
    except EmptyPage:
        productss = paginator.page(paginator.num_pages)

    product_count = product.count()
    customer = Customer.objects.all()
    customer_count = customer.count()
    order = Order.objects.all().order_by('-id',)
    order_count = order.count()

    item = Invoice.objects.get(id=pk)


    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            if request.POST.get("client"):
              #update the backup ith the proforma
              custo = Customer.objects.get(id=int(request.POST.get("client")))

              Invoice.objects.filter(id=pk).update(name_backup= custo.name)
              Invoice.objects.filter(id=pk).update(email_backup= custo.email)
              Invoice.objects.filter(id=pk).update(phone_backup= custo.phone)
              Invoice.objects.filter(id=pk).update(address_backup= custo.address)

            #return redirect('dashboard-invoices')
    else:
        form = InvoiceForm(instance=item)

    invoice_total_amount = 0.0
    for invoice_ in invoice:
      if invoice_.id == pk:
        for product_in_invoice in invoice_product:
          if product_in_invoice.Invoice.id == pk:
            invoice_total_amount = invoice_total_amount + product_in_invoice.Total

    Invoice.objects.filter(id=pk).update(Total= invoice_total_amount)


#    """
    #Balance todo-------------------------------------------------------
    #invoice = Invoice.objects.all()
    invoice_deposit = InvoiceDeposit.objects.all().order_by('-id',)
    invoice_to_be_printed = Invoice.objects.get(id=pk)

    amountPaid = 0.0
    amountWithdrawn = 0.0
    amount_paid_after_withdrawn = 0.0
    balance = 0.0
    for deposit in invoice_deposit:
        if deposit.Invoice.id == pk and deposit.Type == "Deposit":
            amountPaid += float(deposit.Amount)

    for withdraw in invoice_deposit:
        if withdraw.Invoice.id == pk and withdraw.Type == "Withdrawal":
            amountWithdrawn += float(withdraw.Amount)

    total_after_discount2 = float(invoice_to_be_printed.Total - invoice_to_be_printed.discount)
    amount_paid_after_withdrawn = amountPaid - amountWithdrawn

    balance = total_after_discount2 - amount_paid_after_withdrawn
    Invoice.objects.filter(id=pk).update(Balance = balance)
    #Balance todo^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    #---------------------------------------------------
    item2 = Invoice.objects.get(id=pk)
    total_after_discount = item2.Total - item2.discount


    context = {
        'client_funds': item2.client.Funds,
        'balance': item2.Balance,
        'proforma':proforma,
        'proforma_count':proforma_count,
        'total_after_discount':total_after_discount,
        'invoice_total': invoice_total_amount,
        'id_invoice': pk,
        'invoice_product':invoice_product,
        'form': form,
        'query':query,
        'invoice': invoice,
        'invoice_count': invoice_count,
        'category': category,
        'category_count': category_count,

        'products': productss,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/invoice_edit_product.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_edit_product_add(request, invoice_pk, product_pk):
    item = Invoice.objects.get(id=invoice_pk)

    selectedProduct = Product.objects.get(pk=product_pk)

    quantityy = 0
    if request.GET.get('quantity') is  "" :#| request.GET.get('quantity') <= 0 :
      #quantityy = request.GET.get('quantity')
      quantityy = 1
      #messages.success(request, f'!!ALERT-The quantity must not be empty or 0 -ALERT!!')
      #return redirect('dashboard-invoices-edit-product', pk=invoice_pk)
      #Remove the quantity in the stock
      #Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))


      if InvoiceProduct.objects.filter(Invoice__id=item.id, Product__id = selectedProduct.id).exists():
        Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))
        #Modify the product in the invoice if the product exists in the invoice
        #product_in_invoice = InvoiceProduct.objects.get(productName=selectedProduct.name)
        product_in_invoice = InvoiceProduct.objects.get(Invoice__id=item.id, Product__id = selectedProduct.id)
        InvoiceProduct.objects.filter(Invoice__id=item.id, Product__id = selectedProduct.id).update(quantity= product_in_invoice.quantity + int(quantityy))

        product_in_invoice2 = InvoiceProduct.objects.get(Invoice__id=item.id, Product__id = selectedProduct.id)
        InvoiceProduct.objects.filter(Invoice__id=item.id, Product__id = selectedProduct.id).update(Total= product_in_invoice2.quantity * product_in_invoice2.price)
      else:
        Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))
        #Adding the product to the invoice
        total = selectedProduct.price * quantityy
        invoiceProduct = InvoiceProduct(id=None, Invoice=item,
        Product = selectedProduct,
        productName=selectedProduct.name,
        quantity=  quantityy,#selectedProduct.quantity,
        price = selectedProduct.price,
        Total = total)

        invoiceProduct.save()
      return redirect('dashboard-invoices-edit-product', pk=invoice_pk)
    else:
      quantityy = request.GET.get('quantity')

    #Remove the quantity in the stock
    #Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))

    if InvoiceProduct.objects.filter(Invoice__id=item.id, Product__id = selectedProduct.id).exists():
      Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))
      #Modify the product in the invoice if the product exists in the invoice
      product_in_invoice = InvoiceProduct.objects.get(Invoice__id=item.id, Product__id = selectedProduct.id)
      InvoiceProduct.objects.filter(Invoice__id=item.id, Product__id = selectedProduct.id).update(quantity= product_in_invoice.quantity + int(quantityy))

      product_in_invoice2 = InvoiceProduct.objects.get(Invoice__id=item.id, Product__id = selectedProduct.id)
      InvoiceProduct.objects.filter(Invoice__id=item.id, Product__id = selectedProduct.id).update(Total= product_in_invoice2.quantity * product_in_invoice2.price)
    else:
      Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))
      #Adding the product to the invoice
      total = selectedProduct.price * float(quantityy)
      invoiceProduct = InvoiceProduct(id=None, Invoice=item,
      Product = selectedProduct,
      productName=selectedProduct.name,
      quantity=  quantityy,#selectedProduct.quantity,
      price = selectedProduct.price,
      Total = total)

      invoiceProduct.save()

    return redirect('dashboard-invoices-edit-product', pk=invoice_pk)




@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_edit_product_search(request, invoice_pk, invoice_product_pk):

    query = self.request.GET.get('q')

    return redirect('dashboard-invoices-edit-product', pk=invoice_pk)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_edit_product_delete(request, invoice_pk, invoice_product_pk):
    #Get the selected product in the invoice
    productInvoice = InvoiceProduct.objects.get(id=invoice_product_pk)
    #Get the customer account
    invoice = Invoice.objects.get(id=invoice_pk)
    customer = Customer.objects.get(id=invoice.client.id)

    if request.GET.get('quantity2') is  "" :
      #Return the product in the stock if the product already exist
      if Product.objects.filter(name=productInvoice.productName).exists():
        #Modify the product in the invoice if the product exists in the invoice
        product = Product.objects.get(name=productInvoice.productName)
        Product.objects.filter(name=productInvoice.productName).update(quantity= product.quantity + productInvoice.quantity)

        productInvoice.delete()

        return redirect('dashboard-invoices-edit-product', pk=invoice_pk)
    else:
      quantityy = request.GET.get('quantity2')
      #Return the product in the stock if the product already exist
      if Product.objects.filter(name=productInvoice.productName).exists():
        #Modify the product in the invoice if the product exists in the invoice
        product = Product.objects.get(name=productInvoice.productName)
        Product.objects.filter(name=productInvoice.productName).update(quantity= product.quantity + int(quantityy))
        InvoiceProduct.objects.filter(id=invoice_product_pk).update(quantity = productInvoice.quantity - int(quantityy))

        invoiceproduct = InvoiceProduct.objects.get(id=invoice_product_pk)
        InvoiceProduct.objects.filter(id=invoice_product_pk).update(Total = invoiceproduct.quantity * invoiceproduct.price)


    productInvoice2 = InvoiceProduct.objects.get(id=invoice_product_pk)
    if productInvoice2.quantity == 0:
      #Delete the selectionned product
      productInvoice2.delete()

    return redirect('dashboard-invoices-edit-product', pk=invoice_pk)



@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_edit_product_finish(request, invoice_pk, invoice_product_pk):
  #Get the selected product in the invoice
  productInvoice = InvoiceProduct.objects.get(id=invoice_product_pk)
  #productInvoice.price = 0.0;
  #productInvoice.save()
  productInvoice.delete()
  return redirect('dashboard-invoices-edit-product', pk=invoice_pk)
  #return redirect('dashboard-index')





@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_delete(request, pk):
    item = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-invoices')
    context = {'item': item}
    return render(request, 'dashboard/invoice_delete.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_printed(request, pk):
  #invoice = Invoice.objects.all()
  invoice_product = InvoiceProduct.objects.all()
  invoice_to_be_printed = Invoice.objects.get(id=pk)

  total_after_discount = invoice_to_be_printed.Total - invoice_to_be_printed.discount

  context = {
            'total_after_discount':total_after_discount,
            'invoice': invoice_to_be_printed,
            'invoice_product': invoice_product
            }
  return render(request, 'dashboard/invoice_printed.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_edit_add_due(request, invoice_pk, product_pk):
    invoice  = Invoice.objects.get(id=invoice_pk )
    produt = Product.objects.get(id=product_pk )

    #Catch to the request:
    if request.method == 'POST':
        if request.POST.get("due_quantity") == '':
            return redirect('dashboard-invoices-edit-product', pk = invoice_pk)
        #If add button is pressed, use the value from input: due_quantity :
        if float( request.POST.get("due_quantity") ) > 0.0 and "add" in request.POST and InvoiceProduct.objects.filter(Invoice= invoice, Product = produt).exists():
            invoice_product = InvoiceProduct.objects.get(Invoice= invoice, Product= produt)
            amount = float( request.POST.get("due_quantity") )
            due_quantity = invoice_product.dueQuantity
            due_quantity += amount
            invoice_product.dueQuantity = due_quantity
            invoice_product.save()
            pass
        else:
            messages.success(request, f'Error!')

    return redirect('dashboard-invoices-edit-product', pk = invoice_pk)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_edit_transfer_delete_due(request, invoice_pk, invoice_product_pk):
    invoice  = Invoice.objects.get(id=invoice_pk )
    invoice_product = InvoiceProduct.objects.get(pk= invoice_product_pk)
    #produt = Product.objects.get(pk=invoice_product.Product.id )

    #Catch to the request:
    if request.method == 'POST':
        if request.POST.get("due_quantity") == '':
            return redirect('dashboard-invoices-edit-product', pk = invoice_pk)

        #If tranfer button is pressed, use the value from input: due_quantity :
        if Product.objects.filter(pk= invoice_product.Product.id).exists(): #if the product exists
            produt = Product.objects.get(pk=invoice_product.Product.id )
            if float( request.POST.get("due_quantity") ) <= invoice_product.dueQuantity and float( request.POST.get("due_quantity") ) > 0.0 and "tranfer" in request.POST and produt.quantity >= float( request.POST.get("due_quantity") ) and invoice_product.dueQuantity > 0:

                amount = float( request.POST.get("due_quantity") )
                due_quantity = invoice_product.dueQuantity
                due_quantity -= amount
                invoice_product.dueQuantity = due_quantity

                invoice_product_quantity = invoice_product.quantity
                invoice_product_quantity += amount
                invoice_product.quantity = invoice_product_quantity

                invoice_product_total = invoice_product.quantity * invoice_product.price
                invoice_product.Total = invoice_product_total

                #take the products in stock for the transfer
                product_quantity_from_stock = produt.quantity
                product_quantity_from_stock -= amount
                produt.quantity = product_quantity_from_stock

                produt.save()
                invoice_product.save()
                pass



        #If delete button is pressed, use the value from input: due_quantity :
        if float( request.POST.get("due_quantity") ) <= invoice_product.dueQuantity and float( request.POST.get("due_quantity") ) > 0.0 and "delete" in request.POST and invoice_product.dueQuantity > 0 and InvoiceProduct.objects.filter(Invoice= invoice, Product = produt).exists():
            amount = float( request.POST.get("due_quantity") )
            due_quantity = invoice_product.dueQuantity
            due_quantity -= amount
            invoice_product.dueQuantity = due_quantity
            invoice_product.save()
            pass


    return redirect('dashboard-invoices-edit-product', pk = invoice_pk)


# Deposit
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_deposit_show(request, pk):
  #invoice = Invoice.objects.all()
  invoice_deposit = InvoiceDeposit.objects.all().order_by('-id',)
  invoice_to_be_printed = Invoice.objects.get(id=pk)

  amountPaid = 0.0
  amountWithdrawn = 0.0
  amount_paid_after_withdrawn = 0.0
  balance = 0.0
  for deposit in invoice_deposit:
      if deposit.Invoice.id == pk and deposit.Type == "Deposit":
          amountPaid += float(deposit.Amount)

  for withdraw in invoice_deposit:
      if withdraw.Invoice.id == pk and withdraw.Type == "Withdrawal":
          amountWithdrawn += float(withdraw.Amount)

  total_after_discount = float(invoice_to_be_printed.Total - invoice_to_be_printed.discount)
  amount_paid_after_withdrawn = amountPaid - amountWithdrawn

  balance = total_after_discount - amount_paid_after_withdrawn
  Invoice.objects.filter(id=pk).update(Balance = balance)


  context = {
            'balance': balance,
            'invoice': invoice_to_be_printed,
            'invoice_deposit': invoice_deposit
            }
  return render(request, 'dashboard/invoice_deposit.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_deposit_add(request, pk):
    invoice_to_be_printed = Invoice.objects.get(id=pk)
    invoice_deposit = InvoiceDeposit.objects.all().order_by('-id',)
    amountPaid = 0.0
    amountWithdrawn = 0.0
    amount_to_paid_after_withdrawn = 0.0

    for deposit in invoice_deposit:
        if deposit.Invoice.id == pk and deposit.Type == "Deposit":
            amountPaid += float(deposit.Amount)
    for withdraw in invoice_deposit:
        if withdraw.Invoice.id == pk and withdraw.Type == "Withdrawal":
            amountWithdrawn += float(withdraw.Amount)

    total_after_discount = float(invoice_to_be_printed.Total - invoice_to_be_printed.discount)
    amount_to_paid_after_withdrawn = amountPaid - amountWithdrawn

    if request.method == 'POST':
        if request.POST.get("amount") == '':
            return redirect('dashboard-invoices-deposit-show', pk=pk)

        if float( request.POST.get("amount") ) > 0.0 and "depose-from-funds" in request.POST and float( request.POST.get("amount") ) <=invoice_to_be_printed.Balance:
            amount = float( request.POST.get("amount") )
            customer = Customer.objects.get(id=invoice_to_be_printed.client.id)
            funds = customer.Funds - amount

            customer.Funds = funds
            customer.save()

            invoiceDeposit = InvoiceDeposit(id=None,
                            Invoice=invoice_to_be_printed,
                            Type="Deposit",
                            Amount = amount,
                            )

            invoiceDeposit.save()


        if float( request.POST.get("amount") ) > 0.0 and "depose" in request.POST and float( request.POST.get("amount") ) <=invoice_to_be_printed.Balance:
            amount = float( request.POST.get("amount") )

            invoiceDeposit = InvoiceDeposit(id=None,
                            Invoice=invoice_to_be_printed,
                            Type="Deposit",
                            Amount = amount,
                            )

            invoiceDeposit.save()


    return redirect('dashboard-invoices-deposit-show', pk=pk)



@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def invoices_deposit_delete(request, deposit_pk, invoice_pk):
    deposit = InvoiceDeposit.objects.get(id=deposit_pk)

    if request.method == 'POST' and "delete" in request.POST:
        deposit.delete()
        return redirect('dashboard-invoices-deposit-show', pk = invoice_pk)

    if request.method == 'POST' and "withdraw" in request.POST:
        invoice = Invoice.objects.get(id=invoice_pk)
        customer = Customer.objects.get(id=invoice.client.id)

        newFunds = customer.Funds
        newFunds += deposit.Amount

        customer.Funds = newFunds
        customer.save()

        deposit.delete()
        return redirect('dashboard-invoices-deposit-show', pk = invoice_pk)

    return redirect('dashboard-invoices-deposit-show', pk = invoice_pk)












#################################################
# Proforma
@login_required(login_url='user-login')
def proformas(request):
    """"""
    proforma = Proforma.objects.all().order_by('-id',)
    proforma_count = proforma.count()
    proforma_product = ProformaProduct.objects.all()

    invoice  = Invoice.objects.all().order_by('-id',)
    invoice_count = invoice.count()

    category = Category.objects.all().order_by('-id',)
    category_count = category.count()

    product = Product.objects.all().order_by('-id',)
    product_count = product.count()
    customer = Customer.objects.all()
    customer_count = customer.count()
    order = Order.objects.all().order_by('-id',)
    order_count = order.count()
    """"""

    if request.method == 'POST':
        form = ProformaForm(request.POST)
        if request.POST.get("client"):
          custo = Customer.objects.get(id=int(request.POST.get("client")))


          request.POST._mutable = True
          request.POST['name_backup'] = custo.name
          request.POST['email_backup'] = custo.email
          request.POST['phone_backup'] = custo.phone
          request.POST['address_backup'] = custo.address

          #messages.success(request, f'{custo.name}: inside post client')
          #form.save()

          #if form.is_valid():
          #  form.save()
          #  messages.success(request, f'inside is valid after client')
          #  return redirect('dashboard-invoices')


        if form.is_valid():
          form.save()
          messages.success(request, f'A Proforma has been added')
          return redirect('dashboard-proformas')
    else:
       #messages.success(request, f'inside else')
       form = ProformaForm()




    context = {
        'proforma':proforma,
        'proforma_count':proforma_count,
        'proforma_product':proforma_product,

        'invoice': invoice,
        'invoice_count': invoice_count,
        'category': category,
        'category_count': category_count,
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/proforma.html', context)



@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def proformas_edit_product(request, pk):
    proforma = Proforma.objects.all().order_by('-id',)
    proforma_count = proforma.count()
    proforma_product = ProformaProduct.objects.all()


    invoice = Invoice.objects.all().order_by('-id',)
    invoice_product = InvoiceProduct.objects.all()
    invoice_count = invoice.count()
    category = Category.objects.all().order_by('-id',)
    category_count = category.count()

    query = request.GET.get('q', '')
    if query == '':
      product = Product.objects.all()
    else:
      product = Product.objects.filter(
            Q(name__icontains=query) #| Q(state__icontains=query)
        )


    page = request.GET.get('page', 1)
    paginator = Paginator(product, 5)

    try:
        productss = paginator.page(page)
    except PageNotAnInteger:
        productss = paginator.page(1)
    except EmptyPage:
        productss = paginator.page(paginator.num_pages)

    product_count = product.count()
    customer = Customer.objects.all()
    customer_count = customer.count()
    order = Order.objects.all().order_by('-id',)
    order_count = order.count()

    item = Proforma.objects.get(id=pk)


    if request.method == 'POST':
        form = ProformaForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            if request.POST.get("client"):
              #update the backup ith the proforma
              custo = Customer.objects.get(id=int(request.POST.get("client")))

              Proforma.objects.filter(id=pk).update(name_backup= custo.name)
              Proforma.objects.filter(id=pk).update(email_backup= custo.email)
              Proforma.objects.filter(id=pk).update(phone_backup= custo.phone)
              Proforma.objects.filter(id=pk).update(address_backup= custo.address)

            #return redirect('dashboard-invoices')
    else:
        form = ProformaForm(instance=item)

    proforma_total_amount = 0.0
    for proforma_ in proforma:
      if proforma_.id == pk:
        for product_in_proforma in proforma_product:
          if product_in_proforma.Proforma.id == pk:
            proforma_total_amount = proforma_total_amount + product_in_proforma.Total

    Proforma.objects.filter(id=pk).update(Total= proforma_total_amount)

    item2 = Proforma.objects.get(id=pk)
    total_after_discount = item2.Total - item2.discount
    context = {
        'proforma':proforma,
        'proforma_count':proforma_count,
        'proforma_product':proforma_product,

        'total_after_discount':total_after_discount,
        'proforma_total': proforma_total_amount,
        'id_proforma': pk,

        'invoice_product':invoice_product,
        'form': form,
        'query':query,
        'invoice': invoice,
        'invoice_count': invoice_count,
        'category': category,
        'category_count': category_count,

        'products': productss,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/proforma_edit_product.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def proformas_edit_product_add(request, proforma_pk, product_pk):
    item = Proforma.objects.get(id=proforma_pk)

    selectedProduct = Product.objects.get(pk=product_pk)

    quantityy = 0
    if request.GET.get('quantity') is  "" :#| request.GET.get('quantity') <= 0 :
      #quantityy = request.GET.get('quantity')
      quantityy = 1
      #messages.success(request, f'!!ALERT-The quantity must not be empty or 0 -ALERT!!')
      #return redirect('dashboard-invoices-edit-product', pk=invoice_pk)
      #Remove the quantity in the stock
      #Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))


      if ProformaProduct.objects.filter(Proforma__id=item.id, Product__id = selectedProduct.id).exists():
        #Remove the quantity in the stock
        #Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))

        #Modify the product in the invoice if the product exists in the invoice
        #product_in_invoice = InvoiceProduct.objects.get(productName=selectedProduct.name)
        product_in_proforma = ProformaProduct.objects.get(Proforma__id=item.id, Product__id = selectedProduct.id)
        ProformaProduct.objects.filter(Proforma__id=item.id, Product__id = selectedProduct.id).update(quantity= product_in_invoice.quantity + int(quantityy))

        product_in_proforma2 = ProformaProduct.objects.get(Proforma__id=item.id, Product__id = selectedProduct.id)
        ProformaProduct.objects.filter(Proforma__id=item.id, Product__id = selectedProduct.id).update(Total= product_in_proforma2.quantity * product_in_proforma2.price)
      else:
        #Remove the quantity in the stock
        #Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))

        #Adding the product to the invoice
        total = selectedProduct.price * quantityy
        proformaProduct = ProformaProduct(id=None, Proforma=item,
        Product = selectedProduct,
        productName=selectedProduct.name,
        quantity=  quantityy,#selectedProduct.quantity,
        price = selectedProduct.price,
        Total = total)

        proformaProduct.save()
      return redirect('dashboard-proformas-edit-product', pk=proforma_pk)
    else:
      quantityy = request.GET.get('quantity')

    #Remove the quantity in the stock
    #Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))

    if ProformaProduct.objects.filter(Proforma__id=item.id, Product__id = selectedProduct.id).exists():
      #Remove the quantity in the stock
      #Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))

      #Modify the product in the invoice if the product exists in the Proforma
      product_in_proforma = ProformaProduct.objects.get(Proforma__id=item.id, Product__id = selectedProduct.id)
      ProformaProduct.objects.filter(Proforma__id=item.id, Product__id = selectedProduct.id).update(quantity= product_in_proforma.quantity + int(quantityy))

      product_in_proforma2 = ProformaProduct.objects.get(Proforma__id=item.id, Product__id = selectedProduct.id)
      ProformaProduct.objects.filter(Proforma__id=item.id, Product__id = selectedProduct.id).update(Total= product_in_proforma2.quantity * product_in_proforma2.price)
    else:
      #Remove the quantity in the stock
      #Product.objects.filter(pk=product_pk).update(quantity=selectedProduct.quantity -int(quantityy))

      #Adding the product to the invoice
      total = selectedProduct.price * float(quantityy)
      proformaProduct = ProformaProduct(id=None, Proforma=item,
      Product = selectedProduct,
      productName=selectedProduct.name,
      quantity=  quantityy,#selectedProduct.quantity,
      price = selectedProduct.price,
      Total = total)

      proformaProduct.save()

    return redirect('dashboard-proformas-edit-product', pk=proforma_pk)




@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def proformas_edit_product_search(request, proforma_pk, proforma_product_pk):

    query = self.request.GET.get('q')

    return redirect('dashboard-proformas-edit-product', pk=proforma_pk)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def proformas_edit_product_finish(request, proforma_pk, proforma_product_pk):
  #Get the selected product in the invoice
  productProforma = ProformaInvoiceProduct.objects.get(id=proforma_product_pk)
  #productInvoice.price = 0.0;
  #productInvoice.save()
  productProforma.delete()
  return redirect('dashboard-proformas-edit-product', pk=proforma_pk)
  #return redirect('dashboard-index')



@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def proformas_edit_product_delete(request, proforma_pk, proforma_product_pk):
    #Get the selected product in the invoice
    productProforma = ProformaProduct.objects.get(id=proforma_product_pk)

    if request.GET.get('quantity2') is  "" :
      #Return the product in the stock if the product already exist
      if Product.objects.filter(name=productProforma.productName).exists():
        #Modify the product in the invoice if the product exists in the invoice
        product = Product.objects.get(name=productProforma.productName)

        #Product cannot be returned in stock
        #Product.objects.filter(name=productProforma.productName).update(quantity= product.quantity + productProforma.quantity)

        productProforma.delete()
        return redirect('dashboard-proformas-edit-product', pk=proforma_pk)
    else:
      quantityy = request.GET.get('quantity2')
      #Return the product in the stock if the product already exist
      if Product.objects.filter(name=productProforma.productName).exists():
        #Modify the product in the invoice if the product exists in the invoice
        product = Product.objects.get(name=productProforma.productName)

        #Product cannot be returned in stock
        #Product.objects.filter(name=productProforma.productName).update(quantity= product.quantity + int(quantityy))


        ProformaProduct.objects.filter(id=proforma_product_pk).update(quantity = productProforma.quantity - int(quantityy))

        proformaproduct = ProformaProduct.objects.get(id=proforma_product_pk)
        ProformaProduct.objects.filter(id=proforma_product_pk).update(Total = proformaproduct.quantity * proformaproduct.price)


    productProforma2 = ProformaProduct.objects.get(id=proforma_product_pk)
    if productProforma2.quantity == 0:
      #Delete the selectionned product
      productProforma2.delete()

    return redirect('dashboard-proformas-edit-product', pk=proforma_pk)








@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def proformas_delete(request, pk):
    item = Proforma.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-proformas')
    context = {'item': item}
    return render(request, 'dashboard/proforma_delete.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def proformas_printed(request, pk):
  #invoice = Invoice.objects.all()
  proforma_product = ProformaProduct.objects.all()
  proforma_to_be_printed = Proforma.objects.get(id=pk)

  total_after_discount = proforma_to_be_printed.Total - proforma_to_be_printed.discount

  context = {
            'total_after_discount':total_after_discount,
            'proforma': proforma_to_be_printed,
            'proforma_product': proforma_product
            }
  return render(request, 'dashboard/proforma_printed.html', context)





###########################################################
#Customer
@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customers(request):
    proforma = Proforma.objects.all().order_by('-id',)
    proforma_count = proforma.count()

    invoice = Invoice.objects.all().order_by('-id',)
    invoice_count = invoice.count()

    category = Category.objects.all().order_by('-id',)
    category_count = category.count()
    product = Product.objects.all().order_by('-id',)
    product_count = product.count()
    order = Order.objects.all().order_by('-id',)
    order_count = order.count()

    customer = Customer.objects.all()
    customer_count = customer.count()

    if request.method == 'POST':
       form = CustomerForm(request.POST)
       if form.is_valid():
          form.save()
          #product_category_name = form.cleaned_data.get('client')
          messages.success(request, f'A Customer has been added')
          return redirect('dashboard-customers')
    else:
        form = CustomerForm()

    context = {
        'proforma':proforma,
        'proforma_count':proforma_count,
        'form':form,
        'invoice': invoice,
        'invoice_count': invoice_count,
        'category': category,
        'category_count': category_count,
        'customer': customer,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/customers.html', context)

@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customers_edit(request, pk):
  item = Customer.objects.get(id=pk)

  if request.method == 'POST':
    form = CustomerForm(request.POST, instance=item)
    if form.is_valid():
      invoices = Invoice.objects.all()
      proformas = Proforma.objects.all()
      for invo in invoices:
        if invo.client.id == pk:
          invo.name_backup = form.cleaned_data.get("name")
          invo.email_backup = form.cleaned_data.get("email")
          invo.phone_backup = form.cleaned_data.get("phone")
          invo.address_backup = form.cleaned_data.get("address")
          invo.save()
      for profo in proformas:
        if profo.client.id == pk:
          profo.name_backup = form.cleaned_data.get("name")
          profo.email_backup = form.cleaned_data.get("email")
          profo.phone_backup = form.cleaned_data.get("phone")
          profo.address_backup = form.cleaned_data.get("address")
          profo.save()
      form.save()
      return redirect('dashboard-customers')

  else:
    form = CustomerForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/customers_edit.html', context)



@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customers_delete(request, pk):
    item = Customer.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-customers')
    context = {'item': item}
    return render(request, 'dashboard/customers_delete.html', context)


@login_required(login_url='user-login')
@allowed_users(allowed_roles=['Admin'])
def customer_detail(request, pk):
    proforma = Proforma.objects.all().order_by('-id',)
    proforma_count = proforma.count()

    invoice = Invoice.objects.all().order_by('-id',)
    invoice_count = invoice.count()

    category = Category.objects.all().order_by('-id',)
    category_count = category.count()

    #customer = User.objects.filter(groups=2)
    customer = Customer.objects.all()
    customer_count = customer.count()
    product = Product.objects.all().order_by('-id',)
    product_count = product.count()
    order = Order.objects.all().order_by('-id',)
    order_count = order.count()
    customers = User.objects.get(id=pk)
    context = {
        'proforma':proforma,
        'proforma_count':proforma_count,
        'invoice': invoice,
        'invoice_count': invoice_count,
        'category': category,
        'category_count': category_count,
        'customers': customers,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/customers_detail.html', context)




#order
@login_required(login_url='user-login')
def order(request):
    proforma = Proforma.objects.all().order_by('-id',)
    proforma_count = proforma.count()
    invoice = Invoice.objects.all().order_by('-id',)
    invoice_count = invoice.count()

    category = Category.objects.all().order_by('-id',)
    category_count = category.count()

    order = Order.objects.all().order_by('-id',)
    order_count = order.count()
    customer  = Customer.objects.all()
    customer_count = customer.count()
    product = Product.objects.all().order_by('-id',)
    product_count = product.count()

    context = {
        'proforma':proforma,
        'proforma_count':proforma_count,
        'invoice': invoice,
        'invoice_count': invoice_count,
        'category': category,
        'category_count': category_count,
        'order': order,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/order.html', context)
