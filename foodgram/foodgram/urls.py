
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.flatpages import views
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("users.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += staticfiles_urlpatterns()

flatpages_urls = [
        path('author/', views.flatpage, {'url': '/author/'}, name='about_author'),
        path('tech/', views.flatpage, {'url': '/tech/'}, name='about_tech'),
    ]

urlpatterns += [
    path('about/', include(flatpages_urls)),

]
urlpatterns += [
    path('', include('foods.urls'))
]
