from edc.constants import NO, YES

MARITAL_STATUS_CHOICE = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Cohabiting', 'Cohabiting'),
    ('Widowed', 'Widowed'),
    ('Divorced', 'Divorced'),
    ('Other', 'Other, specify'),
)
RACE_CHOICE = (
    ('Black African', 'Black African'),
    ('Caucasian', 'Caucasian'),
    ('Asian', 'Asian'),
    ('Other', 'Other, specify:'),
)
ETHNIC_GRP_CHOICE = (
    ('Tswana-Bangwato', 'Tswana-Bangwato'),
    ('Tswana-Bakwena', 'Tswana-Bakwena'),
    ('Tswana-Bangwaketsi', 'Tswana-Bangwaketsi'),
    ('Tswana-Bakgatla', 'Tswana-Bakgatla'),
    ('Tswana-Batawana', 'Tswana-Batawana'),
    ('Tswana-Barolong', 'Tswana-Barolong'),
    ('Tswana-Bamalete', 'Tswana-Bamalete'),
    ('Tswana-Batlokwa', 'Tswana-Batlokwa'),
    ('Bakalanga', 'Bakalanga'),
    ('Basarwa', 'Basarwa'),
    ('Kgalagadi', 'Kgalagadi'),
    ('White', 'White'),
    ('Asian', 'Asian'),
    ('Other', 'Other, specify:'),
)
DISTRICT20_CHOICE = (
    ('Central', 'Central District'),
    ('Ghanzi', 'Ghanzi District'),
    ('Kgalagadi', 'Kgalagadi District'),
    ('Kgatleng', 'Kgatleng District'),
    ('Kweneng', 'Kweneng District'),
    ('North-East', 'North-East District '),
    ('North-West', 'North-West District (includes Chobe/Ngamiland)'),
    ('South-East', 'South-East District'),
    ('Southern', 'Southern District'),
)
SETTING20_CHOICE = (
    ('Farm/lands', 'Farm/lands'),
    ('Village', 'Village'),
    ('City/Town', 'City/Town'),
)
DISTRICT_CHOICE = (
    ('Central', 'Central District'),
    ('Ghanzi', 'Ghanzi District'),
    ('Kgalagadi', 'Kgalagadi District'),
    ('Kgatleng', 'Kgatleng District'),
    ('Kweneng', 'Kweneng District'),
    ('North-East', 'North-East District '),
    ('North-West', 'North-West District (includes Chobe/Ngamiland)'),
    ('South-East', 'South-East District'),
    ('Southern', 'Southern District'),
)
SETTING_CHOICE = (
    ('Farm/lands', 'Farm/lands'),
    ('Village', 'Village'),
    ('City/Town', 'City/Town'),
)
EDUCATION_CHOICE = (
    ('None', 'None'),
    ('Primary', 'Primary'),
    ('Junior secondary', 'Junior secondary'),
    ('Senior secondary', 'Senior secondary'),
    ('Tertiary', 'Tertiary'),
)
OCCUPATION_CHOICE = (
    ('Housewife', 'Housewife'),
    ('Salaried (government)', 'Salaried (government)'),
    ('Salaried (private)', 'Salaried (private)'),
    ('Domestic work (paid)', 'Domestic work (paid)'),
    ('Self-employed', 'Self-employed'),
    ('Student', 'Student'),
    ('Unemployed', 'Unemployed'),
    ('Other', 'Other, specify:'),
)
MONEY_PROVIDED_CHOICE = (
    ('Unsure', 'Unsure'),
    ('You', 'You'),
    ('Partner', 'Partner or spouse'),
    ('Parents', 'Parents'),
    ('Relatives', 'Other relatives'),
    ('Friend', 'Friend'),
    ('Other', 'Other, specify:'),
)
MONEY_EARNED_CHOICE = (
    ('None', 'None'),
    ('<P200/month (&lt; P50/week)', '<P200/month (&lt; P50/week)'),
    ('P200-500/month (P50-120/week)', 'P200-500/month (P50-120/week)'),
    ('P501-1000/month (P120-230/week)', 'P501-1000/month (P120-230/week)'),
    ('P1001-2500/month (P230-580/week)', 'P1001-2500/month (P230-580/week)'),
    ('P2501-5000/month (P580-1160/week)', 'P2501-5000/month (P580-1160/week)'),
    ('P5001-10000/month (P1160-2330/week)', 'P5001-10000/month (P1160-2330/week)'),
    ('P10001-20000/month (P2330-4600/week)', 'P10001-20000/month (P2330-4600/week)'),
    ('P20001-30000/month (P4600-7000/week)', 'P20001-30000/month (P4600-7000/week)'),
    ('>P30000/month (>P7000/week)', '>P30000/month (>P7000/week)'),
)
TOILET_CHOICE = (
    ('Indoor toilet', 'Indoor toilet'),
    ('Private latrine', 'Private latrine for your house/compound'),
    ('Shared latrine', 'Shared latrine with other compounds'),
    ('No latrine', 'No latrine facilities'),
    ('Other', 'Other, specify:'),
)
CANCER_TYPE_CHOICE = (
    ('Don\'t know', 'Don\'t know'),
    ('Cervical cancer', 'Cervical cancer'),
    ('Breast cancer', 'Breast cancer'),
    ('Esophageal cancer', 'Esophageal cancer'),
    ('Kaposi\'s sarcoma', 'Kaposi\'s sarcoma'),
    ('Lymphoma', 'Lymphoma'),
    ('Liver cancer', 'Liver cancer'),
    ('Eye cancer', 'Eye cancer'),
    ('Other or multiple cancers, describe:', 'Other or multiple cancers, describe:'),
)
CANCER_BEFORE_CHOICE = (
    ('Don\'t know', 'Don\'t know'),
    ('Cervical cancer', 'Cervical cancer'),
    ('Breast cancer', 'Breast cancer'),
    ('Esophageal cancer', 'Esophageal cancer'),
    ('Kaposi\'s sarcoma', 'Kaposi\'s sarcoma'),
    ('Lymphoma', 'Lymphoma'),
    ('Leukemia', 'Leukemia'),
    ('Wilm\'s Tumor', 'Wilm\'s Tumor'),
    ('Other', ' Other or multiple cancers, describe:'),
)
HEPATITIS_BEFORE_CHOICE = (
    ('No', 'No'),
    ('Hepatitis B', 'Hepatitis B'),
    ('Hepatitis C', 'Hepatitis C'),
    ('Don\'t know', 'Don\'t know'),
)
HOURS_OUTDOOR_CHOICE = (
    ('1 hour or less', '1 hour or less'),
    ('2 hours', '2 hours'),
    ('3 hours', '3 hours'),
    ('4 hours', '4 hours'),
    ('5 hours', '5 hours'),
    ('6 hours', '6 hours'),
)
SLEEVED_SHIRT_CHOICE = (
    ('never', 'never'),
    ('rarely', 'rarely'),
    ('sometimes', 'sometimes'),
    ('often', 'often'),
    ('always', 'always'),
)
HAT_CHOICE = (
    ('never', 'never'),
    ('rarely', 'rarely'),
    ('sometimes', 'sometimes'),
    ('often', 'often'),
    ('always', 'always'),
)
SHADE_UMBRELLA_CHOICE = (
    ('never', 'never'),
    ('rarely', 'rarely'),
    ('sometimes', 'sometimes'),
    ('often', 'often'),
    ('always', 'always'),
)
SUNGLASSES_CHOICE = (
    ('never', 'never'),
    ('rarely', 'rarely'),
    ('sometimes', 'sometimes'),
    ('often', 'often'),
    ('always', 'always'),
)
FUEL_HOUSEHOLD20_CHOICE = (
    ('solid fuels', 'solid fuels (dung, charcoal, wood, crops, coal)'),
    ('kerosene or gas', 'kerosene or gas'),
    ('electricity', 'electricity'),
    ('don\'t know', 'don\'t know'),
    ('Other', 'Other, specify'),
)

