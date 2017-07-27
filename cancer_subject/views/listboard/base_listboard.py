from edc_base.utils import get_utcnow
from edc_base.view_mixins import EdcBaseViewMixin
from edc_constants.constants import MALE
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_dashboard.views import ListboardView


class BaseListboardView(AppConfigViewMixin, EdcBaseViewMixin, ListboardView):

    app_config_name = 'cancer_subject'
    navbar_item_selected = 'cancer_subject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            MALE=MALE,
            reference_datetime=get_utcnow())
        return context
