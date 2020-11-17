from random import randint
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from app.forms import LoginForm, SignUpForm, SettingsForm, AskForm

quests = ['Что было раньше: яйцо или курица?', 'Что такое программирование?', 'Что такое программирование?',
          'Что такое отладка?', 'Назовите типы ошибок, которые могут возникнуть в программе', 'Расскажите о синтаксических ошибках',
          'Расскажите об ошибке времени выполнения', 'Расскажите о логических ошибках', 'Что такое блок-схема?',
          'Что такое алгоритм?', 'Что такое цикл?']
answs = ['правильный ответ', 'ответ не по этой теме', 'анектод', 'другой правильный ответ']

tags = []
for i in range(1,5):
    tags.append({
        'id': i - 1,
        'tag_name': 'тег ' + str(i)
    })

questions = []
for i in range(1,100):
    questions.append({
        'title': 'Название ' + str(i),
        'id': i,
        'text': quests[randint(0, len(quests)-1)],
        'tag1': tags[randint(0, 3)],
        'tag2':  tags[randint(0, 3)]
    })


answers = []
for i in range(1,5):
    answers.append({
        'text': answs[randint(0, 3)]
    })

def paginate(request, objects_list, default_limit=10, pages_count=None):
    limit = default_limit
    page = int(request.GET.get('page', 1))
    paginator = Paginator(objects_list, limit)
    page = paginator.page(page)
    start = page.number - pages_count
    if start < 0:
        start = 0
    page_range = paginator.page_range[start: page.number + int(pages_count / 3)]
    return page, page_range


def index(request):
    page, page_range = paginate(request, questions, 10, 10)
    return render(request, 'app/index.html', {
        'questions': page.object_list,
        'page': page,
        'page_range': page_range,
    })

def ask(request):
    form = AskForm()
    return render(request, 'app/ask.html', {
        'form': form,
    })


def question(request, pk):
    question = questions[pk - 1]
    page, page_range = paginate(request, answers, 10, 10)
    return render(request, 'app/question.html', {
        'question': question,
        'answers': page.object_list,
        'page': page,
        'page_range': page_range,
    })

def login(request):
    form = LoginForm()
    return render(request, 'app/login.html', {
        'form': form,
    })

def signup(request):
    form = SignUpForm()
    return render(request, 'app/signup.html', {
        'form': form,
    })

def settings(request):
    form = SettingsForm()
    return render(request, 'app/settings.html', {
        'form': form,
    })


def tag(request, pk):
    tag = tags[pk]
    quest = [i for i in questions if (i['tag1']['id'] == pk or i['tag2']['id'] == pk)]
    page, page_range = paginate(request, quest, 10, 10)
    return render(request, 'app/tag.html', {
        'tag': tag,
        'questions': page.object_list,
        'page': page,
        'page_range': page_range,
    })

def hot(request):
    quest = questions[0:11]
    page, page_range = paginate(request, quest, 10, 10)
    return render(request, 'app/hot.html', {
        'questions': page.object_list,
        'page': page,
        'page_range': page_range,
    })
