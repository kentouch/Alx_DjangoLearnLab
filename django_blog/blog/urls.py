from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.index, name='index'),
    path('about/', views.HomeView.about, name='about'),
    path('login/', views.HomeView.login, name='login'),
    path('logout', views.HomeView.logout, name='logout'),
    path('register/', views.HomeView.register, name='register'),
    path('profile/', views.HomeView.profile, name='profile'),
    # Post urls
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-updated'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    # Comment urls
    path('posts/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment-updated'),
    path('comment/<int:pk>/delete/', views.CommentUpdateView.as_view(), name='comment-delete')
]