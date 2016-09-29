from django.conf.urls import url

from .views import CSVCreateView

app_name = 'saasuweb'

urlpatterns = [

    url(r'^$', CSVCreateView.as_view(), name='csvupload'),


    ]