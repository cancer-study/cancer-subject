from edc_visit_schedule.visit import Requisition

from ..labs import (viral_load_panel, cd4_panel, fbc_panel, csf_panel,
                    chemistry_alt_panel, chemistry_panel)

requisitions = ()

requisitions_d1 = (
    Requisition(
        show_order=10, model='ambition_subject.subjectrequisition',
        panel=viral_load_panel, required=False, additional=False),
    Requisition(
        show_order=20, model='ambition_subject.subjectrequisition',
        panel=cd4_panel, required=False, additional=False),
    Requisition(
        show_order=30, model='ambition_subject.subjectrequisition',
        panel=fbc_panel, required=True, additional=False),
    Requisition(
        show_order=40, model='ambition_subject.subjectrequisition',
        panel=csf_panel, required=True, additional=False),
    Requisition(
        show_order=50, model='ambition_subject.subjectrequisition',
        panel=chemistry_alt_panel, required=True, additional=False),
)

requisitions_d3 = (
    Requisition(
        show_order=10, model='ambition_subject.subjectrequisition',
        panel=chemistry_panel),
)

requisitions_d7 = (
    Requisition(
        show_order=10, model='ambition_subject.subjectrequisition',
        panel=chemistry_alt_panel, required=True, additional=False),
    Requisition(
        show_order=20, model='ambition_subject.subjectrequisition',
        panel=fbc_panel, required=True, additional=False),
    Requisition(
        show_order=30, model='ambition_subject.subjectrequisition',
        panel=csf_panel, required=True, additional=False),
)
# TODO: Add day 5 Chemistry requisition, Only form required
# TODO: Add day 7 FBC, ALT, CSF,and Chemistry requisitions
# TODO: Add day 10 Chemistry requisition, Only form required
# TODO: Add day 12 Chemistry requisition, Only form required
# TODO: Add day 14FBC, ALT, CSF,and Chemistry requisitions
# TODO: Add week 4 FBC, ALT and Chemistry requisitions
