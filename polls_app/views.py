from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions' :latest_questions}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("this is question %s" % question_id)
