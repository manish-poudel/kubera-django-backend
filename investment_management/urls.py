from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('stock/sector', views.sector_stock, name="sector_stock"),
    path('stock/<int:stock_id>/', views.stock_detail, name="stock_detail"),
    path('stock/group/alphabet', views.group_companies_by_alphabet, name='group_companies_by_alphabet'),
    path('add', views.add, name = "add"),
    path('stock/stats',views.company_stats, name="company_stats"),
]
