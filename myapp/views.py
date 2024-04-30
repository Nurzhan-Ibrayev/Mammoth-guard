from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout



from .forms import CreationUserForm
from .models import Teacher

def registerPage(request):
    if request.user.is_authenticated:  # Check if user is already logged in
        return redirect("/")
    form = CreationUserForm()
    
    if request.method == "POST":
        form = CreationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    context = {'form': form}
    return render(request, "register.html", context)

def logoutPage(request):
    logout(request)
    return redirect("/login/")
    
# def loginPage(request):
#     if request.user.is_authenticated:  # Check if user is already logged in
#         return redirect("/")
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             request.session["log_user"] = username
#             return redirect("/")  # Redirect to home page
#         context = {'error': 'Invalid username or password'}
#         return render(request, 'login.html', context)
    
#     return render(request, 'login.html')
    
def loginPage(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session["log_user"] = username
                return redirect('/')
    return render(request, 'login.html', {'form': form})
