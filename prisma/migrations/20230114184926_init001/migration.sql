-- CreateTable
CREATE TABLE "employees" (
    "employeeId" SERIAL NOT NULL,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "nssf_number" TEXT NOT NULL,
    "kra_pin" TEXT NOT NULL,
    "phone" TEXT NOT NULL,
    "hire_date" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "overtime_rate" DOUBLE PRECISION NOT NULL,
    "job_title" TEXT NOT NULL,
    "salary" DOUBLE PRECISION NOT NULL,
    "department" TEXT NOT NULL,
    "bio" TEXT NOT NULL,
    "is_admin" BOOLEAN NOT NULL,
    "created_at" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "employees_pkey" PRIMARY KEY ("employeeId")
);

-- CreateTable
CREATE TABLE "employee_documents" (
    "docId" TEXT NOT NULL,
    "document_type" TEXT NOT NULL,
    "document_url" TEXT NOT NULL,
    "employeeId" INTEGER NOT NULL,

    CONSTRAINT "employee_documents_pkey" PRIMARY KEY ("docId")
);

-- CreateTable
CREATE TABLE "organizations" (
    "organizationId" TEXT NOT NULL,
    "sector" TEXT NOT NULL,
    "organization_name" TEXT NOT NULL,
    "team_size" INTEGER NOT NULL,
    "country" TEXT NOT NULL,
    "email" TEXT NOT NULL,

    CONSTRAINT "organizations_pkey" PRIMARY KEY ("organizationId")
);

-- CreateTable
CREATE TABLE "booked_demos" (
    "demoId" TEXT NOT NULL,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "company_email" TEXT NOT NULL,
    "company_name" TEXT NOT NULL,
    "job_title" TEXT,
    "number_of_employees" TEXT NOT NULL,
    "phone" TEXT,

    CONSTRAINT "booked_demos_pkey" PRIMARY KEY ("demoId")
);

-- CreateTable
CREATE TABLE "reviews" (
    "revieId" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "decription" TEXT NOT NULL,
    "complaints" TEXT,

    CONSTRAINT "reviews_pkey" PRIMARY KEY ("revieId")
);

-- CreateTable
CREATE TABLE "notice_board" (
    "noticeId" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "departmentId" TEXT[],
    "description" TEXT NOT NULL,

    CONSTRAINT "notice_board_pkey" PRIMARY KEY ("noticeId")
);

-- CreateTable
CREATE TABLE "Log" (
    "logId" TEXT NOT NULL,
    "log_type" TEXT NOT NULL,
    "time_created" TIMESTAMP(3) NOT NULL,
    "ip_address" TEXT NOT NULL,

    CONSTRAINT "Log_pkey" PRIMARY KEY ("logId")
);

-- CreateIndex
CREATE UNIQUE INDEX "employees_employeeId_key" ON "employees"("employeeId");

-- AddForeignKey
ALTER TABLE "employee_documents" ADD CONSTRAINT "employee_documents_employeeId_fkey" FOREIGN KEY ("employeeId") REFERENCES "employees"("employeeId") ON DELETE RESTRICT ON UPDATE CASCADE;
