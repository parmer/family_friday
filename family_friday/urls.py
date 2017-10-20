from django.conf.urls import url
from . import views

app_name = "family_friday"

urlpatterns = [
    # Views
    url('^$', views.index_view, name='groups'),
    url('^manage/$', views.ManageEmployeesView.as_view(), name='manage'),

    # Data Endpoints
    url('^employees/$', views.list_employees, name='employees'),
    url('^employee-groups/$', views.get_groups, name='employee_groups'),
    url('^create-employee/$', views.create_employee, name='create_employee'),
    url('^delete-employee/(?P<employee_id>[0-9]+)/$', views.delete_employee, name='delete_employee'),
    url('^employee-in-office/(?P<employee_id>[0-9]+)/$', views.employee_in_office, name='employee_in_office'),
    url('^employee-out-of-office/(?P<employee_id>[0-9]+)/$', views.employee_not_in_office, name='employee_not_in_office'),
]
