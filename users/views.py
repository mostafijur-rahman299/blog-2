from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import UserProfile

from blog.models import Post 

# User Registration section
def user_register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "Account has been Created.Now you can login!")
            return redirect('blog:home-page')
    else:
        register_form = RegistrationForm()
    return render(request, 'users/register.html', {"form": register_form})

# User Settings section 
@login_required
def request_user_profile(request):
    obj = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated!")
            return redirect("users:user-profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'object': obj,
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)



# User Profile Detail section
def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    object1 = UserProfile.objects.get(user=user)
    object2 = Post.objects.filter(author=user)
    return render(request, "users/user_profile.html", {"object": object1, "object2": object2})

