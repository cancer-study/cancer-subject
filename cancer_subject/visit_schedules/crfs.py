from edc_visit_schedule.visit import Crf
crf = {}
crfs_1000 = (
    Crf(show_order=2, model='cancer_subject.symptomsandtesting'),
    Crf(show_order=3, model='cancer_subject.labresultheightweight'),
    Crf(show_order=4, model='cancer_subject.activityandfunctioning'),
    Crf(show_order=5, model='cancer_subject.baseriskassessmentdemo'),
    Crf(show_order=6, model='cancer_subject.baseriskassessment'),
    Crf(show_order=7, model='cancer_subject.baseriskassessmentfemale'),
    Crf(show_order=8, model='cancer_subject.baseriskassessmentcancer'),
    Crf(show_order=9, model='cancer_subject.baseriskassessmentsun'),
    Crf(show_order=10, model='cancer_subject.baseriskassessmentfuel'),
    Crf(show_order=11, model='cancer_subject.baseriskassessmentchemical'),
    Crf(show_order=12, model='cancer_subject.baseriskassessmentmining'),
    Crf(show_order=33, model='cancer_subject.baseriskassessmenteating'),
    Crf(show_order=14, model='cancer_subject.baseriskassessmentsmoking'),
    Crf(show_order=15, model='cancer_subject.baseriskassessmentalcohol'),
    Crf(show_order=16, model='cancer_subject.cancerdiagnosis'),
    Crf(show_order=17, model='cancer_subject.oncologytreatmentplan'),
    Crf(show_order=18, model='cancer_subject.labresulthaematology'),
    Crf(show_order=19, model='cancer_subject.labresultchemistry'),
    Crf(show_order=20, model='cancer_subject.labresulttb'),
    Crf(show_order=21, model='cancer_subject.baselinehivhistory'),
    Crf(show_order=22, model='cancer_subject.bhhhivtest'),
    Crf(show_order=23, model='cancer_subject.bhhwhoillness'),
    Crf(show_order=24, model='cancer_subject.haartrecord'),
    Crf(show_order=25, model='cancer_subject.oncologytreatmentrecord'),
    Crf(show_order=26, model='cancer_subject.otrsurgical'),
    Crf(show_order=27, model='cancer_subject.otrchemo'),
    Crf(show_order=28, model='cancer_subject.radiationtreatment'))
crf.update({1000: crfs_1000})

crfs_1300 = (
    Crf(show_order=1, model='cancer_subject.activityandfunctioning'),
    Crf(show_order=2, model='cancer_subject.currentsymptoms'),
    Crf(show_order=3, model='cancer_subject.oncologytreatmentcompleted'),
    Crf(show_order=4, model='cancer_subject.otrchemo'),
    Crf(show_order=5, model='cancer_subject.radiationtreatment'),
    Crf(show_order=6, model='cancer_subject.otrsurgical'))
crf.update({1300: crfs_1300})

crfs_1600 = (
    Crf(show_order=1, model='cancer_subject.activityandfunctioning'),
    Crf(show_order=2, model='cancer_subject.currentsymptoms'),
    Crf(show_order=3, model='cancer_subject.oncologytreatmentcompleted'),
    Crf(show_order=4, model='cancer_subject.otrchemo'),
    Crf(show_order=5, model='cancer_subject.radiationtreatment'),
    Crf(show_order=6, model='cancer_subject.otrsurgical'))
crf.update({1600: crfs_1600})

crfs_1900 = (
    Crf(show_order=1, model='cancer_subject.activityandfunctioning'),
    Crf(show_order=2, model='cancer_subject.currentsymptoms'),
    Crf(show_order=3, model='cancer_subject.oncologytreatmentcompleted'),
    Crf(show_order=4, model='cancer_subject.otrchemo'),
    Crf(show_order=5, model='cancer_subject.radiationtreatment'),
    Crf(show_order=6, model='cancer_subject.otrsurgical'))
crf.update({1900: crfs_1900})

crfs_2200 = (
    Crf(show_order=1, model='cancer_subject.activityandfunctioning'),
    Crf(show_order=2, model='cancer_subject.currentsymptoms'),
    Crf(show_order=3, model='cancer_subject.oncologytreatmentcompleted'),
    Crf(show_order=4, model='cancer_subject.otrchemo'),
    Crf(show_order=5, model='cancer_subject.otrsurgical'))
crf.update({2200: crfs_2200})

_crfs = (
    Crf(show_order=1, model='cancer_subject.activityandfunctioning'),
    Crf(show_order=2, model='cancer_subject.currentsymptoms'))

start_point = 2200
for _ in range(16):
    start_point += 300
    crf.update({start_point: _crfs})
