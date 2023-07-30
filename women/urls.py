from django.urls import path, re_path, include
from rest_framework import routers

# from women.views import WomenAPIUpdate, WomenAPIDetailView, CategoryAPIView, CategoryDetailView, WomenAPIList
from women.views import WomenViewSet

women_router = routers.DefaultRouter()
women_router.register(r'women', WomenViewSet, basename="women")
print(women_router.urls)

urlpatterns = [
    path('api/v1/', include(women_router.urls))
    # path('api/v1/woman/<int:pk>/', WomenAPIDetailView.as_view()),
    # path('api/v1/category/', CategoryAPIView.as_view()),
    # path('api/v1/category/<int:pk>/', CategoryAPIView.as_view()),
]
