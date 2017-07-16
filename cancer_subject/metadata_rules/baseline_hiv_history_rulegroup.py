from edc_metadata.rules.predicate import P
from edc_constants.constants import DWTA, NO
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules.crf.crf_rule import CrfRule
from edc_metadata.rules.crf import CrfRuleGroup


class BaselineHIVHistoryRuleGroup(CrfRuleGroup):

    has_hiv_result = CrfRule(
        predicate=P(
            'has_hiv_result',
            func=lambda has_smoked: True if has_smoked in [NO, DWTA] else False),
        consequence=NOT_REQUIRED,
        alternative=REQUIRED,
        target_models=['bhhhivtest'])

    had_who_illnesses = CrfRule(
        predicate=P('had_who_illnesses', 'eq', NO),
        consequence=NOT_REQUIRED,
        alternative=REQUIRED,
        target_models=['bhhwhoillness'])

    class Meta:
        app_label = 'cancer_subject'
        source_model = 'cancer_subject.baselinehivhistory'
