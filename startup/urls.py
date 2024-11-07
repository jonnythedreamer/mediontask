from rest_framework import routers
from .views import CustomUserViewSet
from django.urls import path, include, re_path
from . import views

router = routers.DefaultRouter()
router.register(r'customusers', CustomUserViewSet)

#urlpatterns = router.urls

urlpatterns = [
  #urlpatterns = router.urls
    path('api/customusers', views.customuser_list),
    path('api/professions', views.profession_list),
    path('api/permissions', views.permission_list),
    re_path('api/customusers/(?P<pk>[0-9]+)', views.customuser_detail),
    path('api/customusers/fired', views.customuser_list_fired)
]
