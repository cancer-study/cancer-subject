from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from .crfs import crf
from .requisitions import requisitions

# schedule for new participants
schedule1 = Schedule(
    name='schedule1',
    title='Cancer',
    enrollment_model='cancer_subject.enrollment',
    disenrollment_model='cancer_subject.disenrollment',
)

visit0 = Visit(
    code='1000',
    title='Day 1',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=45),
    requisitions=requisitions,
    crfs=crf.get(1000))

visit1 = Visit(
    code='1300',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(1300))

visit2 = Visit(
    code='1600',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(1600))

visit3 = Visit(
    code='1900',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(1900))

visit4 = Visit(
    code='2200',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(2200))

visit5 = Visit(
    code='2500',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(2500))

visit6 = Visit(
    code='2800',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(2800))

visit7 = Visit(
    code='3100',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(3100))

visit8 = Visit(
    code='3400',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(3400))

visit9 = Visit(
    code='3700',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(3700))

visit10 = Visit(
    code='4000',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(4000))

visit11 = Visit(
    code='4300',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(4300))

visit12 = Visit(
    code='4600',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(4600))

visit13 = Visit(
    code='4900',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(4900))

visit14 = Visit(
    code='5200',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(5200))

visit15 = Visit(
    code='5500',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(5500))

visit16 = Visit(
    code='5800',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(5800))

visit17 = Visit(
    code='6100',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(6100))

visit18 = Visit(
    code='6400',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(6400))

visit19 = Visit(
    code='6700',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(6700))

visit20 = Visit(
    code='7000',
    title='Day 3',
    timepoint=1,
    rbase=relativedelta(days=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=6),
    requisitions=requisitions,
    crfs=crf.get(7000))

schedule1.add_visit(visit=visit0)
