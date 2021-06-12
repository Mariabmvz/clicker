from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('temp/call_click/', views.call_click),
    path('temp/update_boost/', views.update_boost),
    path('register/', views.register, name='register'),
    path('accounts/profile/', RedirectView.as_view(pattern_name="index")),
]