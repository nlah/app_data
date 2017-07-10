
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^data_array', views.data_array, name='data_array'),
    url(r'^add_upc', views.add_upc, name='add_upc'),
    url(r'^del_upc', views.del_upc, name='del_upc'),
    url(r'^add_file_csv', views.add_file_csv, name='add_file_csv'),
    url(r'^download_example', views.download_example, name='download_example'),
    url(r'^download', views.download, name='download'),
    url(r'^settings', views.settings, name='settings'),

]
