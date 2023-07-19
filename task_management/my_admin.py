from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = "My Admin"
    site_title = "My Admin Portal"
    index_title = "Welcome to this Portal"


my_admin_site = MyAdminSite(name='myadmin')