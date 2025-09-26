from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.message_list, name='message_list'),
    path('inbox/', views.InboxView.as_view(), name='inbox'),
    path('sent/', views.SentMessagesView.as_view(), name='sent'),
    path('send/', views.MessageCreateView.as_view(), name='send'),
    path('message/<int:pk>/', views.MessageDetailView.as_view(), name='detail'),
]
