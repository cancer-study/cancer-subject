from edc_reference.reference_model_config import ReferenceModelConfig
from edc_reference.site import site_reference_fields

reference = ReferenceModelConfig(
    model='cancer_subject.baselinehivhistory',
    fields=['has_hiv_result', 'had_who_illnesses'])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='cancer_subject.baseriskassessment',
    fields=['has_worked_mine', 'has_alcohol', ])
site_reference_fields.register(reference)

reference = ReferenceModelConfig(
    model='cancer_subject.bhhivtest',
    fields=['hiv_result', ])
site_reference_fields.register(reference)
