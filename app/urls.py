from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
	   path('',views.firstpage,name='firstpage'),
     path('login/',views.edu,name = 'edu'),
     path('login/add/',views.educrev,name='educrev'),
     path('login/next/',views.EducationView.as_view(),name='education'),
     path ('login/next/<int:pk>',views.UpdatepostView.as_view(), name='updateview'),
     path('login/next/save/',views.job345, name='job345'),
     path('login/next/save/job/',views.JobView.as_view(),name='job'),
     path ('login/next/save/job/<int:pk>',views.UpdatepostViewjob.as_view(), name='updateviewjob'),
     path ('login/next/save/job/<int:pk>/delete/',views.Deletepostviewjob.as_view(), name='deleteviewjob'),
     path('check',views.formfunction),
     path ('login/next/<int:pk>/delete/',views.Deletepostview.as_view(), name='deleteview'),
     

     path('login/next/job/skill/',views.addonstest,name='extra'),#Tejaswini
     path('login/next/job/skill/addonemorefield/',views.addonemoreaddon,name='addonemoreaddon'),
     path('login/next/job/skill/fieldadd/',views.ExtrafieldView.as_view(),name='extrafi'),
     path ('login/next/job/skill/fieldadd/<int:pk>',views.UpdateEFView.as_view(), name='updateviewef'),
     path ('login/next/job/skill/fieldadd/<int:pk>/delete/',views.DeleteEFview.as_view(), name='deleteviewef'),
     path('login/next/job/skill/final/',views.home,name='home1'),#Tejaswini




      #BELOW URLS ADDED BY SIRI.

         #path('login/back/',views.backopt,name='backopt'),
     path('login/next/skills/',views.skilledu,name='skillsedu'),
         # path('login/next/add/',views.jobadd,name='jobadd'),
     path('login/next/skills/add',views.skillseducrev,name='skillseducrev'),
     path('login/next/skills/next/',views.SkillsView.as_view(),name='skillsview'),
     path('login/next/skills/next/<int:pk>',views.skillUpdatepostView.as_view(),name='skillsupdateview'),
         #path ('login/next/job/<int:pk>',views.UpdatepostView.as_view(), name='updateview'),
     path ('login/next/skills/next/<int:pk>/delete/',views.skillDeletepostview.as_view(), name='skillsdeleteview'),

         #path('login/next/job/skill/',views.addonstest,name='home'),
         #path('login/next/job/skill/addonemorefield/',views.addonemoreaddon,name='home'),
         #path('login/next/job/skill/next/fieldadd/',views.home,name='home'),
     path('login/next/job/skill/next/fieldadd/pdf_view/',views.viewPDF.as_view(),name='pdf_view'),

          #path('login/back/',views.backopt,name='backopt'),
          #path('login/next/job/',views.skillsfun,name='skillfun'),
          #path('login/next/add/',views.jobadd,name='jobadd'),
          #path('login/next/job/add/',views.skillsadd,name='skillfun'),
          #path('login/next/job/skill/',views.addons,name='home'),
          #path('login/next/job/skill/',views.addonstest,name='home'),
          #path('login/next/job/skill/addonemorefield/',views.addonemoreaddon,name='home'),
          #path('login/next/job/skill/fieldadd/',views.home,name='home'),
          #path('login/next/job/skill/fieldadd/pdf_view/',views.viewPDF.as_view(),name='pdf_view'),
          


]