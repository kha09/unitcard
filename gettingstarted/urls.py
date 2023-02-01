from django.urls import path, include
from django.contrib import admin
from unitcard.views import *
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name='home'),
    path("ar", home_arabic, name='home_arabic'),
    path("card", card, name='card'),
    path('<int:id>', file_detail, name="file_detail"),

]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)