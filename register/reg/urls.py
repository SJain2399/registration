from django.urls import path
from reg import views
urlpatterns = [
    path('', views.signup,name='signup'),
    path('user_login/',views.user_login,name='user_login'),
]