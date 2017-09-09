from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^todos/', include('todos.urls')),
    url(r'^', include('todos.urls')),
]
