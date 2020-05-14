from . import views
from django.urls import path

urlpatterns = [
    path('', views.ProdList.as_view(), name='home'),
    path('<slug:slug>/', views.ProdDetail.as_view(), name='prod_detail'),
]