from django.shortcuts import render, redirect, get_object_or_404
from .models import UserDetail
from .forms import UserDetailForm

# View to list all users
def user_list(request):
    users = UserDetail.objects.all()
    return render(request, 'users/user_list.html', {'users': users})

# View to create a new user
def user_create(request):
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to the list of users after creation
    else:
        form = UserDetailForm()
    return render(request, 'users/user_form.html', {'form': form})

# View to update an existing user
def user_update(request, pk):
    user = get_object_or_404(UserDetail, pk=pk)
    if request.method == 'POST':
        form = UserDetailForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')  # Redirect to the list of users after updating
    else:
        form = UserDetailForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

# View to delete a user
def user_delete(request, pk):
    user = get_object_or_404(UserDetail, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')  # Redirect to the list of users after deletion
    return render(request, 'users/user_confirm_delete.html', {'user': user})
