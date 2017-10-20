from math import floor
from random import random

from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError
from django.views import generic

from family_friday.models import Employee


class ManageEmployeesView(generic.TemplateView):
    template_name = "family_friday/manage.html"


class GroupsView(generic.TemplateView):
    template_name = "family_friday/groups.html"


def list_employees(request):
    employees = Employee.objects.all().values('id', 'name', 'join_date')
    return JsonResponse(list(employees), safe=False)


def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()

    return JsonResponse({})


def _create_json_error(error_message):
    response = JsonResponse({
        'error': error_message
    })
    response.status_code = 400
    return response


def create_employee(request):
    try:
        name = request.GET['employee_name']
        employee = Employee(name=name, join_date=timezone.now())
        employee.save()

        return JsonResponse({'id': employee.id})
    except IntegrityError:
        return _create_json_error("employee already exists")
    except MultiValueDictKeyError:
        return _create_json_error("employee_name not provided")


def _get_random_index_for_list(arr):
    return floor(random() * len(arr))


def get_groups(request):
    groups = []
    employees = list(Employee.objects.all().values('id', 'name', 'join_date'))

    MIN_GROUP_SIZE = 3
    MAX_GROUP_SIZE = 5

    while len(employees) >= MIN_GROUP_SIZE:
        group = {
            'name': "Group %s" % len(groups),
            'employees': []
        }

        for x in range(0, MAX_GROUP_SIZE - 1):
            employee_index = _get_random_index_for_list(employees)
            employee = employees.pop(employee_index)
            group['employees'].append(employee)

        groups.append(group)

    while len(employees) > 0:
        employee_index = _get_random_index_for_list(employees)
        group_index = _get_random_index_for_list(groups)
        group = groups[group_index]

        if len(group['employees']) < MAX_GROUP_SIZE:
            group['employees'].append(employees.pop(employee_index))

    return JsonResponse(groups, safe=False)


