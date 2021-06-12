from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='ridit-home'),
  path('',views.school,name='school'),
  path('',views.partner,name='partner'),
  path('',views.chauffer,name='chauffer'),
  path('',views.puc,name='puc'),
  path('',views.ch,name='ch'),
  path('success/',views.success,name='success'),
  path('commingsoon/',views.comming_soon,name='soon'),
  path('faq/',views.faq,name='faq'),
  path('drivingfaq/',views.driveFAQ,name='driveFAQ'),
  path('pucfaq/',views.pucFAQ,name='pucFAQ'),
  path('chauffeurfaq/',views.chauffeurFAQ,name='chauffeurFAQ'),
  path('licensefaq/',views.LicenseFAQ,name='licenseFAQ'),
]