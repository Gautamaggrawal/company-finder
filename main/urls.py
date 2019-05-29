from django.urls import path

from .views import (
     LoginView,SignUpView,CreateProfileView,LogOutView,CreateCompanyView)

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='log_in'),
    path('createprofile/',CreateProfileView.as_view(),name="create_profile"),
    path('createcompany/',CreateCompanyView.as_view(),name="create_company"),
    path('logout/', LogOutView.as_view(), name='log_out'),
    path('signup/', SignUpView.as_view(), name='sign_up'),

]