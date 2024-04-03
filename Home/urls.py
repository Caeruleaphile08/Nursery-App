from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.land,name='land'),
    path('sign_up/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('first/', views.first, name='first'),
    path('citrus/', views.citrus, name='citrus'),
    path('berry/', views.berry, name='berry'),
    path('annuals/', views.annuals, name='annuals'),
    path('perinnials/', views.perinnials, name='perinnials'),
    path('biennials/', views.biennials, name='biennials'),
    path('airpurifier/', views.airpurifier, name='airpurifier'),
    path('contact/', views.contact, name='contact'),
    path('search-results/', views.search_plants_results, name='search_plants_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
