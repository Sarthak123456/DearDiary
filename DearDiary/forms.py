
from django import forms
from django.core.mail import send_mail
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
        password=self.cleaned_data.get("password")
        if username and password:
            user=authenticate(username=username, password=password)
            if not user:
                send_mail(
                    'Subject here',
                    'Here is the message.',
                    'sarthak.tuteja91@gmail.com',
                    ['sarthak.tuteja91@gmail.com'],
                    fail_silently=False,
                )
                raise forms.ValidationError("This is not a valid user")
               
            if not user.check_password(password):
                raise forms.ValidationError("Enter correct password")
            if not user.is_active:
                raise forms.ValidationError("User not valid")
            
                  
   
        return super(UserLoginForm, self).clean(*args, **kwargs)
        
        
class UserRegisterForm(forms.ModelForm):
    email= forms.EmailField(label=' Confirm Email')
    email2= forms.EmailField(label=' Email')
    
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=[
            
            'username',
            'password',
            'email2',
            'email'
            ]
            
    def clean_email(self):
        email=self.cleaned_data.get('email')
        email2=self.cleaned_data.get('email2')
        
        if email!= email2:
            raise forms.ValidationError('Emails must match')
        email_qs=User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("User already there!")
            
        return email
            
   
   