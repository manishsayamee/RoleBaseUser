from django.urls import include, path

from .views import SignUpView, MakerSignUpView, CheckerSignUpView, Login_View, Log_Out,Profile_View,upload_listview, uploadFileDeleteView, update,commentPost
from filecollections.views import upload_fileCreateView
app_name='accounts'

urlpatterns = [

  
    

    path('signup/', SignUpView, name='signup'),
    path('login/', Login_View,name='login'),
    path('logout/', Log_Out, name='logout'),
    path('profile/', Profile_View, name='profile'),
    path('signup/maker/', MakerSignUpView.as_view(), name='maker_signup'),
    path('signup/checker/', CheckerSignUpView.as_view(), name='checker_signup'),
    path('list/',upload_listview.as_view(), name='list'),
    path('upload/',upload_fileCreateView.as_view, name='upload'),
    path('update/<int:user_id>/',update,name='update'),
    path('delete/<int:user_id>/', uploadFileDeleteView, name="delete"),
    path('comment/<int:post_id>/', commentPost, name='comment'),
    


]