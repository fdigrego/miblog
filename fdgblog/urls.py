from django.urls import path
from .views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('update_post/<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>/', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('category/<str:cats>/', CategoryView, name='categories'),
]
