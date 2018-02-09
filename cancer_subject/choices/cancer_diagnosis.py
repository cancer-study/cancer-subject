CANCER_CATEGORY_CHOICE = (
    ('new', 'New Cancer (no treatment for this cancer type for >5 year, or treatment began less than 6 weeks ago'),
    ('relapsed', 'Relapsed or recurrent cancer (no active treatment for this cancer for >1 year)'),
    ('Ongoing', 'Ongoing treatment (active treatment for this cancer type in past year)'),
)
SYMPTOM_PROMPT_CHOICE = (
    ('Pain', 'Pain'),
    ('Lump/Mass', 'Lump/Mass'),
    ('Fever', 'Fever'),
    ('Cough', 'Cough'),
    ('Shortness of Breath', 'Shortness of Breath'),
    ('Bleeding', 'Bleeding'),
    ('Weight loss', 'Weight loss'),
    ('Swelling of leg', 'Swelling of leg'),
    ('Difficulty swallowing', 'Difficulty swallowing'),
    ('Bump/rash on skin or eye', 'Bump/rash on skin or eye'),
    ('Other', 'Other'),
)
DIAGNOSIS_BASIS_CHOICE = (
    ('Clinical Only', 'Clinical Only'),
    ('Clinical AND Radiology (CT, X-ray, U/S)', 'Clinical AND Radiology (CT, X-ray, U/S)'),
    ('Surgery', 'Surgery'),
    ('Biochemical/Immunological Test', 'Biochemical/Immunological Test'),
    ('Cytology/Haematology', 'Cytology/Haematology'),
    ('Histology of Metastasis', 'Histology of Metastasis'),
    ('Histology of Primary', 'Histology of Primary'),
    ('Autopsy with Histology', 'Autopsy with Histology'),
    ('Other', 'Other (including unknown): '),
)
TUMOUR_BASIS_CHOICE = (
    ('UNK', 'Unknown'),
    ('Clinical', 'Clinical'),
    ('Pathology', 'Pathology'),
)

TUMOUR_POSSIBLE_GRADES = (
    ('UNK', 'Unknown'),
    ('X', 'X'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)
LYMPH_BASIS_CHOICE = (
    ('UNK', 'Unknown'),
    ('Clinical', 'Clinical'),
    ('Pathology', 'Pathology'),
)
LYMPH_POSSIBLE_GRADES = (
    ('UNK', 'Unknown'),
    ('X', 'X'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
)
METASTASIS_BASIS_CHOICE = (
    ('UNK', 'Unknown'),
    ('Clinical', 'Clinical'),
    ('Pathology', 'Pathology'),
)
METASTASIS_POSSIBLE_GRADES = (
    ('UNK', 'Unknown'),
    ('X', 'X'),
    ('0', '0'),
    ('1', '1'),
)
POSSIBLE_OVERALL_STAGES = (
    ('X', 'X'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)
#Only two stages A and B
POSSIBLE_OVERALL_STAGE_MODIFIER = (
    ('UNK', 'Unknown'),
    ('No stage modifier', 'No stage modifier'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)
