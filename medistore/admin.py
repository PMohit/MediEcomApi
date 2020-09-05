from django.contrib import admin

# Register your models here.
from medistore.models import Company, Medicine, MedicalDetails, Customer, Employee, Bill, EmployeeSalary, BillDetails, \
    CompanyAccount, CustomerRequest, CompanyBank, EmployeeBank

admin.site.register(Company)
admin.site.register(Medicine)
admin.site.register(MedicalDetails)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(EmployeeSalary)
admin.site.register(BillDetails)
admin.site.register(CompanyAccount)
admin.site.register(CustomerRequest)
admin.site.register(CompanyBank)
admin.site.register(EmployeeBank)