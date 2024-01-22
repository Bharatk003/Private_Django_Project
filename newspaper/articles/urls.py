from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    CommentCreateView,
    )

urlpatterns = [

    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', CommentCreateView.as_view(), name='article_new'),
    path('comment/<int:pk>/', CommentCreateView.as_view(), name = 'comment'),
    path('', ArticleListView.as_view(), name='article_list'),

]