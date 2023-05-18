
import csv

class PermissionManagementData:
    def __init__(self, filename):
        self.filename = filename

    def save(self, permissionManagements):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['customerPermission','employeePermission'])
            for permissionManagement in permissionManagements:
                writer.writerow([permissionManagement.customerPermission, permissionManagement.employeePermission])

    def load(self):
        permissionManagements = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                permissionManagements.append(PermissionManagement(row['customerPermission'],row['employeePermission']))
        return permissionManagements

class PermissionManagement:
    def __init__(self, customerPermission, employeePermission):
        self.customerPermission = customerPermission
        self.employeePermission = employeePermission

    def setCustomerPermission(self, permission):
        self.customerPermission = permission

    def setEmployeePermission(self, employee_id, permission):
        if employee_id not in self.employeePermission:
            self.employeePermission[employee_id] = {}
        self.employeePermission[employee_id] = permission

    def getEmployeePermission(self, employee_id):
        if employee_id in self.employeePermission:
            return self.employeePermission[employee_id]
        else:
            return {}



def test_permission_management():
    permission_management = PermissionManagement({'read': True, 'write': False}, {})
    assert permission_management.customerPermission == {'read': True, 'write': False}
    assert permission_management.employeePermission == {}

    permission_management.setEmployeePermission(1, {'read': True, 'write': True})
    assert permission_management.employeePermission == {1: {'read': True, 'write': True}}

    permission = permission_management.getEmployeePermission(1)
    assert permission == {'read': True, 'write': True}

    permission = permission_management.getEmployeePermission(2)
    assert permission == {}
