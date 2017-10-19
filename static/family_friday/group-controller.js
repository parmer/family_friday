class GroupController {
    constructor(employeeService, $scope) {
        this.employeeService = employeeService;
        this.employees = [];

        this.employeeService.getEmployees().then(function(employees) {
            this.employees = employees;
        }.bind(this));
    }

    randomIndexForArray(array) {
        return Math.floor(Math.random() * array.length);
    }

    generateGroups() {
        this.groups = [];
        let employeesCopy = angular.copy(this.employees);

        function randomEmployeeIndex() {
            return Math.floor(Math.random() * employeesCopy.length);
        }

        while(employeesCopy.length >= GroupController.MIN_GROUP_SIZE) {
            let group = {
                name: "Group " + (this.groups.length + 1),
                employees: []
            };

            for (let i = 0; i < GroupController.MAX_GROUP_SIZE - 1; i++) {
                let randomIndex = this.randomIndexForArray(employeesCopy);
                group.employees.push(employeesCopy[randomIndex]);
                employeesCopy.splice(randomIndex, 1);
            }

            this.groups.push(group);
        }

        while(employeesCopy.length > 0) {
            let employeeIndex = this.randomIndexForArray(employeesCopy);
            let groupIndex = this.randomIndexForArray(this.groups);
            let group = this.groups[groupIndex];

            if (group.employees.length < GroupController.MAX_GROUP_SIZE) {
                group.employees.push(employeesCopy[employeeIndex]);
                employeesCopy.splice(employeeIndex, 1);
            }
        }
    }
}

GroupController.$inject = ["EmployeeService", "$scope"];
GroupController.MIN_GROUP_SIZE = 3;
GroupController.MAX_GROUP_SIZE = 5;

angular.module("group", ["employee-service"]).controller("GroupController", GroupController);
angular.bootstrap(document, ["group"]);