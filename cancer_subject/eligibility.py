from edc_constants.constants import YES


class CancerStatusEvaluator:

    def __init__(self, cancer_status=None):
        self.eligible = None
        if cancer_status == YES:
            self.eligible = True
        else:
            self.eligible = False


class Eligibility:

    def __init__(self, cancer_status=None):
        self.cancer_status_evaluator = CancerStatusEvaluator(
            cancer_status=cancer_status)
        self.criteria = dict(
            cancer_status=self.cancer_status_evaluator.eligible)
        self.eligible = all(self.criteria.values())
