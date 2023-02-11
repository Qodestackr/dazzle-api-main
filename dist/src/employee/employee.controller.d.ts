import { EmployeeService } from 'src/employee/employee.service';
export declare class EmployeeController {
    private employeeService;
    constructor(employeeService: EmployeeService);
    getEmployeeInfo(body: any): {
        name: string;
        email: string;
    };
    createEmployeeAccount(body: any): string;
}
