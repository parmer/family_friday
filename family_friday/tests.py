from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from family_friday.models import Employee, MAX_GROUP_SIZE, MIN_GROUP_SIZE


# Create your tests here.
class EmployeeModelTests(TestCase):
    def create_employees_and_get_groups(self, amount):
        for x in range(0, amount):
            Employee.objects.create(name="Employee %s" % x, join_date=timezone.now())

        response = self.client.get(reverse('family_friday:employee_groups'))
        return response.json()

    def verify_groups_size(self, groups):
        for group in groups:
            group_size = len(group['employees'])
            self.assertLessEqual(group_size, MAX_GROUP_SIZE, "Group is bigger than %s" % MAX_GROUP_SIZE)
            self.assertGreaterEqual(group_size, MIN_GROUP_SIZE, "Group is smaller than %s" % MIN_GROUP_SIZE)

    def test_evenly_divided_employee_set(self):
        num_employees = (MAX_GROUP_SIZE - 1) * 4
        groups = self.create_employees_and_get_groups(num_employees)
        self.verify_groups_size(groups)

    def test_one_less_than_evenly_divided_employee_set(self):
        num_employees = (MAX_GROUP_SIZE - 1) * 4 - 1
        groups = self.create_employees_and_get_groups(num_employees)
        self.verify_groups_size(groups)

    def test_two_less_than_evenly_divided_employee_set(self):
        num_employees = (MAX_GROUP_SIZE - 1) * 4 - 2
        groups = self.create_employees_and_get_groups(num_employees)
        self.verify_groups_size(groups)

    def test_large_employee_set(self):
        groups = self.create_employees_and_get_groups(300)
        self.verify_groups_size(groups)




