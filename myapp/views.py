from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import logout

# API endpoint
def api_data(request):
    data = {"message": "Hello, Django Backend!"}
    return JsonResponse(data)

# Frontend view
def frontend_view(request):
    return render(request, 'myapp/index.html')

# Home view
def home_view(request):
    return render(request, 'myapp/home.html')

# Signup view with debugging
def signup_view(request):
    print("Request method:", request.method)  # Debug request method (GET/POST)

    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Corrected assignment
        print("Form data (POST):", request.POST)  # Debug the submitted data
        print("Form is valid:", form.is_valid())  # Debug form validity

        if form.is_valid():
            user = form.save()  # Save the new user to the database
            print("New user created:", user)  # Debug the saved user
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to the login page
        else:
            print("Form errors:", form.errors)  # Debug validation errors
    else:
        print("Rendering blank form")  # Debug GET request
        form = UserCreationForm()  # Initialize a blank form for GET requests

    # Render the signup page for both GET and invalid POST requests
    return render(request, 'myapp/signup.html', {'form': form})

# Custom logout view
def custom_logout_view(request):
    logout(request)
    return redirect('/')
