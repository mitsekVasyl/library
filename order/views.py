from django.shortcuts import render, get_object_or_404
from .models import Order
# Create your views here.


def order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    context = {'order': order}
    return render(request, 'order/order.html', context)


def orders(request):
    orders = Order.objects.all().order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'order/orders.html', context)

def user_orders(request, user_id):
    orders = Order.objects.filter(user=user_id).order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'order/userorders.html', context)

def book_orders(request, book_id):
    orders = Order.objects.filter(book=book_id).order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'order/orders.html', context)