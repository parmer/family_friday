class ManageController {
    constructor(employeeService) {
        this.employeeService = employeeService;
        this.employees = [];
        this.newEmployeeName = "";

        this.refreshEmployees();
    }

    createEmployee() {
        this.isCreatingEmployee = true;
        this.createError = "";

        this.employeeService.createEmployee(this.newEmployeeName)
            .then(this.refreshEmployees.bind(this))
            .catch(function(error) {
                this.createError = error;
            }.bind(this))
            .then(function () {
                this.isCreatingEmployee = false;
                this.newEmployeeName = "";
            }.bind(this));
    }

    refreshEmployees() {
        this.employeeService.getEmployees().then(function(employees) {
            this.employees = employees;
        }.bind(this));
    }

    deleteEmployee(employee) {
        this.employeeService.deleteEmployee(employee).then(this.refreshEmployees.bind(this));
    }
}

ManageController.$inject = ["EmployeeService"];

angular.module("manage", ["employee-service"]).controller("ManageController", ManageController);
angular.bootstrap(document, ["manage"]);