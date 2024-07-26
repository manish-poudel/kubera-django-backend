from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('stock/sector', views.sector_stock, name="sector_stock"),
    path('stock/<int:stock_id>/', views.stock_detail, name="stock_detail"),
    path('stock/<str:exchange>/group/alphabet', views.group_companies_by_alphabet, name='group_companies_by_alphabet'),
    path('stock/<str:exchange>/stats', views.company_stats, name='company_stats'),
    path('stock/<str:exchange>/fundamentals/historical/<str:ftype>', views.get_fundamental_data, name='get_fundamental_data'),
    path('add', views.add, name='add'),
]