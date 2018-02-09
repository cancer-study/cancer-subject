STAGES = (
    ('X', 'X'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

MODIFIER = (
    ('X', 'X'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)

TREATMENT_INTENT = (
    ('UNK', 'Unknown'),
    ('Curative', 'Curative'),
    ('Palliative', 'Palliative'),
)

TREATMENT_RELATIONSHIP = (
    ('UNK', 'Unknown'),
    ('no modalities', 'No other treatment modalities'),
    ('concurrent chemo', 'Concurrent chemotherapy'),
    ('Adj after surgery', 'Adjuvant after surgery'),
    ('Adj after chemo', 'Adjuvant after chemotherapy'),
    ('Adj after surgery and chemo', 'Adjuvant after surgery and chemotherapy'),
    ('Neo before chemo', 'Neoadjuvant before Chemotherapy'),
    ('Neo before surgery', 'Neoadjuvant before Surgery'),
    ('Other', 'Other, specify'),
)

SIDE_EFFECTS = (
    ('UNK', 'Unknown'),
    ('hyperpigmentation', 'hyperpigmentation'),
    ('vaginal stenosis', 'vaginal stenosis'),
    ('diarrhea, proctitis', 'diarrhea, proctitis'),
    ('moist desquamation', 'moist desquamation'),
    ('fibrosis', 'fibrosis'),
    ('Other', 'Other, specify'),
)

RESPONSE = (
    ('UNK', 'Unknown'),
    ('Complete', 'Complete'),
    ('Almost Complete', 'Almost Complete'),
    ('Residual Tumor', 'Residual Tumor'),
    ('Poor response', 'Poor response'),
    ('Good palliation', 'Good palliation'),
    ('Modest Palliation', 'Modest Palliation'),
    ('Poor Palliation', 'Poor Palliation'),
    ('Other', 'Other, specify'),
)

REASONS_MISSED_OR_DELAYED = (
    ('Toxicity hematologic', 'Toxicity- hematologic (anemia, neutropenia, or low plts), '),
    ('Toxicity skin', 'Toxicity-skin (dermatitis, mucositis), '),
    ('unresponsive', 'Cancer not responding to treatment'),
    ('defaulted', 'Defaulted visit or lost to follow-up'),
    ('machine downtime', 'Machine down-time or repair'),
    ('no accomodation', 'clinic too busy to accommodate'),
    ('no transport', 'lack of transportation to facility'),
    ('Other', 'Other, specify'),
)

RADIATION_TECHNIQUE = (
    ('AP/PA', 'AP/PA'),
    ('4-field Box', '4-field Box'),
    ('Opposed Laterals', 'Opposed Laterals'),
    ('Tangents', 'Tangents'),
    ('IMRT', 'IMRT'),
    ('IR 192', 'IR 192'),
    ('Other', 'Other Technique')
)

MODALITY = (
    ('Photons', 'Photons'),
    ('Electrons', 'Electrons'),
    ('Brachy', 'Brachy'),
    ('Particle Therapy', 'Particle Therapy'),
    ('Other Energy', 'Other Energy'),
)

BRACHY_LENGTH = (
    ('2', '2'),
    ('3.5', '3.5'),
    ('4', '4'),
    ('6', '6'),
    ('8', '8'),
    ('OTHER', 'Other'),
    ('UNK', 'Unknown'),
)

BRACHY_TYPE = (
    ('T&SR', 'T&SR'),
    ('T&Ovoids', 'T&Ovoids'),
    ('T&Cylinder', 'T&Cylinder'),
    ('Cylinder', 'Cylinder'),
    ('SR', 'SR'),
    ('OTHER', 'Other'),
    ('UNK', 'Unknown'),
)
