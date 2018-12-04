"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from trips.views import home, post_detail
from django.conf import settings
from django.conf.urls.static import static
from users.views import index
# from ubike.views import ubike_data, NB_IoT

urlpatterns = [
                  url('admin/', admin.site.urls),
                  url(r'^', include('musics.urls')),
                  url(r'^users/', include('users.urls')),
                  url(r'^users/', include('django.contrib.auth.urls')),
                  url(r'^$', index, name='index'),  # 首頁
                  url(r'^', include('ubike.urls')),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
