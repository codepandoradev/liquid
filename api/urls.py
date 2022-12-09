import mimetypes

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

mimetypes.add_type('application/javascript', '.js')

urlpatterns = []

if settings.USE_BROWSABLE_API:
    urlpatterns += [
        path('__docs__/', SpectacularAPIView.as_view(), name='__docs__'),
        path('', SpectacularSwaggerView.as_view(url_name='__docs__')),
    ]

urlpatterns += [
    path('silk/', include('silk.urls', namespace='silk')),
    path('django_admin/', admin.site.urls),
    path('base/', include('app.base.urls')),
    path('user/', include('app.users.urls')),
    path('wallet/', include('app.wallet.urls')),
    path('management/', include('app.management.urls')),
    path('rigs/', include('app.rigs.urls')),
    path('support/', include('app.support.urls')),
    *static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

if settings.URL_PREFIX is not None:
    urlpatterns = [path(f'{settings.URL_PREFIX}/', include(urlpatterns))]
