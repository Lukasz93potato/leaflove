from django.urls import path
from . import views
from .views import *
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
     path('home/', views.HomeView.as_view(), name ='home'),
     path('logout/', views.LogoutView.as_view(), name ='logout'),
     path('register/', RegisterView.as_view(), name='register'),
     path('login/', login_page, name='login_page'),
     path('token/',
          jwt_views.TokenObtainPairView.as_view(),
          name ='token_obtain_pair'),
     path('token/refresh/',
          jwt_views.TokenRefreshView.as_view(),
          name ='token_refresh')
]