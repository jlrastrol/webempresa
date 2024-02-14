

from django.urls import path
from . import views as service_view

urlpatterns = [
        path('', service_view.services, name="services"),
]

