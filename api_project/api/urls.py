# let's make a url that directs to the view

from django.urls import path, include
from .views import BookViewSet, BookList
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('api/books/', BookList.as_view(), name= 'BookListView'),
    path('', BookViewSet.as_view({'get': 'list'}), name= 'BookListView'),
    path('api/books/<int:pk>/', BookViewSet.as_view({'get': 'retrieve'}), name= 'BookDetailView'),
    path('api/books/<int:pk>/update/', BookViewSet.as_view({'put': 'update'}), name= 'BookUpdateView'),
    path('api/books/<int:pk>/delete/', BookViewSet.as_view({'delete': 'destroy'}), name= 'BookDeleteView'),
    path('api/books/create/', BookViewSet.as_view({'post': 'create'}), name= 'BookCreateView'),
    path('api/auth/', obtain_auth_token, name= 'AuthToken'),
    path('api/', include(router.urls))
]