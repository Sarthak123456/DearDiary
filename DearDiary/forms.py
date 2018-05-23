
from django import forms
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
    )

User=get_user_model()

class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username=self.cleaned_data.get("username")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("Username not correct.Username is Case-Sensitive.")
        password=self.cleaned_data.get("password")
        if username and password:
            user=authenticate(username=username, password=password)
            if not user:
               raise forms.ValidationError("Password not correct")
   
        return super(UserLoginForm, self).clean(*args, **kwargs)
        
        
class UserRegisterForm(forms.ModelForm):
    email= forms.EmailField(label='Email')
    # email2= forms.EmailField(label=' Email')
    
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=[
            
            'username',
            'password',
            'email'
            ]
            
    def clean_email(self):
        email=self.cleaned_data.get('email')
        # email2=self.cleaned_data.get('email2')
        
        # if email!= email2:
        #     raise forms.ValidationError('Emails must match')
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("User already there!")
            
        return email
            
   
  