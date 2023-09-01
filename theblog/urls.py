# from . import views
from django.urls import path
from .views import CategoryListView, CategoryView, HomeView, ArticleDetailView, PostAddView, PostUpdateView, PostDeleteView,AddCategoryView

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('article/<int:pk>/',ArticleDetailView.as_view(), name ='article-detail'),
    path('add_post/',PostAddView.as_view(), name='add_post'),
    path('article/edit/<int:pk>',PostUpdateView.as_view(), name='update_post' ),
    path('add_category/',AddCategoryView.as_view(), name='add_category'),
    path('article/<int:pk>/delete',PostDeleteView.as_view(), name='delete_post'),
    path('category/<str:cats>/',CategoryView,name='category'),
    path('category-list/',CategoryListView,name='category_list'),
    # path('like/<int:pk>/',LikeView,name='like_post')
]
