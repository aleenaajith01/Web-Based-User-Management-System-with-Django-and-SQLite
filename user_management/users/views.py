from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
from .models import User
from users.models import User


def saveEnquiry(request):
    n=''
    if request.method=='POST':
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        phone_number=request.POST.get('phone_number')
        email=request.POST.get('email')
        address=request.POST.get('address')
        en=User(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email, address=address)
        en.save()
        n='Data Entered'
    return render(request, 'users/create_user.html',{'n':n})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_user')
    else:
        form = UserForm()
    return render(request, 'users/create_user.html', {'form': form})

# View to list all users
def list_users(request):
    users = User.objects.all()  # Retrieve all users
    return render(request, 'users/list_users.html', {'users': users})



# View to edit an existing user
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_user')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/edit_user.html', {'form': form, 'user': user})

def update_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_user')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/update_user.html', {'form': form, 'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('list_user')  # Redirect after deletion
    return render(request, 'users/confirm_delete.html', {'user': user})  # Render a confirmation template