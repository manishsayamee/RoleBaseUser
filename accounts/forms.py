from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.db import transaction

# from classroom.models import Student, Subject, User
from .models import Maker, User

class MakerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):

        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_maker = True
        user.save()
        # maker = Maker.objects.create(user=user)
        return user


class CheckerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_checker = True
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
  username=forms.CharField(max_length=150)
  password = forms.CharField(max_length=128, widget=forms.PasswordInput())


from .models import Comment

class commentForm(forms.ModelForm):
    class Meta:
        from .models import Comment
        model=Comment
        fields =['name','comments']