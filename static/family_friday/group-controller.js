class GroupController {
    constructor(employeeService) {
        this.employeeService = employeeService;
        this.employees = [];

        this.employeeService.getEmployees().then(function(employees) {
            this.employees = employees;
        }.bind(this));
    }

    generateGroups() {
        this.employeeService.getEmployeeGroups().then(function(groups) {
            this.groups = groups;
        }.bind(this));
    }
}

GroupController.$inject = ["EmployeeService"];

angular.module("group", ["employee-service"]).controller("GroupController", GroupController);
angular.bootstrap(document, ["group"]);