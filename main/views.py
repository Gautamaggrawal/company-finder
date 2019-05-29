from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import login, authenticate, REDIRECT_FIELD_NAME
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView, PasswordChangeView as BasePasswordChangeView,
    PasswordResetDoneView as BasePasswordResetDoneView, PasswordResetConfirmView as BasePasswordResetConfirmView,
)

from django.views.generic import View, FormView
from django.conf import settings

from django.shortcuts import render, redirect,HttpResponse

from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.generic import *
from hitcount.views import HitCountDetailView
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from django.contrib.auth.models import User
from .models import *
from .forms import *


class LoginView(FormView):
    """
    Provides the ability to login as a user with a username and password
    """
    success_url = '/profile/'
    template_name='login.html'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, allowed_hosts=self.request.get_host()):
            redirect_to = self.success_url
        return redirect_to



class CompanyDetailView(HitCountDetailView):
    model=Company
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = Company.objects.filter()
    context_object_name = 'company'
    count_hit = True
    template_name="company_detail.html"






class SignUpView(FormView):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('/accounts/createprofile/')

class CreateProfileView(FormView):
    form_class = ProfileForm
    template_name = 'CreateProfile.html'

    def get_form_kwargs(self):
        kwargs = super(CreateProfileView, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        print(form.cleaned_data.get('avatar'))
        form.save()
        return redirect('/profile/')

class CreateCompanyView(FormView):
    form_class = Companyform
    template_name = 'Createcompany.html'
    success_url="/"

    def form_valid(self, form):
        form.save()
        return HttpResponse('<script type="text/javascript">window.close()</script>')



from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def uploadimg(request):
    print(request.POST)
    return HttpResponse("aj")


class LogOutView(LoginRequiredMixin, BaseLogoutView):
    template_name = 'logout.html'




class comp(TemplateView):
    template_name = 'main/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        par_obj=UserProfile.objects.get(user=self.request.user)
        print(par_obj)
        # par2_obj=Participants.objects.all()

        context['users'] = par_obj
        context['show']=True


        return context

class IndexPageView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        par_obj=UserProfile.objects.all()
        print(par_obj)
        # par2_obj=Participants.objects.all()

        if par_obj.count()!=0:
        	context['users'] = par_obj
        	context['show']=True
        else:
        	context['data'] = "No users registered"
        	context['show']=False


        return context


