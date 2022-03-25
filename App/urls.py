from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/register/', RegisterFormView.as_view(), name='register'),
    path('note/all/', message_page, name='notes'),
    path('note/add/', add_message, name='add_note'),
]
