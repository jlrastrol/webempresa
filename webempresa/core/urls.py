
from django.urls import path
from . import views as core_views

urlpatterns = [
    path('', core_views.home),
    path('about', core_views.about),
    path('services', core_views.services),
    path('store', core_views.store),
    path('contact', core_views.contact),
    path('blog', core_views.blog),
    path('sample', core_views.sample),

]
