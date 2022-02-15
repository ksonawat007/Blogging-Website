from django.contrib import admin
from django.urls import path, include
from accounts.views import register, Login,Logout, profile, dashboard, home
from blog.views import Create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register,name = 'Register'),
    path('profile/',profile,name="Profile"),
    path('login/',Login,name = 'Login'),
    path('logout/',Logout,name = 'Logout'),
    path('AddPost/',Create,name = 'AddPost'),
    path('Dashboard/',dashboard,name = 'Dashboard'),
    path('',home,name = "Home"),
]

