from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from user.api import UserListCreate
from blog.api import PostViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserListCreate)
router.register(r'posts', PostViewSet)  
router.register(r'categories', CategoryViewSet)  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("blog.urls", namespace="blog")),
    path("user/", include("user.urls", namespace="user")),
    path('api/', include(router.urls)), 
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
