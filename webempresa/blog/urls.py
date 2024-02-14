
from django.urls import path
from . import views as blog_view

urlpatterns = [
    path('', blog_view.blog, name="blog"),
    path('category/<int:category_id>', blog_view.category, name="category")
]
