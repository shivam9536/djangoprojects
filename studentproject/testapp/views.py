from django.shortcuts import render
from testapp import forms
from testapp.models import Student

# Create your views here.
def index_view(request):
    return render(request,'testapp/index.html')

def student_view(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Form data inserted into database successfully")
            return index_view(request)
    return  render(request,'testapp/register.html',{'form':form})

def student_data(request):
    student_list = Student.objects.all()
    my_dict = {'student_list':student_list,}
    return render(request,'testapp/studentdata.html',context=my_dict)