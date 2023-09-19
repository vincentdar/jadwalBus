from django.urls import path   
from . import views

urlpatterns = [
    path('bus_routes/', views.RouteList, name="RouteList"),
    path('bus_routes/<int:pk>/', views.RouteDetail, name="RouteDetail"),
    path('bus_routes/add/', views.AddRoute, name="AddRoute"),
    path('bus_routes/update/<int:pk>/', views.UpdateRoute, name="UpdateRoute"),
    path('bus_routes/delete/<int:pk>/', views.DeleteRoute, name="DeleteRoute"),
]