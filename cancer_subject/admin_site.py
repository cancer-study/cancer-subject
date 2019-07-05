from django.contrib.admin import AdminSite as DjangoAdminSite


class AdminSite(DjangoAdminSite):
    site_title = 'Cancer Subject'
    site_header = 'Cancer Subject'
    index_title = 'Cancer Subject'
    site_url = '/cancer_subject/list/'


cancer_subject_admin = AdminSite(name='cancer_subject_admin')
