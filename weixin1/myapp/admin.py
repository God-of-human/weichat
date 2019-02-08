from django.contrib import admin

# Register your models here.
from .models import Grade,Students
class StudentInfo(admin.TabularInline):
    model = Students
    extra = 3

class GradeAdmin(admin.ModelAdmin):
    inlines = [StudentInfo]
    #显示字段
    list_display = ['pk','gname','gdate','ggirlnum','gboynum','isDelete']
    #过滤字段
   # list_filter =
    #搜索字段
  #  search_fields =
    #分页
    list_per_page =10
admin.site.register(Grade,GradeAdmin)
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    #设置页面列的名称
    gender.short_description = "性别"
    #显示字段
    list_display = ['pk','sname',gender,'sage','isDelete','sgrade']
    #过滤字段
    list_per_page = 10
    actions_on_top = False
    actions_on_bottom = True


#admin.site.register(Students,StudentsAdmin)