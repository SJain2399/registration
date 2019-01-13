from django.urls import path
from reg import views
urlpatterns = [
    path('', views.signup,name='signup'),
]