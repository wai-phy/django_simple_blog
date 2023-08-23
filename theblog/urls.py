from . import views
from django.urls import path
from .views import HomeView, ArticleDetailView, PostAddView

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>/',ArticleDetailView.as_view(), name ='article-detail'),
    path('add_post/',PostAddView.as_view(), name='add_post')
]
