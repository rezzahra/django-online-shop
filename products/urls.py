from django.urls import path
from .import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products_list'),
    path('<int:pk>/', views.ProductDietailView.as_view(), name='detial'),
    path('comment/<int:pk>/', views.CreateCommentForm.as_view(), name='comment_create')
]