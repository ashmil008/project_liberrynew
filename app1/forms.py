from .models import login,add
from django.forms import ModelForm,widgets
from django import forms

class edit_bookform(ModelForm):

    class Meta:
        model = add
        fields = ['book_name','auther_name','type_book','details','image']

class ChangepasswordForm(ModelForm):

    class Meta:
        model = login
        fields =['password']

        widgets = {
            'password': forms.TextInput(attrs={'class': 'form-control'})
        }


class EditprofileForm(ModelForm):

    class Meta:
        model = login
        fields = ['name','phone_number','classs']

        widgets ={
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'classs': forms.TextInput(attrs={'class': 'form-control'})


        }


