from django.urls import path
from . import views
from .views import ContactFormView

urlpatterns = [
 
    path('', ContactFormView.as_view(), name='contact'),
]
