from django.urls import path
from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.message_list, name='message_list'),
    path('conversation/<int:conversation_id>/', views.conversation_detail, name='conversation'),
    path('start/', views.start_conversation, name='start_conversation'),
]
