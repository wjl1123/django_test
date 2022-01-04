from django.urls import path
from .views import *

app_name = 'photo'

urlpatterns = [
    path('', photo_list, name='photo_list'),
    path('detail/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]
