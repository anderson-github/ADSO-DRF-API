from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista-productos/', views.ProductsView.as_view(), name='lista-productos'),
    path('<int:pk>/', views.index, name='index'),
]