FUEL_MONTH_CHOICE = (
    ('solid fuels', 'solid fuels (dung, charcoal, wood, crops, coal)'),
    ('kerosene or gas', 'kerosene or gas'),
    ('electricity', 'electricity'),
    ('don\'t know', 'don\'t know'),
    ('Other', 'Other, specify'),
)
ASBESTOS_NO_PROTECTION_CHOICE = (
    ('<5 years', 'less than 5 years'),
    ('5 to 20 years', 'between 5 and 20 years'),
    ('>20 years', 'more than 20 years'),
)
CHEMICALS_TIME_CHOICE = (
    ('<5 years', 'less than 5 years'),
    ('5 to 20 years', 'between 5 and 20 years'),
    ('>20 years', 'more than 20 years'),
)
TOTAL_TIME_NO_PROTECTION_CHOICE = (
    ('<5 years', 'less than 5 years'),
    ('5 to 20 years', 'between 5 and 20 years'),
    ('>20 years', 'more than 20 years'),
)
MINE_TIME_CHOICE = (
    ('<5 years', 'less than 5 years'),
    ('5 to 20 years', 'between 5 and 20 years'),
    ('>20 years', 'more than 20 years'),
)
MINE_TYPE_CHOICE = (
    ('gold', 'gold'),
    ('diamond', 'diamond'),
    ('copper', 'copper'),
    ('nickel', 'nickel'),
    ('other, specify:', 'other, specify:'),
)
MINE_UNDERGROUND_TIME_CHOICE = (
    ('<5 years', 'less than 5 years'),
    ('5 to 20 years', 'between 5 and 20 years'),
    ('>20 years', 'more than 20 years'),
)
SMOKE_NOW_CHOICE = (
    ('yes', 'yes'),
    ('no', 'no, I used to smoke but quit'),
)
CIGARETTE_SMOKING_CHOICE = (
    ('14 or fewer cigarettes a day', '14 or fewer cigarettes a day'),
    ('between 15 and 25 cigarettes a day', 'between 15 and 25 cigarettes a day'),
    ('more than 25 cigarettes a day', 'more than 25 cigarettes a day'),
    ('refused', 'Participant declined to answer')
)
CIGARETTE_SMOKED_CHOICE = (
    ('14 or fewer cigarettes a day', '14 or fewer cigarettes a day'),
    ('between 15 and 25 cigarettes a day', 'between 15 and 25 cigarettes a day'),
    ('more than 25 cigarettes a day', 'more than 25 cigarettes a day'),
    ('refused', 'Participant declined to answer')
)
WHEN_QUIT_CHOICE = (
    ('less than 2 years ago', 'less than 2 years ago'),
    ('between 2 and 10 years ago', 'between 2 and 10 years ago'),
    ('between 10 and 20 years ago', 'between 10 and 20 years ago'),
    ('more than 20 years ago', 'more than 20 years ago'),
    ('refused', 'Participant declined to answer')
)
AGE_FIRSTSEX_CHOICE = (
    ('younger than 15 years old', 'younger than 15 years old'),
    ('between 15 and 17 years old', 'between 15 and 17 years old'),
    ('older than 17 years old', 'older than 17 years old'),
    ('don\'t know', 'don\'t know'),
    ('never', 'never'),
    ('Don\'t want to answer', 'Don\'t want to answer'),
    ('Declined', 'Patient declined to answer'),
)
TRADMEDICINE_CHOICE = (
    ('Never', 'Never'),
    ('Less than once a year', 'Less than once a year'),
    ('Between 1 and 5 times a year', 'Between 1 and 5 times a year'),
    ('Between 5 to 10 times a year', 'Between 5 to 10 times a year'),
    ('More than 10 times a year', 'More than 10 times a year'),
    ('Declined', 'Patient declined to answer'),
)
COMMUNITY = (
    ('Bokaa', 'Bokaa'),
    ('Digawana', 'Digawana'),
    ('Gumare', 'Gumare'),
    ('Gweta', 'Gweta'),
    ('Lentsweletau', 'Lentsweletau'),
    ('Lerala', 'Lerala'),
    ('Letlhakeng', 'Letlhakeng'),
    ('Mandunyane', 'Mandunyane'),
    ('Mmankgodi', 'Mmankgodi'),
    ('Mmadinare', 'Mmadinare'),
    ('Mmathethe', 'Mmathethe'),
    ('Masunga', 'Masunga'),
    ('Maunatlala', 'Maunatlala'),
    ('Mathangwane', 'Mathangwane'),
    ('Metsimotlhabe', 'Metsimotlhabe'),
    ('Molapowabojang', 'Molapowabojang'),
    ('Nata', 'Nata'),
    ('Nkange', 'Nkange'),
    ('Oodi', 'Oodi'),
    ('Otse', 'Otse'),
    ('Raikops', 'Raikops'),
    ('Ramokgonami', 'Ramokgonami'),
    ('Ranaka', 'Ranaka'),
    ('Sebina', 'Sebina'),
    ('Sefare', 'Sefare'),
    ('Sefophe', 'Sefophe'),
    ('Shakawe', 'Shakawe'),
    ('Shoshong', 'Shoshong'),
    ('Tati Siding', 'Tati Siding'),
    ('Tsetsebjwe', 'Tsetsebjwe'),
    ('DWTA', 'Do not want to answer'),
    ('Other', 'Other community'),
)

FOOD_SECURITY = (
    ('Never', 'Never'),
    ('Rarely', 'Rarely'),
    ('Sometimes', 'Sometimes'),
    ('Often', 'Often'),
    ('Declined', 'Patient declined to answer')
)

YES_NO_DECLINED = (
    (YES, YES),
    (NO, NO),
    ('Declined', 'Patient declined to answer')
)
