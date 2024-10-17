from django.contrib import admin
from django.urls import path, include
from api.views import BooksViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'books',BooksViewSet)


urlpatterns = [

    path('', include(router.urls))
    # path('admin/', admin.site.urls),
]