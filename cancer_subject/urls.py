import sys
from django.conf.urls import url

from .admin_site import cancer_subject_admin

app_name = 'cancer_subject'

urlpatterns = [
    url(r'^admin/', cancer_subject_admin.urls)]
