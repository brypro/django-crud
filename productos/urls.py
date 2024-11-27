from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('listar/', views.listar_productos, name='listar_productos'),
    path('actualizar/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
