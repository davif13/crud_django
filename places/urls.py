from django.urls import path

from places import views

app_name = 'places'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('<int:place_id>/detail', views.detail, name='detail'),
    path('<int:place_id>/delete/', views.delete, name='delete'),
    path('upsert', views.upsert, name='upsert'),
]