from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('propiedades/', views.propiedades_list, name='propiedades_list'),
    path('admin/login/', views.custom_login, name='login'),
    path('crud/propiedades/', views.crud_propiedades, name='crud_propiedades'),
    path('crud/corredores/', views.crud_corredores, name='crud_corredores'),
  
    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)