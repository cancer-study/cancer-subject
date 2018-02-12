from .appointment_admin import AppointmentAdmin
from .base_risk_assessment_admin import (
    BaseRiskAssessmentAdmin, BaseRiskAssessmentAlcoholAdmin,
    BaseRiskAssessmentCancerAdmin, BaseRiskAssessmentChemicalAdmin,
    BaseRiskAssessmentDemoAdmin, BaseRiskAssessmentEatingAdmin,
    BaseRiskAssessmentFemaleAdmin, BaseRiskAssessmentFuelAdmin,
    BaseRiskAssessmentMiningAdmin, BaseRiskAssessmentSmokingAdmin,
    BaseRiskAssessmentSunAdmin)
from .baseline_hiv_history_admin import BaselineHIVHistoryAdmin, BHHHivTestAdmin
from .baseline_hiv_history_admin import BHHWhoIllnessAdmin, BHHCd4Admin
from .enrollment_checklist_admin import EnrollmentChecklistAdmin
from .lab_result_admin import LabResultAdmin, LabResultHeightWeightAdmin
from .lab_result_admin import LabResultHivAdmin, LabResultCd4Admin, LabResultViralloadAdmin
from .lab_result_admin import LabResultHaematologyAdmin, LabResultChemistryAdmin
from .lab_result_admin import LabResultTbAdmin
from .main import ActivityAndFunctioningAdmin, CancerDiagnosisAdmin
from .main import HaartRecordAdmin, OncologyTreatmentPlanAdmin, TreatmentResponseAdmin
from .main import SymptomsAndTestingAdmin, OncologyTreatmentCompletedAdmin
from .main import CurrentSymptomsAdmin
from .oncology_treatment_record_admin import OncologyTreatmentRecordAdmin, OTRChemoAdmin
from .oncology_treatment_record_admin import OTRRadiationAdmin, OTRSurgicalAdmin
from .radiation_treatment_admin import RadiationTreatmentAdmin
from .subject_consent_admin import SubjectConsentAdmin
from .subject_locator_admin import SubjectLocatorAdmin
from .subject_visit_admin import SubjectVisitAdmin
