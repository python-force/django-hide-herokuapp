# -*- coding: utf-8 -*-
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path

from hide_herokuapp.views import herokuapp_robots_view


urlpatterns = [
    re_path(r'^robots\.txt$', herokuapp_robots_view),
]
