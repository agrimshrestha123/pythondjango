from django import forms
from .models import Posts

class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["category","title","image_url","status","content","slug"]
        # VVV this does the work of <input type="text" placeholder="enter author name">
        widgets={
            "category":forms.Select(attrs={
                "placeholder":"Select"
            }),
            "title":forms.TextInput(attrs={
                "placeholder":"Enter Post Title"
            }),
            "image_url":forms.URLInput(attrs={
                "placeholder":"image.com",
                "class" : 'form-control'
            }),
            "status":forms.TextInput(),
            "content":forms.Textarea(attrs={
                "placeholder":"Enter Post Content",
                "row":2,
                "max_length":1000,
            }),
            "slug":forms.TextInput(attrs={
                "placeholder":"Enter Post Slug"
            })
        }
# attrs-> html attributes
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class":"form-control"
        }
    ), required=True)
    # email = forms.EmailField(widget=forms.EmailInput,required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class":"form-control"
        }
    ), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class":"form-control"
        }
    ), required=True)
    # picture=forms.ImageField(upload_to='profile_pic')
    # document=forms.FileField

    class Meta:
        model = User
        # fields = ['username','email', 'password', 'confirm_password']
        fields = ['username','password', 'confirm_password']


    def clean_username(self): 
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username
    
    # def clean_email(self):
    #     print("email check running")
    #     email=self.cleaned_data.get("email")
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Email already exists")
    #     return email
    
    def clean_password(self):
        print("password clean running")
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("Password is too short")
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords didn't match")
        return cleaned_data
    
from .models import Profile
class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields=['picture']
    
    

    
        


