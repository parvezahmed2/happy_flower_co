from django.contrib import admin
from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, UserLgoutView, UserUpdateView
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
     
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLgoutView.as_view(), name='logout'),
    path('ragister/<uid64>/<token>/', views.activate, name='activate'),
]
 