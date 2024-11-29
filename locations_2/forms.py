from django import forms
from .models import Location,User,Contact
from .models import Location,User, Contact
from secrets import choice
from django.core.exceptions import ValidationError

class PropertyRegister(forms.ModelForm):
	class Meta:
		model = Location
		fields = ['title','city','district','sector','image', 'description']
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email', 'subject', 'message']


class RegistrationForm(forms.ModelForm):
    GENDER  = (
        ('Male','Male'),
        ('Female','Female')
    )
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    age = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','age','gender')
    def clean(self):
        errors=[]
        first_name = self.cleaned_data['first_name']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if(password != confirm_password):
            errors.append("Password doesn't match")
        
        if(len(first_name)< 2):
            errors.append("Fistname is too short")
        if(len(username)< 2):
            errors.append("Username is too short")

        if(len(errors) > 0):
            raise ValidationError(errors)

    
    def save(self):
        user  = User(username = self.cleaned_data['username'],gender = self.cleaned_data['gender'],first_name = self.cleaned_data['first_name'],last_name= self.cleaned_data['last_name'],age=self.cleaned_data['age'],email=self.cleaned_data['email'])
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

# class ContactForm(forms.ModelForm):
#     class Meta:
#         model=Contact
#         fields=['name','email','subject','message']