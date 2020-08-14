from django.shortcuts import render
from .forms import ModelFormFileUpload
from accounts.models import Maker
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def Home(request):
  return render(request, 'MediaFile/home.html')


@method_decorator(login_required, name='dispatch')
class upload_fileCreateView(CreateView):
  
  form_class = ModelFormFileUpload
  template_name = 'MediaFile/media.html'
  success_url = '/accounts/profile'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return super().form_valid(form)

class FileDeleteView(DeleteView):
    model = ModelFormFileUpload.Meta.model
    success_url = '/accounts/profile/'

    def get_queryset(self):
        return Maker.objects.filter(
            user=self.request.user
        )

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)