from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/<int:id_company>/', views.login_view, name='login'),
    path('user', views.UserListView.as_view(),name= 'user'),
    # path('logout/<int:id_company>/',  LogoutView.as_view(), name='logout'),
    path('logout/<int:id_company>/',  views.logout_view, name='logout')
]
