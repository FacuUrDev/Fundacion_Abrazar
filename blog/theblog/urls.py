from django.urls import path
from .views import AddPostView, ArticleView, DeletePostView, HomeView, AddPostView, EditPostView, AddCategoryView, CategoryView, CategoryListView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleView.as_view(), name="article"),
    path('add/', AddPostView.as_view(), name="add"),
    path('category/', AddCategoryView.as_view(), name="category"),
    path('article/edit/<int:pk>', EditPostView.as_view(), name="edit"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete"),
    path('category/<str:cats>', CategoryView, name="category"),
    path('category-list/', CategoryListView, name="category-list"),

]
