from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello-viewsets',views.HelloViewset, basename='hello-viewset')
router.register('profile',views.UserProfilesViewset)

urlpatterns = [
    path('hello',views.HelloApiView.as_view(),name='hello'),
    path('',include(router.urls)),
]
