# project
from . import views
from django.urls import path


urlpatterns = [
    path('download/', views.get_file, {'add_attachment_headers': True},
        name='db_file_storage.download_file'),
    path('get/', views.get_file, {'add_attachment_headers': False},
        name='db_file_storage.get_file')
]
