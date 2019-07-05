from django.urls import path, include
from . import views
app_name = 'wall'


urlpatterns = [
    path('', views.home, name='home_page'),
    path('r/', views.search, name='search'),
    path('i/', views.images, name='images_page'),
    path('p/<pic_id>', views.picture, name='picture_page'),
    path('c/', views.catlog, name='catlog_page'),
    path('e/', views.explore, name='explore_page'),
    path('c/<cat_item>/', views.catlog_search, name='catlog_search'),

]
