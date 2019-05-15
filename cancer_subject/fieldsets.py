subject_contacts_fieldset = (
    ('Subject Contact Information', {
        'fields': (
            'may_call',
            'may_visit_home',
            'mail_address',
            'physical_address',
            'subject_cell',
            'subject_cell_alt',
            'subject_phone',
            'subject_phone_alt')})
)

indirect_contacts_fieldset = (
    ('Other Contact Information', {
        'fields': (
            'may_contact_indirectly',
            'indirect_contact_name',
            'indirect_contact_relation',
            'indirect_contact_cell',
            'indirect_contact_cell_alt',
            'indirect_contact_phone')})
)


other_indirect_contacts_fieldset = (
    ('Other Alternative Contact Information', {
        'fields': (
            'has_alt_contact',
            'alt_contact_name',
            'alt_contact_rel',
            'alt_contact_cell',
            'other_alt_contact_cell',
            'alt_contact_tel',)})
)
