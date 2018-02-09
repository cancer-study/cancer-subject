app_name = 'cancer_subject'

from django.conf.urls import url
from django.views.generic.base import RedirectView

from .admin_site import cancer_subject_admin

urlpatterns = [
    url(r'^admin/', cancer_subject_admin.urls),
    url(r'', RedirectView.as_view(url='/'), name='home_url'),
]
