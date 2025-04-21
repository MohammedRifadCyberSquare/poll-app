from django.shortcuts import render
from .models import Candidates, Votes
# Create your views here.


def home(request):
    return render(request, 'result/home.html')


def candidates_list(request, position):
    print('position:', position)
    candidates_list = Candidates.objects.filter(cand_post=position)
    return render(request, 'result/candidates_list.html', {'candidates_list': candidates_list, 'position': position})


def result_headboy(request):
    return render(request, 'result/result_headboy.html')

def result_fine_arts(request):
    return render(request, 'result/result_finearts.html')

def result_assistant_headboy(request):
    return render(request, 'result/assistant_headboy.html')

def result_student_editor(request):
    return render(request, 'result/student_editor.html')

def result_sports_minister(request):
    return render(request, 'result/sports_minister.html')

def result_volunteer_captain(request):
    print("In volunteer captain")
    return render(request, 'result/volunteer_captain.html')
