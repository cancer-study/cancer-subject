from edc_metadata.rules.predicate import P, PF
from edc_constants.constants import POS, NEG, UNK
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules.crf.crf_rule import CrfRule
from edc_metadata.rules.crf import CrfRuleGroup


class BHHHivTestRuleGroup(CrfRuleGroup):

    has_hiv_result = CrfRule(
        predicate=P('hiv_result', 'eq', POS),
        consequence=NOT_REQUIRED,
        alternative=REQUIRED,
        target_models=[f'{app_label}.haartrecord'])

    also_hiv_result = CrfRule(
        predicate=PF(
            'hiv_result',
            func=lambda hiv_result: True if hiv_result in [NEG, UNK] else False),
        consequence=NOT_REQUIRED,
        alternative=REQUIRED,
        target_models=[f'{app_label}.haartrecord'])

    class Meta:
        app_label = 'cancer_subject'
        source_model = f'{app_label}.bhhhivtest'
