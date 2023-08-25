# from . import views
from django.urls import path
from .views import HomeView, ArticleDetailView, PostAddView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>/',ArticleDetailView.as_view(), name ='article-detail'),
    path('add_post/',PostAddView.as_view(), name='add_post'),
    path('article/edit/<int:pk>',PostUpdateView.as_view(), name='update_post' ),
    path('article/<int:pk>/delete',PostDeleteView.as_view(), name='delete_post')
]
