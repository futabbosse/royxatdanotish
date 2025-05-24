from django.shortcuts import render, redirect
from .forms import UserProfileForm



def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserProfileForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request , 'success.html')