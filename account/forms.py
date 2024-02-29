from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User




# class RegistrationForm(UserCreationForm):
#     first_name=forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
#     last_name=forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']
    
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
    



#         email = cleaned_data.get('email')
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("Email already exists.")

#         return cleaned_data

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         # user.set_password(self.cleaned_data['password'])
#         user.is_active = False
#         if commit:
#             user.save()
#         return user




class RegistrationForm(forms.Form):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")

        return cleaned_data

    def save(self, commit=True):
        username = self.cleaned_data['username']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = False
        if commit:
            user.save()
        return user





class UpdateForm(forms.ModelForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id' : 'required'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']