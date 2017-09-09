from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^details/(?P<todo_id>\d+)/$',views.detail,name='detail'),
    url(r'^add/$',views.add,name='add'),
]
