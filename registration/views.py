from django.shortcuts import render, redirect
from .forms import CompanyRegistrationForm

def register_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CompanyRegistrationForm()
    return render(request, 'register.html', {'form': form})

def success(request):
    return render(request, 'success.html')
