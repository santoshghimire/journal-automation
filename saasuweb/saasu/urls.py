from django.conf.urls import url

from .views import CSVCreateView
from . import views
app_name = 'saasu'

urlpatterns = [

    url(r'^$', CSVCreateView.as_view(), name='csvupload'),


    ]
