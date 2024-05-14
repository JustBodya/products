from django.contrib import admin
from django.urls import path, include

from api.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
print(router.urls)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
