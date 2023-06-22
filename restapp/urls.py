from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello-viewsets',views.HelloViewset, basename='hello-viewset')
router.register('profile',views.UserProfilesViewset)
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello',views.HelloApiView.as_view(),name='hello'),
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
]
