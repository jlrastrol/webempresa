
from django.urls import path
from . import views as contact_view

urlpatterns = [
    path('', contact_view.contact, name="contact"),
]
