from django.shortcuts import render

def home(request):
    # Add logic to check if user is logged in
    if request.user.is_authenticated:
        message = "Welcome back! You are logged in."
    else:
        message = "Welcome! Please log in to access more features."
    return render(request, 'home.html', {'message': message})
