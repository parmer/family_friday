from django.conf.urls import url
from . import views

app_name = "family_friday"

urlpatterns = [
    # Views
    url('^$', views.GroupsView.as_view(), name='groups'),
    url('^manage/$', views.ManageEmployeesView.as_view(), name='manage'),

    # Data Endpoints
    url('^employees/$', views.list_employees, name='employees'),
    url('^create-employee/$', views.create_employee, name='create_employee'),
    url('^delete-employee/(?P<employee_id>[0-9]+)/$', views.delete_employee, name='delete_employee'),
]
