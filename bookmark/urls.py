from django.urls import path
from django.contrib.auth import views as auth_view
from .views import *
from accounts import forms

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    #  2nd url       View               template name
    path("add/", BookmarkCreateView.as_view(), name='add'),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name='detail'),
    # int:pk  =  (primary key) 북마크의 글번호!, 슬러그 형태 (함수이름같이 만든거 how to press)
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name='update'),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name='delete'),
]
