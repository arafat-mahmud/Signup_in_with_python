from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name='login'),       # Login page
    path('signup/', views.sign_up, name='signup'),  # Sign-up page
    path('welcome/', views.welcome, name='welcome'),  # Welcome page
    path('logout/', views.logout_view, name='logout'),  # Logout route
]
