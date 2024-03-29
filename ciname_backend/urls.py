from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('categorys/', include('categories.urls')),
    path('cart/', include('cart.urls')),
    path('review/', include('review.urls')),
]

# for image
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)