from django.urls import path, re_path, include
from rest_framework import routers

from women.views import WomenViewSet


router = routers.DefaultRouter()
router.register(r'women', WomenViewSet, basename='women')
print(router.urls)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update', 'delete': 'destroy'})),
]
