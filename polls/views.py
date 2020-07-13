from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
# from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.db.models import F
from .models import Choice, Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 方式1
    # output = ', '.join([q.question_text for q in latest_question_list])

    # 方式2
    # template = loader.get_template('polls/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))

    # 方式3
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    # 方式1
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("没有相应的问题存在！")

    # 方式2
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
      selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
      # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "请勾选一个回答！",
        })
    else:
      selected_choice.votes = F('votes') + 1
      selected_choice.save()
      return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

