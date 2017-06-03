from django.conf.urls import url,include
from Monitor import views
urlpatterns = [
    url(r'^api/', include('Monitor.rest_urls')),
]