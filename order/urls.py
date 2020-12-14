from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    # Order page
    path('orders/', views.orders, name='orders'),
    path('orders/<int:order_id>/', views.order, name='order'),
    path('user_orders/<int:user_id>/', views.user_orders, name='user_orders'),
    path('orders/books/<int:book_id>/', views.book_orders, name='book_orders')
]