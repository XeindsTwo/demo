from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path
from users.views import register_view, login_view, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
