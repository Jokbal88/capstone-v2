from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class StudentRegistrationForm(UserCreationForm):
    student_id = forms.CharField(max_length=7)
    lrn = forms.CharField(max_length=12)
    lastname = forms.CharField(max_length=100)
    firstname = forms.CharField(max_length=100)
    middlename = forms.CharField(max_length=100, required=False)
    degree = forms.CharField(max_length=100)
    year_level = forms.IntegerField()
    sex = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    email = forms.EmailField()
    contact_number = forms.CharField(max_length=11)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Use email as username
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Student.objects.create(
                student_id=self.cleaned_data['student_id'],
                lrn=self.cleaned_data['lrn'],
                lastname=self.cleaned_data['lastname'],
                firstname=self.cleaned_data['firstname'],
                middlename=self.cleaned_data['middlename'],
                degree=self.cleaned_data['degree'],
                year_level=self.cleaned_data['year_level'],
                sex=self.cleaned_data['sex'],
                email=self.cleaned_data['email'],
                contact_number=self.cleaned_data['contact_number']
            )
        return user