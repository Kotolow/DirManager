from django.urls import include, path
from mainapp import views

urlpatterns = [
    path('files/', views.files_api, name='files_api'),
    path('filtered_files/', views.filtered_files_api, name='filtered_files_api'),
    path('fill_db/', views.fill_db_api, name='fill_db_api'),
]
