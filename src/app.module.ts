import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { EmployeeModule } from './employee/employee.module';
import { AuthModule } from './auth/auth.module';
import { DbModule } from './db/db.module';

@Module({
  imports: [EmployeeModule, AuthModule, DbModule],
  controllers: [AppController],
  providers: [AppService],
})

export class AppModule { }
