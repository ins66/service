from django.forms import forms, ModelForm

from student.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        # fields = "__all__"
        exclude = ['sno','name','gender','birthday','mobile','email','address']
