from django.urls import path
from .views import AttendanceRecordList, AttendanceRecordDetail, TimesheetRecordList, TimesheetRecordDetail

urlpatterns = [
    path('attendance-records/', AttendanceRecordList.as_view(),
         name='attendance-record-list'),
    path('attendance-records/<int:pk>/', AttendanceRecordDetail.as_view(),
         name='attendance-record-detail'),
    path('timesheet-records/', TimesheetRecordList.as_view(),
         name='timesheet-record-list'),
    path('timesheet-records/<int:pk>/', TimesheetRecordDetail.as_view(),
         name='timesheet-record-detail'),
]


'''
Employee Profile:

Model to store employee personal information, contact details, and employment history.
Job Positions:

Model to define different job positions within the organization, including job titles, responsibilities, and departments.
Employee Status:

Model to track the status of employees (e.g., active, on hold, suspended, etc.).
Employee Contracts:

Model for managing employment contracts, including contract start and end dates, terms, and renewal information.
Performance Reviews:

Model to store records of employee performance reviews, feedback, and goals.
Training and Development:

Model for managing employee training and development programs and tracking employee participation.
Employee Documents:

Model to store and manage important employee documents, such as resumes, certificates, and identification documents.
Time and Attendance:

Model to track employee attendance, leave requests, and timesheet records.
Payroll Information:

Model for managing payroll-related information, including salary details, tax information, and deductions.
Benefit Plans:

Model to define employee benefit plans, such as health insurance, retirement plans, and other benefits offered by the organization.
HR Policies and Procedures:

Model for storing HR policies and procedures, making them accessible to employees.
Recruitment and Onboarding:

Model for managing the recruitment process, including job postings, applicant details, and onboarding tasks for new hires.
Employee Surveys and Feedback:

Model for collecting and storing employee feedback and survey responses.
Organizational Structure:

Model to define the organizational hierarchy, including reporting relationships and department structures.
Termination and Offboarding:

Model for tracking employee terminations, exit interviews, and offboarding tasks.
Leave Requests and Approvals:

Model for managing employee leave requests, approvals, and tracking leave balances.

'''
