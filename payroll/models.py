from django.db import models

# Create your models here.
'''
model Performance {
  id Int @id

  performance_note String
}


//////////
// LEAVE x PAYROLL
/////////

model TimeSheet {
  id            Int      @id
  userId        String
  date          DateTime
  startTime     DateTime
  endTime       DateTime
  totalHours    String
  overtimeHours Int
  rate          Float

  @@map("timesheets")
}

model Attendance {
  id       Int      @id
  // type : training attendance ,, job,, meeting ,, etc*
  date     DateTime
  checkin  String
  checkout String
}

model Absence {
  id Int @id

  reason String
  status Boolean //!Approved...Communicated...Rejected
}

model Leave {
  id        Int      @id
  userId    String
  startDate DateTime
  endDate   DateTime
  type      String // type of leave: sick, holiday, ...*
  status    String // pending/ approved/ rejected
  reason    String

  @@map("leaves")
}

model PayrollPaymentMethod {
  id Int @id

  @@map("payroll_payment_method")
}

model Salary {
  id Int @id
}

model Bonus {
  id           Int   @id
  bonus_amount Float
  // bonus_type   quarterly | monthly | annually
  // period??.
  // @@map('bonuses')
}

model Deduction {
  id Int @id
}

model Tax {
  userId String @id

  tax_type   TaxType
  tax_amount Float

  @@map("taxes")
}

enum TaxType {
  INCOME_TAX
  PAYE
  NHIF
  NSSF
  HDMF
}

model Payroll {
  id             Int    @id
  main_salary    Float
  compenstations Float // e.g fitness, library etc
  allowances     Float // fuel...
  overtime_rate  Float
  bonus          Float
  nssf_number    String
  kra_pin        String

  @@map("payrolls")
}

// payroll history
model PayrollTransaction {
  id Int @id
}

'''


class Payroll(models.Model):
    # compensation_options = 'fitness', library...
    payroll_id = models.CharField(max_length=255)
    main_salary = models.DecimalField()
    total_compensation_amount = models.DecimalField()
    allowance_amount = models.DecimalField()  # fuel etc => for allowance_type
