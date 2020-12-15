from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('api/<int:pk>/', views.ContactUpdateAPIView.as_view(), name='update'),
    path('api/', views.ContactListView.as_view(), name='list'),
    # re_path('api/(?P<pk>[0-9]+)/?$', views.ContactUpdateAPIView.as_view(), name = 'update')
]