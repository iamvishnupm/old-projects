from django.shortcuts import render, redirect, get_object_or_404
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def home(request, c_slug=None):
    categ = None
    pd = None
    if(c_slug):
        categ = get_object_or_404(Categories, slug=c_slug)
        pd=product.objects.filter(category=categ, availability=True)
    else:
        pd = product.objects.all().filter(availability=True)
    
    categories = Categories.objects.all()
    paginator = Paginator(pd, 3)
    
    page_no = int(request.GET.get('page', '1'))
    
    try:
        page = paginator.page(page_no)
    except(EmptyPage, InvalidPage):
        page = paginator.page(paginator.num_pages)

    return render(request, "index.html", {
        "categories" : categories,
        "page" : page,
    })

def details(request, c_slug, p_slug):
    try:
        pd = product.objects.get(category__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    return render(request, "details.html", {
        "product" : pd,
    })


def search(request):
    if 'search' in request.GET:
        query = request.GET.get('search')
        pd = product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    else:
        return redirect("/")
    return render(request, 'search.html', {
        "products" : pd,
    })

def cart(request):
    cart = Cart.objects.all()
    total_amount = 0
    for item in cart:
        total_amount += item.price
    return render(request, "cart.html", {
        'cart' : cart,
        'total' : total_amount,
    })


def add_to_cart(request, id):
    pd = product.objects.get(id=id)
    try:
        item = Cart.objects.get(pd=pd)
        item.qty += 1
        item.set_price()
        item.save()
    except:
        item = Cart.objects.create(pd=pd, qty=1)

    return redirect(request.META.get("HTTP_REFERER"))


def remove_from_cart(request, id):
    pd = product.objects.get(id=id)
    item = Cart.objects.get(pd=pd)
    item.qty -= 1
    if(item.qty == 0):
        item.delete()
    else:
        item.set_price()
        item.save()
    return redirect(request.META.get("HTTP_REFERER"))

def delete_item(request, id):
    pd = product.objects.get(id=id)
    item = Cart.objects.get(pd=pd)
    item.delete()
    return redirect("/cart/")


