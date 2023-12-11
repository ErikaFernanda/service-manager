from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register("", views.LoginViewSet, basename="login")

urlpatterns = [
    path('', include(router.urls)),
    # path('login/<int:pk>/', views.LoginViewSet.as_view({'get': 'get', 'post': 'post'}), name='login'),
    # path('login/', views.LoginViewSet.as_view({'get': 'list'}), name='login'),
    path('user', views.UserListView.as_view(),name= 'user'),
    # path('logout/<int:id_company>/',  LogoutView.as_view(), name='logout'),
    # path('logout/<int:id_company>/',  views.logout_view, name='logout')

    # router.register("", views.LoginViewSet, basename="login")
    # router.register("", views.RefreshViewSet, basename="refresh")
    # router.register("", views.PasswordAdjustViewSet, basename="password")
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
