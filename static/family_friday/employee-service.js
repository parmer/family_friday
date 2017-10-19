class EmployeeService {
    constructor($http) {
        this.$http = $http;
    }

    getEmployees() {
        return this.$http.get("/employees/").then(function(response) {
            return response.data;
        }.bind(this));
    }

    createEmployee(name) {
        let employeeData = {
            params: {
                employee_name: name
            }
        };

        return this.$http.get("/create-employee/", employeeData)
            .then(function(response) {
                return response.data;
            })
            .catch(function(response) {
                throw response.data.error;
            });
    }

    deleteEmployee(employee) {
        return this.$http.get("/create-employee/" + employee.id + "/", employeeData).then(function(response) {
            return response.data;
        }.bind(this));
    }
}

EmployeeService.$inject = ["$http"];

angular.module("employee-service", []).service("EmployeeService", EmployeeService);
