from django.contrib import admin
from django.urls import path, include

from api.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/product/', ProductAPIList.as_view()),
    path('api/v1/product/<int:pk>/', ProductAPIUpdate.as_view()),
    path('api/v1/productdelete/<int:pk>/', ProductAPIDestroy.as_view()),
]
