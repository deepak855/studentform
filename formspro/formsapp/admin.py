from django.contrib import admin
from  .models import StudentData

class AdminStudentData(admin.ModelAdmin):
    list_display = ['sno','sname','sloc','sfee']

admin.site.register(StudentData,AdminStudentData)
