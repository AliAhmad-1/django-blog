from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.register,name='regitser'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.log_out,name='logout'),

    path('edit_profile/',views.edit_profile,name='edit-profile'),
    path('password_change/',views.password_change,name='password_change'),

    
]
