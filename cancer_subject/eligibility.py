from django.apps import apps as django_apps

from edc_constants.constants import YES, NO, POS

from .constants import ABLE_TO_PARTICIPATE


class AgeEvaluator:

    def __init__(self, age=None, guardian=None, adult_lower=None,
                 adult_upper=None, minor_lower=None, minor_upper=None):
        app_config = django_apps.get_app_config('cancer_screening')
        adult_lower = adult_lower or app_config.eligibility_age_adult_lower
        adult_upper = adult_upper or app_config.eligibility_age_adult_upper
        minor_lower = minor_lower or app_config.eligibility_age_minor_lower
        minor_upper = minor_upper or app_config.eligibility_age_minor_upper
        self.reason = None
        self.eligible = None
        if adult_lower <= age <= adult_upper:
            self.eligible = True
        elif minor_lower <= age <= minor_upper and guardian == YES:
            self.eligible = True
        else:
            self.eligible = False

        if not self.eligible:
            if age < adult_lower:
                if minor_lower <= age <= minor_upper and guardian == NO:
                    self.reason = f'Minor of age: {age}'' with no guardian.'
                else:
                    self.reason = f'age<{adult_lower}'
            elif age > adult_upper:
                self.reason = f'age>{adult_upper}'


class CitizenshipEvaluator:

    def __init__(self, citizen=None, legal_marriage=None,
                 marriage_certificate=None):
        self.eligible = None
        self.reason = None
        if (citizen == YES) or (
                citizen == NO and marriage_certificate == YES and
                legal_marriage == YES):
            self.eligible = True
        else:
            self.eligible = False

        if not self.eligible and citizen == NO:
            if legal_marriage == YES and marriage_certificate == NO:
                self.reason = ('Not a citizen, married to a citizen but does '
                               'not have a marriage certificate.')
            elif legal_marriage == NO:
                self.reason = 'Not a citizen and not married to a citizen..'


class CancerStatusEvaluator:

    def __init__(self, cancer_status=None):
        self.eligible = None
        self.reason = None
        if cancer_status == YES:
            self.eligible = True
        else:
            self.eligible = False
            self.reason = 'Participant Does not Have Cancer.'


class ParticipationEvaluator:

    def __init__(self, participation=None):
        self.eligible = None
        self.reason = None
        if participation == ABLE_TO_PARTICIPATE:
            self.eligible = True
        else:
            self.eligible = False
            self.reason = f'Not able participant {participation}.'


class LiteracyEvaluator:

    def __init__(self, literate=None, guardian=None):
        self.eligible = None
        self.reason = None
        if literate == YES or (
                literate == NO and guardian == YES):
            self.eligible = True
        else:
            self.eligible = False

        if not self.eligible:
            if literate == NO and (not guardian or guardian == NO):
                self.reason = 'Illiterate with no literate witness.'


class Eligibility:

    def __init__(self, age=None, literate=None, guardian=None,
                 legal_marriage=None, marriage_certificate=None, citizen=None,
                 cancer_status=None, participation=None):

        self.age_evaluator = AgeEvaluator(age=age, guardian=guardian)
        self.cancer_status_evaluator = CancerStatusEvaluator(
            cancer_status=cancer_status)
        self.citizenship = CitizenshipEvaluator(
            citizen=citizen, legal_marriage=legal_marriage,
            marriage_certificate=marriage_certificate)
        self.literacy_evaluator = LiteracyEvaluator(
            literate=literate, guardian=guardian)
        self.participation_evaluator = ParticipationEvaluator(
            participation=participation)
        self.criteria = dict(
            age=self.age_evaluator.eligible,
            citizen=self.citizenship.eligible,
            literate=self.literacy_evaluator.eligible,
            participation=self.participation_evaluator.eligible,
            cancer_status=self.cancer_status_evaluator.eligible)
        self.eligible = all(self.criteria.values())

    @property
    def reasons(self):
        """Returns a list of reason not eligible.
        """
        reasons = [k for k, v in self.criteria.items() if not v]
        if self.citizenship.reason:
            reasons.pop(reasons.index('citizen'))
            reasons.append(self.citizenship.reason)
        if self.literacy_evaluator.reason:
            reasons.pop(reasons.index('literate'))
            reasons.append(self.literacy_evaluator.reason)
        if self.age_evaluator.reason:
            reasons.pop(reasons.index('age'))
            reasons.append(self.age_evaluator.reason)
        if self.cancer_status_evaluator.reason:
            reasons.pop(reasons.index('cancer_status'))
            reasons.append(self.cancer_status_evaluator.reason)
        if self.participation_evaluator.reason:
            reasons.pop(reasons.index('participation'))
            reasons.append(self.participation_evaluator.reason)
        return reasons
