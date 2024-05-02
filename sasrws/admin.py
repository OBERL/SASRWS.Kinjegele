from django.contrib import admin
from .models import Department, Employee, Customer, Car, Service, ServiceRecord, Reminder, DistanceData

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('DepartmentName', 'HeadOfDepartment', 'RegisteredDate')
    search_fields = ('DepartmentName', 'HeadOfDepartment')
    readonly_fields = ('RegisteredDate',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'DepartmentId', 'RegisteredDate')
    list_filter = ('DepartmentId',)
    search_fields = ('FullName', 'DepartmentId__DepartmentName')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('FullName', 'Resident', 'PhoneNumber', 'RegisteredDate')
    search_fields = ('FullName', 'Resident', 'PhoneNumber')
    readonly_fields = ('image_tag', 'Car_id')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('CarID', 'customer', 'employee', 'CarStatus', 'PaymentAmount', 'RegisteredDate')
    list_filter = ('CarStatus', 'RegisteredDate')
    search_fields = ('CarID', 'customer__FullName', 'employee__FullName')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')
    search_fields = ('name',)

@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'service', 'date', 'notes')
    list_filter = ('date', 'service')
    search_fields = ('vehicle__CarID', 'service__name', 'notes')

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('driver', 'vehicle', 'service', 'reminder_date', 'sent', 'last_serviced_distance', 'next_service_distance')
    list_filter = ('sent', 'reminder_date')
    search_fields = ('driver__FullName', 'vehicle__CarID', 'service__name')
    readonly_fields = ('last_serviced_distance', 'next_service_distance')

@admin.register(DistanceData)
class DistanceDataAdmin(admin.ModelAdmin):
    list_display = ('car', 'distance', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('car__CarID',)
    readonly_fields = ('timestamp',)
