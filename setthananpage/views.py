from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def setthananpage_index_view(request):
    '''This function render index page of ecommerce views'''
    return HttpResponse('Welcome to 6410742537 Setthanan Thitathanapat HomePage!!')

def setthananpage_category_view(request):

    return HttpResponse('Welcome to 6410742537 Setthanan Thitathanapat Catagory!!')

def setthananpage_product_view(request):
    
    return HttpResponse('Welcome to 6410742537 Setthanan Thitathanapat Product!!')

def setthananpage_checkout_view(request):
    
    return HttpResponse('Welcome to 6410742537 Setthanan Thitathanapat Checkout!!')


def setthananpage_contact_view(request):
    
    return HttpResponse('Welcome to 6410742537 Setthanan Thitathanapat Contact!!')
