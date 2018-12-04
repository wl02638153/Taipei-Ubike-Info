from django.conf.urls import url, include
from ubike.views import ubike_data, NB_IoT
from ubike.views import ubike_data_ORM, post_detail

urlpatterns = [
    url(r'^NB-IoT', NB_IoT, name='NB-IoT'),  # 訪問頁面
    # url(r'^ubike', ubike_data, name='ubike'),
    url(r'^ubike', ubike_data_ORM, name='ubike'),
    url(r'^Ubike_detail/(?P<pk>\d+)/$', post_detail, name='post_detail'),
]
