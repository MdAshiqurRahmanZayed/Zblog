from unicodedata import name
from django.urls import path, include
from .views import ArticleDetailView, HomeView, AddPostView, UpdatePostView, DeletePostView, AddCategotyView, CategoryView, CategoryListView, LikeView, AddCommentView
# from .views import CategoryView, CategoryListView, LikeView
# from . import views
from django.urls import path, re_path
urlpatterns = [
    # path('', views.home,name="home"),
    path('',HomeView.as_view(),name='home'),
    path('article/<int:pk>',ArticleDetailView.as_view(),name='article-detail'),
    path('add_post/', AddPostView.as_view(),name='add_post'),
    path('add_category/', AddCategotyView.as_view(),name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    # path('categories/<str:cats>', CategoryView, name='category'),
    path('categories/<str:cats>/', CategoryView, name='category'),
    path('categories-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),

]
