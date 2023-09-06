from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf.urls.static import static

port = ":8000" if not settings.DOCKER else ""
docs_url = f'http://127.0.0.1{port}/api/docs/'

urlpatterns = [
    path('', RedirectView.as_view(url=docs_url)),
    path('admin/', admin.site.urls),
    path('api/', include('news.urls')),
    path('api/', include('users.urls')),
    path('api/auth/token/', include('auth.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
