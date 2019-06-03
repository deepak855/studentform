from django import forms
class StudentForm(forms.Form):
    sno = forms.IntegerField(
        label="Enter student Number :",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'student number.',
                'class':'form-control',
            }
        )
    )
    sname = forms.CharField(
        label="Enter Your Name :",
        widget=forms.TimeInput(
            attrs={
                'placeholder':'student name.',
                'class':'form-control',
            }
        )
    )
    sloc = forms.CharField(
        label="Enter Your Location :",
        widget=forms.TextInput(
            attrs={
                'placeholder':'enter your location. ',
                'class':'form-control',
            }
        )
    )
    sfee = forms.IntegerField(
        label="Enter Your fee :",
        widget=forms.TextInput(
            attrs={
                'placeholder':'enter fee.',
                'class':'form-control',
            }
        )
    )
