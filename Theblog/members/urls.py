from django.urls import path
from .views import UserList, UserView, ProfileList, ProfileView, MyObtainTokenPairView, RegisterView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('', UserList.as_view(), name='user-list'),
    path('<int:pk>/', UserView.as_view(), name='user-detail'),
    path('profile/', ProfileList.as_view(), name='profile-list'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile-detail'),
]