from django.urls import path

from . import views

app_name = 'msgs'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:msgform_id>/new/', views.new, name='new'),
    path('save_message/', views.save_message, name='save_message'),
]
