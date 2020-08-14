from accounts.models import Maker
from django.forms import ModelForm


class ModelFormFileUpload(ModelForm):
  class Meta:
    model = Maker
    fields = ['file', 'description']


