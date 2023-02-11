import { Body, Controller, Delete, Get, Post } from '@nestjs/common';
import { EmployeeService } from 'src/employee/employee.service';


@Controller('employee')
export class EmployeeController {

    constructor(private employeeService: EmployeeService) {

    }

    @Get()
    getEmployeeInfo(@Body() body) {
        return { name: 'Mi', email: 'mi@gmail.com' }
    }

    @Post()
    createEmployeeAccount(@Body() body) {
        return 'Account created successfully!'
    }

    // @Delete()
}
