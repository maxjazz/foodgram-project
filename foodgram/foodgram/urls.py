
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

flatpages_urls = [
        path('author/',
             views.flatpage,
             {'url': '/author/'},
             name='about_author'),
        path('tech/',
             views.flatpage,
             {'url': '/tech/'},
             name='about_tech'),
    ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("users.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('about/', include(flatpages_urls)),
    path('', include('foods.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += staticfiles_urlpatterns()
