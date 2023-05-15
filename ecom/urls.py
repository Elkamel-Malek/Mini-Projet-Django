from django.urls import path
from . import views

urlpatterns = [

path('logout', views.LogoutView.as_view(template_name='ecom/logout.html'), name='logout'),
]