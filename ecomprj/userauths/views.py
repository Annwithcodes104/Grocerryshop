from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def register_view(request):
    form = UserRegisterForm()  # Define form outside the if-else block
    if request.method == 'POST':
        form = UserRegisterForm(request.POST )
        if form.is_valid():
            
            print('registered successfully')
            new_user=form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f"Hey {username},sign-up successfully")
            new_user=authenticate(username=form.cleaned_data['email'],
                                  password=form.cleaned_data['password1'])
            login(request,new_user)
            return redirect('index')
    else:
        print('user cannot be register')

    context = {
        'form': form
    }

    return render(request, 'userauths/login.html', context)

def loginView(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method=='POST':
        email=request.POST.get()
