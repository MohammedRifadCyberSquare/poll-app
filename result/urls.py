from django.urls import path
from . import views

app_name = 'result'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('candidates_list/<str:position>', views.candidates_list, name = 'candidates_list'),
    path('show_result/headboy', views.result_headboy, name = 'result_headboy'),
    path('show_result/finearts', views.result_fine_arts, name = 'result_fine_arts'),
    path('show_result/sports_minister', views.result_sports_minister, name = 'result_sports_minister'),
    path('show_result/volunteer_captain', views.result_volunteer_captain, name = 'result_volunteer_captain'),
    path('show_result/assist_head', views.result_assistant_headboy, name = 'result_assistant_headboy'),
    path('show_result/student_editor', views.result_student_editor, name = 'result_student_editor'),

    
 
]