from django.urls import path
from .views import api_data, home_view, signup_view, custom_logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('api/', api_data),  # Backend API endpoint
    path('', home_view, name='home'), 
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', custom_logout_view, name='logout'),  # Custom logout view
]
