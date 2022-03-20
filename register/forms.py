from django import forms


class StudentForm(forms.Form):

    sname = forms.CharField(label='Name',widget=forms.TextInput(attrs={'class': 'special','style': 'width:170px','placeholder':'Enter your Name'},))
    semail = forms.CharField(label='Email.:',widget=forms.TextInput(attrs={'class': 'special','style': 'width:180px','placeholder':'Enter your email'}))
    # smob = forms.CharField(label='Mob.:',widget=forms.TextInput(attrs={'class': 'special','style': 'width:180px','placeholder':'Enter your Department'}),)
    saddr = forms.CharField(label='Addr.:',widget=forms.TextInput(attrs={'class': 'special','style': 'width:180px','placeholder':'Enter your Address'}))

class SForm(forms.Form):
    sname = forms.CharField(max_length=30,label='Name' )

# class StudentsForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('sname','saddr','sdep','ssch')
#         widgets = {
#             'sname':forms.TextInput(attrs={'place holder':'please enter','class': 'special','style': 'width:10px'}),
#             'saddr': forms.TextInput(attrs={'class': 'form-control'}),
#             'sdep': forms.TextInput(attrs={'class': 'form-control'}),
#             'ssch': forms.TextInput(attrs={'class': 'form-control'}),
#         }


