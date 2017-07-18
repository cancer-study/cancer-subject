from edc_metadata.rules import PredicateCollection
from edc_constants.constants import YES


class Predicates(PredicateCollection):

    app_label = 'cancer_subject'
    
    def func_oncology_plan(self, visit, **kwargs):
        try:
            model_cls = self.get_model('oncologytreatmentplan')
            model_cls.objects.get(subject_visit=visit, radiation_plan=YES)
        except model_cls.DoesNotExist:
            return False
        return True
    
    
    def func_oncology_record(self, visit, **kwargs):
        try:
            model_cls = self.get_model('oncologytreatmentrecord')
            model_cls.objects.get(subject_visit=visit, radiation_received=YES)
        except model_cls.DoesNotExist:
            return False
        return True
    
    
    def func_oncology(self, visit, **kwargs):
        show_radiation_treatment = False
        if self.func_oncology_plan(visit) and self.func_oncology_record(visit):
            show_radiation_treatment = True
        elif not self.func_oncology_plan(visit) and self.func_oncology_record(visit):
            show_radiation_treatment = True
        elif self.func_oncology_plan(visit) and not self.func_oncology_record(visit):
            show_radiation_treatment = True
        elif not self.unc_oncology_plan(visit) and not self.func_oncology_record(visit):
            show_radiation_treatment = False
        return show_radiation_treatment
    
    def func_haematology(self, visit, **kwargs):
        haematology = self.get_model('resultstorecord').objects.get(
            name='haematology')
        try:
            model_cls = self.get_model('cancerdiagnosis')
            self.get_model('cancerdiagnosis').objects.get(
                subject_visit=visit, results_to_record__in=[haematology])
        except model_cls.DoesNotExist:
            return False
        return True
    
    
    def func_chemistry(self, visit, **kwargs):
        chemistry = self.get_model('resultstorecord').objects.get(
            name='chemistry')
        try:
            model_cls = self.get_model('cancerdiagnosis')
            model_cls.objects.get(
                subject_visit=visit, results_to_record__in=[chemistry])
        except model_cls.DoesNotExist:
            return False
        return True
    
    
    def func_tubercolosis(self, visit, **kwargs):
        tb = self.get_model('resultstorecord').objects.get(
            name='tubercolosis')
        try:
            model_cls = self.get_model('cancerdiagnosis')
            model_cls.objects.get(
                subject_visit=visit, results_to_record__in=[tb])
        except model_cls.DoesNotExist:
            return False
        return True
    
    
    def func_none_selection(self, visit, **kwargs):
        if_none = self.get_model('resultstorecord').objects.get(name='none')
        try:
            model_cls = self.get_model('cancerdiagnosis')
            model_cls.objects.get(
                subject_visit=visit, results_to_record__in=[if_none])
        except model_cls.DoesNotExist:
            return False
        return True

