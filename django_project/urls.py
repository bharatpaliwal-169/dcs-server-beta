from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.i18n import JavaScriptCatalog
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from ridit import views as ridit_views
#from employee_reg import views as emp_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', include('ridit.urls')),
    path('school/', ridit_views.school, name='school'),
    path('puc/', ridit_views.puc, name='puc'),
    path('chauffer/', ridit_views.chauffer, name='chauffer'),
    path('partner/', ridit_views.partner, name='partner'),
    path('ch/', ridit_views.ch, name='ch'),
    path('success/', ridit_views.ch, name='success'),
    path('insurance/', ridit_views.insurance, name='insurance'),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript-catalog'),#for datepicker functionality in forms
]

