from django.urls import include, path
from mainapp import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('files/', views.files_api, name='files_api'),
    path('filtered_files/', views.filtered_files_api, name='filtered_files_api'),
    path('fill_db/', views.fill_db_api, name='fill_db_api'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
