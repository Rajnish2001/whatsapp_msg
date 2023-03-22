from django.urls import path
from .views import Index, WhatsAppAPI

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('webhook', WhatsAppAPI.as_view(), name='webhook'),
]