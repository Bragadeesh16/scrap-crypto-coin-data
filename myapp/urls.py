from django.urls import path
from . import views
urlpatterns = [
    path('scraping-data',views.scraping_data.as_view() ,name='scraping_data'),
    path('scraping-detail/<int:pk>',views.scraping_detail,name='scraping_detail'),
    path('start_scraping/<int:pk>/', views.scraping_detail, name='scraping_detail')
]