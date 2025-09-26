from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('pages/', views.PageListView.as_view(), name='page_list'),
    path('pages/<int:pk>/', views.PageDetailView.as_view(), name='page_detail'),
    path('pages/create/', views.PageCreateView.as_view(), name='page_create'),
    path('pages/<int:pk>/edit/', views.PageUpdateView.as_view(), name='page_edit'),
    path('pages/<int:pk>/delete/', views.PageDeleteView.as_view(), name='page_delete'),
]
