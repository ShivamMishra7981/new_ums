from django.urls import path,include
from . import views
from .views import UserApiViewSet 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api',UserApiViewSet)

#used basename so that it does not overwrite the existing url
router.register(r'manager-api',views.ManagerViewSet,basename='managerapi')
router.register(r'executive-api',views.ExecutiveViewSet,basename='executive-api')

urlpatterns = [
    path("",views.home,name="home"),
    #-- API -- 
    path('',include(router.urls)),
    path('api/',include('rest_framework.urls')),
    #-- view-permission --
    # path("<int:id>/permissions/",views.view_user_permissions,name="user-permissions"),
]
