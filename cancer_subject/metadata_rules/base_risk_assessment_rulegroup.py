from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.rules import CrfRule
from edc_metadata.rules.crf import CrfRuleGroup
from edc_metadata.rules.predicate import P
from edc_constants.constants import DECLINED, NO


class BaseRiskAssessmentRuleGroup(CrfRuleGroup):

    has_smoked = CrfRule(
        predicate=P(
            'has_smoked',
            func=lambda has_smoked: True if has_smoked in [NO, DECLINED] else False),
        consequence=NOT_REQUIRED,
        alternative=REQUIRED,
        target_models=['baseriskassessmentsmoking'])

    has_worked_mine = CrfRule(
        predicate=P(
            'has_worked_mine',
            func=lambda has_worked_mine: True if has_worked_mine in [NO, DECLINED] else False),
        consequence=NOT_REQUIRED,
        alternative=REQUIRED,
        target_models=['baseriskassessmentsmoking'])

    has_worked_mine = CrfRule(
        predicate=P(
            'has_alcohol',
            func=lambda has_alcohol: True if has_alcohol in [NO, DECLINED] else False),
        consequence=NOT_REQUIRED,
        alternative=REQUIRED,
        target_models=['baseriskassessmentsmoking'])

    class Meta:
        app_label = 'cancer_subject'
        source_model = 'cancer_subject.baseriskassessment'


# class GenderRuleGroup(RuleGroup):
#
#     gender = ScheduledDataRule(
#         logic=Logic(
#             predicate=('gender', 'equals', 'm'),
#             consequence='not_required',
#             alternative='new'),
#         target_model=['baseriskassessmentfemale'])
#
#     class Meta:
#         app_label = 'cancer_subject'
#         source_fk = None
#         source_model = RegisteredSubject
# site_rule_groups.register(GenderRuleGroup)
