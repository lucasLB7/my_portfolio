from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
import datetime

from . import views

urlpatterns = [
    url(r'^$', views.home, name='PortfolioHome'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.projects_by_date,name = 'DatedProjects'),
    url(r'^search/',views.search_results, name='search_results'),
    url(r'^article/(\d+)',views.article,name='article')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)