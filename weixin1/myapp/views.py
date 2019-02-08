from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("实验成功")

def detail(request, num):
    return HttpResponse("detail-%s"%num)


from .models import Grade
def grade(request):
    #去模板里取数据
    gradesList = Grade.objects.all()
    #将数据传递给模板，模板在渲染页面，
    return render(request,'myapp/grades.html',{"grade":gradesList})
# Create your views here.
from .models import Students
def students(request):
    studentsList = Students.objects.all()
    return render(request,'myapp/students.html',{"students":studentsList})


def gradesStudents(request, num):
    grade = Grade.objects.get(pk=num)
    studentList = grade.students_set.all()
    return render(request,'myapp/students.html',{"students":studentList})