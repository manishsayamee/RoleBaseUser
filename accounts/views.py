from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .forms import MakerSignUpForm, CheckerSignUpForm
from .models import User






def SignUpView(request):
  return render(request, 'accounts/signup.html')



class MakerSignUpView(CreateView):
  model = User
  form_class = MakerSignUpForm
  template_name = 'accounts/signup_form.html'

  def get_context_data(self, **kwargs):
      kwargs['user_type'] = 'maker'
      return super().get_context_data(**kwargs)

  def form_valid(self, form):
      user = form.save()
      login(self.request, user)
      return redirect('accounts:login')


class CheckerSignUpView(CreateView):
  model = User
  form_class = CheckerSignUpForm
  template_name = 'accounts/signup_form.html'

  def get_context_data(self, **kwargs):
      kwargs['user_type'] = 'checker'
      return super().get_context_data(**kwargs)

  def form_valid(self, form):
      user = form.save()
      login(self.request, user)
      return redirect('accounts:login')




from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .decorators import maker_required, checker_required
from django.utils.decorators import method_decorator
from .models import Maker



@method_decorator(login_required, name='dispatch')
@maker_required
class upload_fileCreateView(CreateView):
  from filecollections.forms import ModelFormFileUpload
  form_class = ModelFormFileUpload
  template_name = 'MediaFile/media.html'
  success_url = '/accounts/profile'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return super().form_valid(form)

from filecollections.forms import ModelFormFileUpload
class upload_listview(ListView):
  template_name = 'accounts/list.html'
  context_object_name = 'data'
  model = Maker
  queryset = Maker.objects.all()

from django.shortcuts import get_object_or_404
@login_required
@checker_required
def update(request, user_id):
  user_object = get_object_or_404(Maker, user_id=user_id)
  if request.method == 'POST':
      form = ModelFormFileUpload(
          request.POST, instance=user_object
      )
      if form.is_valid():
          print("form is valid")
          print(form.cleaned_data)
          form.save()
          return redirect(f'/accounts/update/{user_id}')
      else:
          print("form is invalid")
  else:
      form = ModelFormFileUpload(instance=user_object)

  return render(request, 'accounts/update.html', {
      'form': form
  })



@login_required
@checker_required
def uploadFileDeleteView(request,user_id):
  obj = get_object_or_404(Maker,user_id=user_id)
  obj.delete()
  return redirect(request, 'accounts/list/')


from .forms import LoginForm
from django.contrib.auth import authenticate, login,logout

def Log_Out(request):

  logout(request)
  return redirect('/accounts/login')

@login_required()
def Profile_View(request):

  from .models import Maker
  messages = Maker.objects.filter(user=request.user)
  return render(request, 'accounts/profile.html',{'messages':messages})

def Login_View(request):
  if request.method=='POST':
    form = LoginForm(request.POST)

    if form.is_valid():
      print(form.cleaned_data)

      user=authenticate(username = form.cleaned_data['username'],
                        password = form.cleaned_data['password'])
      if user:
        print("A user is found", user)
        login(request, user)
        return redirect('/accounts/profile')
      else:
        print("User is not found")

  elif request.method == 'GET':
    form = LoginForm()
 
  return render(request, 'accounts/login.html', {'form':form})

    
from .models import Comment
from .forms import commentForm
from django.shortcuts import render, get_object_or_404

def commentPost(request, post_id):
  template_name = 'accounts/comment.html'
  post = get_object_or_404(Comment, id=post_id)
  comments = post.comments.filter(active=True)
  new_comment = None

  if request.method == 'POST':
      comment_form = commentForm(data=request.POST)
      if comment_form.is_valid():
          new_comment = comment_form.save(commit=False)
          new_comment.post = post
          new_comment.save()
  else:
      comment_form = commentForm()

  return render(request, template_name, {'post': post, 'comments': comments,'new_comment': new_comment,    'comment_form': comment_form})
                                      
                                        
                                          