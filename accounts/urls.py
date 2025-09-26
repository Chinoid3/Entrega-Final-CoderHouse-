from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='edit_profile'),
    path('profile/edit-user/', views.edit_user_view, name='edit_user'),
    path('profile/change-password/', views.change_password_view, name='change_password'),
    path("inbox/", views.inbox_view, name="inbox"),
]
