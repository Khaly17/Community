from django.urls import path

from .import views

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('member/<int:member_id>/', views.member_view, name ='member'),
    path('members/', views.members_view, name ='members')
]