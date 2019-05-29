from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from main.views import IndexPageView,comp,uploadimg,CompanyDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("uploadimage/",uploadimg),
    path('getcompanydetails/<int:pk>', login_required(CompanyDetailView.as_view(),login_url='/login/')),
    path('', IndexPageView.as_view(), name='index'),
    path('profile/', login_required(comp.as_view(),login_url='/login/'), name='profile'),
    path('accounts/', include('main.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
