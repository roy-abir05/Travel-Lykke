from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.
def register(request):
    print("Register view called", request.method)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account created for {user.username}! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below\n{}'.format(form.errors))
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile_view(request):
    if request.method == 'POST':
        user = request.user
        profile = user.profile

        # Update User fields
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.save()

        # Update Profile fields
        profile.phone_number = request.POST.get('phone_number', profile.phone_number)
        if 'profile_image' in request.FILES:
            profile.profile_image = request.FILES['profile_image']
        profile.save()

        messages.success(request, 'Your profile has been updated!')
        return redirect('profile')

    return render(request, 'users/profile.html')

class CustomPasswordChangeView(PasswordChangeView):
    template_name = "users/change_password.html"
    success_url = reverse_lazy("profile") 