from django.urls import path,URLPattern

from . import views

app_name = 'tienda'
urlpatterns = [
    path('', views.index, name='index'),
    path('producto/<int:producto_id>/', views.producto, name='producto'),
    path('categoria/<int:categoria_id>/', views.detalles, name='categoria')
]