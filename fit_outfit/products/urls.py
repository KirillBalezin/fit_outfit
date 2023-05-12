from django.urls import path

from . import views

app_name = 'products'

urlpatterns = [
     path('', views.index, name='index'),
     path('categories/', views.categories, name='categories'),
     path('category/<slug:slug>/', views.category_products,
          name='category_list'),
     path('create_product/', views.product_create, name='create_product'),
     path('create_category/', views.category_create, name='create_category'),
     path('<int:product_id>/edit/', views.product_edit,
          name='product_edit'),
     path('<int:product_id>/', views.product_detail,
          name='product_detail'),
     path('<int:product_id>/delete/', views.product_delete,
          name='product_delete'),
     path(r'(?P<int:product_id>\d+)/(?P<field>\d+)/(?P<sign>\d+)/quantity/',
          views.product_quantity, name='product_quantity'),
]
