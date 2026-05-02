from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from posts.models import Post
from profiles.models import Profile

class LoginForm(AuthenticationForm):
    pass


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "caption"]
        widgets = {
            "caption": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "¿Qué estás pensando?"
            })
        }


class EditProfile(forms.ModelForm):
    username = forms.CharField(max_length=150)

    class Meta:
        model = Profile
        fields = ["profile_picture", "biography", "birth_date"]
        widgets = {
            "birth_date": forms.DateInput(format='%Y-%m-%d', attrs={
                "type": 'date',
            }),
            'bio': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super(EditProfile, self).__init__(*args, **kwargs)

        if self.instance and self.instance.user:
            self.fields['username'].initial = self.instance.user.username
    