from django.urls import path
from . import views 

# from .views import register_candidate, CandidateLoginView

urlpatterns = [
    path('', views.home, name= 'home'),
    path('home/', views.home, name= 'home'),
    path('login/', views.login_user, name='login'), 

    path('logout/', views.logout_user, name= 'logout'),
    path('job_listing/', views.job_listing, name= 'job_listing'),
    path('about/', views.about, name= 'about'),
    path('contact/', views.contact, name= 'contact'),
    path('job_details/<int:myid>/', views.job_details, name= 'job_details'),
    path('employers/', views.employers, name= 'employers'),
    path('candidates/', views.candidates, name= 'candidates'),
    
    path('candidate_details/<int:myid>', views.candidate_details, name= 'candidate_details'),

    path('search/', views.search_results, name= 'search_results'),
    
    #admin
    path('settings/', views.settings, name= 'settings'),
    path('delete_account/', views.delete_account, name='delete_account'), 


    # User
    path('user_homepage/', views.user_homepage, name= 'user_homepage'),  
    path('register_candidates/', views.register_candidates, name= 'register_candidates'),  
    path('user_profile/', views.user_profile, name= 'user_profile'),
    path('job_apply/<int:myid>/', views.job_apply, name= 'job_apply'),
    path("applied_jobs/", views.applied_jobs, name="applied_jobs"),
    path('delete_applied_job/<int:application_id>/', views.delete_applied_job, name='delete_applied_job'),
    
    path("notification/", views.notification, name="notification"),


    # Company
    path('company_homepage/', views.company_homepage, name= 'company_homepage'),  

    path('register_company/', views.register_company, name= 'register_company'),  
    path('company_homepage/', views.company_homepage, name= 'company_homepage'),  
    path('company_profile/', views.company_profile, name= 'company_profile'),  
    path('add_job/', views.add_job, name= 'add_job'),  
    path('job_list/', views.job_list, name= 'job_list'),  
    path('edit_job/<int:myid>/', views.edit_job, name= 'edit_job'),  
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),

    path('job/delete/<int:job_id>/', views.delete_job, name='delete_job'),

    path('job_detail/<int:myid>/', views.job_detail, name= 'job_detail'),  

    path('all_applicants/', views.all_applicants, name= 'all_applicants'),  
    path('delete-applicant/<int:id>/', views.delete_applicant, name='delete_applicant'),


    path('company/<int:company_id>/vacancies/', views.company_vacancies, name='company_vacancies'),
   
    path('download',views.all_download,name='download')
    
 ]

