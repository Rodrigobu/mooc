from django.conf.urls import url
from .views import home
from .views import contact

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contato/$', contact, name='contact')
]
