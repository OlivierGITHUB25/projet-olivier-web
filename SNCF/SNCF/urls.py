from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appSNCF/', include('appSNCF.urls')),
    path('traitement/', views.traitement),
]
