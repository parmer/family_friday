class EmployeeService {
    constructor($http) {
        this.$http = $http;
    }

    getResponseDataPromise(url, params) {
        let data = {};

        if (params) {
            data['params'] = params;
        }

        return this.$http.get(url, data).then(function(response) {
            return response.data;
        }.bind(this));
    }

    getEmployees() {
        return this.getResponseDataPromise("/employees/");
    }

    getEmployeeGroups() {
        return this.getResponseDataPromise("/employee-groups/");
    }

    createEmployee(name) {
        let employeeData = {
            employee_name: name
        };

        return this.getResponseDataPromise("/create-employee/", employeeData)
            .catch(function(response) {
                throw response.data.error;
            });
    }

    deleteEmployee(employee) {
        return this.getResponseDataPromise("/delete-employee/" + employee.id + "/");
    }
}

EmployeeService.$inject = ["$http"];

angular.module("employee-service", []).service("EmployeeService", EmployeeService);
