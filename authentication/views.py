from django.shortcuts import render, get_object_or_404
from .models import CustomUser

def index(request):
    return render(request, 'index.html')

def get_users(request):
    users = CustomUser.objects.all().order_by('id')
    context = {'users': users}
    return render(request, 'authentication/users.html', context)

def user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    context = {'user': user}
    return render(request, 'authentication/user.html', context)