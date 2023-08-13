from django.urls import path
from .views import UserRegisterView, UserProfileView,ListUserProfileView,DeleteUserProfileView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='user-profile'),
    path('user/listall',ListUserProfileView.as_view(),name='list_users'),
    path('delete/user/<int:pk>/',DeleteUserProfileView.as_view(),name='delete-user')
]
